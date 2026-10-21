#ifndef MyAppVersion
  #define MyAppVersion "1.0.0"
#endif

#define AppSource AddBackslash(SourcePath) + "dist\Poketupi"

[Setup]
AppId={{7344E7DF-3630-4E3A-94B6-DF171178A052}
AppName=Poketupi
AppVersion={#MyAppVersion}
AppPublisher=Poketupi
DefaultDirName={localappdata}\Programs\Poketupi
DefaultGroupName=Poketupi
UninstallDisplayIcon={app}\Poketupi.exe
OutputDir=installer-output
OutputBaseFilename=Poketupi-Setup-{#MyAppVersion}
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "Criar um atalho na área de trabalho"; Flags: unchecked

[Files]
Source: "{#AppSource}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Poketupi"; Filename: "{app}\Poketupi.exe"
Name: "{autodesktop}\Poketupi"; Filename: "{app}\Poketupi.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Poketupi.exe"; Description: "Abrir Poketupi"; Flags: nowait postinstall skipifsilent
