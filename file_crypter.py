#!/usr/bin/env python3

from cryptography.fernet import Fernet
from rich.console import Console
from rich.panel import Panel
import subprocess
import argparse
import sys
import os

PROGRAM = "file_crypter"
DESCRIPTION = "A file encrypter and decrypter using Fernet symmetric encryption"
VERSION = "0.1.1"

console = Console()
error_console = Console(stderr=True, style="bold red")


def update():
    subprocess.run(
        ["pipx", "install", "--force", "git+https://github.com/batubyte/file-crypter"],
        check=True,
    )


def generate_key(path="secret.key"):
    key = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(key)
    console.print(f"[green][+][/] Key saved to {path}")


def load_key(path="secret.key"):
    with open(path, "rb") as f:
        key = f.read()
    return Fernet(key)


def encrypt_file(input_file, output_file, fernet):
    if os.path.exists(output_file):
        confirm = input(f"[yellow][!][/] {output_file} already exists. Overwrite? [y/N]: ").lower()
        if confirm not in ("y", "yes"):
            console.print("[yellow][!][/] Encryption cancelled.")
            return

    with open(input_file, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(output_file, "wb") as f:
        f.write(encrypted)
    console.print(f"[green][+][/] Encrypted file saved to {output_file}")


def decrypt_file(input_file, output_file, fernet):
    if os.path.exists(output_file):
        confirm = input(f"[yellow][!][/] {output_file} already exists. Overwrite? [y/N]: ").lower()
        if confirm not in ("y", "yes"):
            console.print("[yellow][!][/] Decryption cancelled.")
            return

    with open(input_file, "rb") as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted)
    with open(output_file, "wb") as f:
        f.write(decrypted)
    console.print(f"[green][+][/] Decrypted file saved to {output_file}")


def parse_args():
    parser = argparse.ArgumentParser(
        prog=PROGRAM, description=DESCRIPTION, add_help=False
    )
    
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s version {VERSION}"
    )
    parser.add_argument(
        "-h", "--help", action="store_true", help="show this help message"
    )
    parser.add_argument(
        "-u", "--update", action="store_true", help="update file-crypter"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # generate key
    parser_key = subparsers.add_parser("genkey", help="Generate a new key")
    parser_key.add_argument(
        "-o", "--out", default="secret.key", help="Where to save the key file"
    )

    # encrypt
    parser_encrypt = subparsers.add_parser("encrypt", help="Encrypt a file")
    parser_encrypt.add_argument(
        "-f", "--file", required=True, help="Input file to encrypt"
    )
    parser_encrypt.add_argument(
        "-o", "--out", default="file.enc", help="Encrypted output file"
    )
    parser_encrypt.add_argument(
        "-k", "--key", default="secret.key", help="Key file to use"
    )

    # decrypt
    parser_decrypt = subparsers.add_parser("decrypt", help="Decrypt a file")
    parser_decrypt.add_argument(
        "-f", "--file", required=True, help="Encrypted input file"
    )
    parser_decrypt.add_argument(
        "-o", "--out", default="file.dec", help="Decrypted output file"
    )
    parser_decrypt.add_argument(
        "-k", "--key", default="secret.key", help="Key file to use"
    )
    
    if len(sys.argv) == 1 or '--help' in sys.argv or '-h' in sys.argv:
        console.print(
            Panel(
                parser.format_help(),
                title=" ".join(sys.argv),
                border_style="cyan",
                width=80,
            )
        )
        sys.exit()

    return parser.parse_args()


def main():
    args = parse_args()
    
    if args.command == "genkey":
        generate_key(args.out)
    else:
        fernet = load_key(args.key)
        if args.command == "encrypt":
            encrypt_file(args.file, args.out, fernet)
        elif args.command == "decrypt":
            decrypt_file(args.file, args.out, fernet)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        error_console.log(f"Error: {e}")
        sys.exit(1)
