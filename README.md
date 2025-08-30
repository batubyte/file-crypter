> [!NOTE]
> Update soon

## 🔐 File Crypter
<img width="872" height="363" alt="image" src="https://github.com/user-attachments/assets/6766bf65-5b16-4ced-a916-2fa4d282506d" />

### 📦 Installation
```bash
pipx install git+https://github.com/batubyte/file-crypter
```
```bash
file-crypter
```

### ✨ Features
```py
# Generate key
> file-crypter --generate C:\...\fernet.key

# Crypt file
> file-crypter --key C:\...\fernet.key --encrypt --file my_file.txt
> file-crypter --key C:\...\fernet.key --decrypt --file my_file.txt.encrypted

# Crypt directory
> file-crypter --key C:\...\fernet.key --encrypt --dir MyFolder
> file-crypter --key C:\...\fernet.key --decrypt --dir MyFolder
```
