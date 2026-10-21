# Instalador para Windows

Para gerar o instalador, instale o Python 3.10 a 3.13 e o Inno Setup 6.
No PowerShell, execute `powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\build_windows.ps1`
a partir da pasta do repositório. A política de execução só é flexibilizada
para esse processo; nenhuma configuração do Windows é alterada.

O script cria um ambiente Python isolado, instala as dependências de
empacotamento e inclui os sprites, as imagens e as músicas no aplicativo. O
instalador resultante fica em
`Trabalho Pokemon\installer-output\Poketupi-Setup-1.0.0.exe` e pode ser
instalado sem permissões de administrador. Para definir outra versão, use
`.\build_windows.ps1 -Version 1.2.3`.
