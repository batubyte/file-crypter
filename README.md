# 🔐 File Crypter
![image](https://github.com/user-attachments/assets/9da68520-6773-4441-9b7b-5a33ae2f0471)

## 📦 Installation
```bash
pipx install git+https://github.com/batubyte/file-crypter
```
```bash
file-crypter
```

## ✨ Features
```py
$ file_crypter genkey -k C:\secret.key
$ file_crypter encrypt -f file.dat -o file.enc -k C:\secret.key
$ file_crypter decrypt -f file.enc -o file.dec -k C:\secret.key
```

## 📄 Fernet documentation
https://cryptography.io/en/latest/fernet/
