> [!NOTE]
> Update coming soon

## 🔐 File Crypter
![image](https://github.com/user-attachments/assets/febcb6d7-6d21-42e9-a8f4-65286aad11e9)

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
> file-crypter generate fernet.key

# Crypt file
> file-crypter -k fernet.key --encrypt --file my_file.txt
> file-crypter -k fernet.key --decrypt --file my_file.txt.encrypted

# Crypt directory
> file-crypter -k fernet.key --encrypt --dir MyFolder
> file-crypter -k fernet.key --decrypt --dir MyFolder
```
