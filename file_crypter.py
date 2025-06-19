#!/usr/bin/env python3

from cryptography.fernet import Fernet
import argparse
import logging
import sys
import os

PROGRAM = "File Crypter"
DESCRIPTION = "A file encrypter and decrypter using Fernet symmetric encryption"
VERSION = "0.1.0"

logging.basicConfig(
    filename="output.log",
    filemode="w",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def generate_key(path="key.key"):
    key = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(key)
    print(f"[+] Key saved to {path}")


def load_key(path="key.key"):
    with open(path, "rb") as f:
        key = f.read()
    return Fernet(key)


def encrypt_file(input_file, output_file, fernet):
    if os.path.exists(output_file):
        confirm = input(f"[!] {output_file} already exists. Overwrite? [y/N]: ").lower()
        if confirm not in ("y", "yes"):
            print("[!] Encryption cancelled.")
            return

    with open(input_file, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(output_file, "wb") as f:
        f.write(encrypted)
    print(f"[+] Encrypted file saved to {output_file}")


def decrypt_file(input_file, output_file, fernet):
    if os.path.exists(output_file):
        confirm = input(f"[!] {output_file} already exists. Overwrite? [y/N]: ").lower()
        if confirm not in ("y", "yes"):
            print("[!] Decryption cancelled.")
            return

    with open(input_file, "rb") as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted)
    with open(output_file, "wb") as f:
        f.write(decrypted)
    print(f"[+] Decrypted file saved to {output_file}")


def parse_args():
    parser = argparse.ArgumentParser(prog=PROGRAM, description=DESCRIPTION)
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {VERSION}"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # generate key
    parser_key = subparsers.add_parser("genkey", help="Generate a new key")
    parser_key.add_argument(
        "-k", "--key", default="key.key", help="Where to save the key file"
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
        "-k", "--key", default="key.key", help="Key file to use"
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
        "-k", "--key", default="key.key", help="Key file to use"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if args.command == "genkey":
        generate_key(args.key)
    else:
        fernet = load_key(args.key)
        if args.command == "encrypt":
            encrypt_file(args.file, args.out, fernet)
        elif args.command == "decrypt":
            decrypt_file(args.file, args.out, fernet)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception:
        logging.critical("Unhandled exception occurred", exc_info=True)
        sys.exit(1)
