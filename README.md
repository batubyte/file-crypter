# File Crypter
![image](https://github.com/user-attachments/assets/3ea1856e-a8fb-459d-b2fc-8bf9b5a41547)

## 🪟 Windows
### 📦 Installation
```batch
::Install WinGet
::Do Win + X -> A
Start-BitsTransfer -Source https://aka.ms/getwinget -Destination AppInstaller.msixbundle; Add-AppxPackage .\AppInstaller.msixbundle; Remove-Item .\AppInstaller.msixbundle

::Install Git
winget install --id=Git.Git -e --accept-package-agreements --accept-source-agreements

::Install uv
::Do Win + R -> cmd
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" && setx Path=%USERPROFILE%\.local\bin;%Path%

:: Install project
rmdir /s /q "%USERPROFILE%\Documents\file-crypter" & git clone https://github.com/batubyte/file-crypter "%USERPROFILE%\Documents\file-crypter"
```
#### ▶ Run
```batch
::Do Win + R -> cmd
cd %USERPROFILE%\Documents\file-crypter
uv sync & uv run file-crypter.py
```

## 🐧 Linux (Ubuntu/Debian)
### 📦 Installation
```bash
sudo apt update && sudo apt install -y git
curl -LsSf https://astral.sh/uv/install.sh | sh
rm -rf ~/Documents/file-crypter && git clone https://github.com/batubyte/file-crypter.git ~/Documents/file-crypter
```
#### ▶ Run
```bash
cd ~/Documents/file-crypter
uv sync && uv run file-crypter.py
```
