# 🔐 File Crypter
![image](https://github.com/user-attachments/assets/3ea1856e-a8fb-459d-b2fc-8bf9b5a41547)

## 📦 Install
### Linux (Ubuntu/Debian)
```bash
sudo apt update && sudo apt install -y git
curl -LsSf https://astral.sh/uv/install.sh | sh && export PATH="$HOME/.local/bin:$PATH"
rm -rf ~/Documents/file-crypter && git clone https://github.com/batubyte/file-crypter.git ~/Documents/file-crypter && chmod +x ~/Documents/file-crypter/file_crypter.py
```
### Windows
```batch
:: WinGet
:: Do Win + X -> A
Start-BitsTransfer -Source https://aka.ms/getwinget -Destination AppInstaller.msixbundle; Add-AppxPackage .\AppInstaller.msixbundle; Remove-Item .\AppInstaller.msixbundle

:: Git
winget install --id=Git.Git -e --accept-package-agreements --accept-source-agreements

:: uv
:: Do Win + R -> cmd
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" && setx Path=%USERPROFILE%\.local\bin;%Path%

:: Repository
rmdir /s /q "%USERPROFILE%\Documents\file-crypter" & git clone https://github.com/batubyte/file-crypter.git "%USERPROFILE%\Documents\file-crypter"
```

## ⚡ Run
### Linux
```bash
cd ~/Documents/file-crypter && uv sync && uv run file_crypter.py -h
```
### Windows
```batch
:: Do Win + R -> cmd
cd %USERPROFILE%\Documents\file-crypter & uv sync & uv run file_crypter.py -h
```

## 📚 Fernet documentation
https://cryptography.io/en/latest/fernet/
