# File Crypter
![image](https://github.com/user-attachments/assets/8a141ee4-8b0e-4fcc-9a6b-06610a32ecf8)

## Installation
### Linux (Ubuntu/Debian)
```bash
sudo apt update && sudo apt install -y git
curl -LsSf https://astral.sh/uv/install.sh | sh
cd ~/Documents
git clone https://github.com/batubyte/file-crypter.git
```
### Windows
```batch
::Install WinGet
::Do Win + X -> A
Start-BitsTransfer -Source https://aka.ms/getwinget -Destination AppInstaller.msixbundle; Add-AppxPackage .\AppInstaller.msixbundle; Remove-Item .\AppInstaller.msixbundle

::Install Git
winget install --id=Git.Git -e --accept-package-agreements --accept-source-agreements

::Install uv
::Do Win + R -> cmd
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
set Path=%USERPROFILE%\.local\bin;%Path%

:: Install project
cd %USERPROFILE%\Documents
git clone https://github.com/batubyte/file-crypter.git
```

## Run
### Linux
```bash
cd ~/Documents/file-crypter
uv sync
uv run file-crypter.py
```
### Windows
```batch
::Win + R -> cmd
cd %USERPROFILE%\Documents\file-crypter
uv sync
uv run file-crypter.py
```

## Nmap docs
https://nmap.org/book/man.html
