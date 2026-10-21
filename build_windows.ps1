[CmdletBinding()]
param(
    [ValidatePattern('^\d+\.\d+\.\d+$')]
    [string]$Version = '1.0.0'
)

$ErrorActionPreference = 'Stop'

$projectRoot = Join-Path $PSScriptRoot 'Trabalho Pokemon'
$python = Join-Path $projectRoot '.venv\Scripts\python.exe'
$requirements = Join-Path $projectRoot 'requirements-build.txt'
$buildRoot = Join-Path $env:TEMP "Poketupi-build-$([guid]::NewGuid().ToString('N'))"
$distRoot = Join-Path $projectRoot 'dist'
$appOutput = Join-Path $distRoot 'Poketupi'
$spritesRoot = Join-Path $projectRoot 'sprites'
$setupScript = Join-Path $projectRoot 'installer.iss'
$installerOutput = Join-Path $projectRoot 'installer-output'

if (-not (Test-Path -LiteralPath $python)) {
    $pythonLauncher = Get-Command py.exe -ErrorAction SilentlyContinue
    if ($pythonLauncher) {
        & $pythonLauncher.Source -3 -m venv (Join-Path $projectRoot '.venv')
    }
    else {
        $pythonCommand = Get-Command python.exe -ErrorAction SilentlyContinue
        if (-not $pythonCommand) {
            throw 'Python 3 não foi encontrado. Instale o Python 3.10 ou superior antes de continuar.'
        }
        & $pythonCommand.Source -m venv (Join-Path $projectRoot '.venv')
    }

    if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $python)) {
        throw 'Não foi possível criar o ambiente virtual Python do projeto.'
    }
}

$pythonVersion = & $python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
if ($LASTEXITCODE -ne 0 -or $pythonVersion -notmatch '^3\.(1[0-3])$') {
    throw 'O build requer Python entre as versões 3.10 e 3.13.'
}

& $python -m pip install --disable-pip-version-check -r $requirements
if ($LASTEXITCODE -ne 0) {
    throw 'A instalação das dependências do build falhou.'
}

$compiler = Get-Command ISCC.exe -ErrorAction SilentlyContinue
if ($compiler) {
    $compilerPath = $compiler.Source
}
else {
    $compilerCandidates = @(
        (Join-Path $env:LOCALAPPDATA 'Programs\Inno Setup 6\ISCC.exe'),
        (Join-Path $env:ProgramFiles 'Inno Setup 6\ISCC.exe'),
        (Join-Path ${env:ProgramFiles(x86)} 'Inno Setup 6\ISCC.exe')
    )
    $compilerPath = $compilerCandidates |
        Where-Object { $_ -and (Test-Path -LiteralPath $_) } |
        Select-Object -First 1
}

if (-not $compilerPath) {
    throw 'Inno Setup 6 não foi encontrado. Instale-o e execute este script novamente.'
}

New-Item -ItemType Directory -Force -Path $buildRoot, $distRoot | Out-Null
if (Test-Path -LiteralPath $appOutput) {
    Remove-Item -LiteralPath $appOutput -Recurse -Force
}

$pyinstallerArguments = @(
    '--noconfirm',
    '--clean',
    '--windowed',
    '--onedir',
    '--name', 'Poketupi',
    '--paths', $projectRoot,
    '--distpath', $distRoot,
    '--specpath', $buildRoot,
    '--workpath', (Join-Path $buildRoot 'pyinstaller')
)

$assetFiles = Get-ChildItem -LiteralPath $projectRoot -File |
    Where-Object { $_.Extension -in @('.png', '.jpg', '.mp3') }

foreach ($asset in $assetFiles) {
    $pyinstallerArguments += @('--add-data', "$($asset.FullName);.")
}

$pyinstallerArguments += @('--add-data', "$spritesRoot;sprites")
$pyinstallerArguments += (Join-Path $projectRoot '_frontendteste.py')

Push-Location $projectRoot
try {
    & $python -m PyInstaller @pyinstallerArguments
    if ($LASTEXITCODE -ne 0) {
        throw 'O empacotamento do jogo com PyInstaller falhou.'
    }
}
finally {
    Pop-Location
    if (Test-Path -LiteralPath $buildRoot) {
        Remove-Item -LiteralPath $buildRoot -Recurse -Force
    }
}

& $compilerPath "/DMyAppVersion=$Version" $setupScript "/O$installerOutput" "/FPoketupi-Setup-$Version"
if ($LASTEXITCODE -ne 0) {
    throw 'A compilação do instalador do Windows falhou.'
}

$installer = Join-Path $installerOutput "Poketupi-Setup-$Version.exe"
if (-not (Test-Path -LiteralPath $installer)) {
    throw "O instalador esperado não foi gerado: $installer"
}

Write-Host "Instalador criado com sucesso: $installer"
