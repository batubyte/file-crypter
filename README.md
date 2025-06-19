# 🔐 File Crypter
![image](https://github.com/user-attachments/assets/3ea1856e-a8fb-459d-b2fc-8bf9b5a41547)

## 📦 Installation
1. Install [Python](https://www.python.org/downloads) with **"add to PATH"** option
2. Install [pipx](https://pipx.pypa.io/latest/installation/#installing-pipx)
3. ``pipx install git+https://github.com/batubyte/file-crypter``
4. ``file_crypter``

## Features
```py
> file_crypter genkey -k C:\example.key
> file_crypter encrypt -f file.dat -o file.enc -k C:\example.key
> file_crypter decrypt -f file.enc -o file.dec -k C:\example.key
```

## 📚 Fernet documentation
https://cryptography.io/en/latest/fernet/
