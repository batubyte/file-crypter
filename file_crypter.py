#!/usr/bin/env python3

import argparse
import subprocess
import sys
import os
from typing import Tuple
import platform
from pathlib import Path

from cryptography.fernet import Fernet
from rich.color import Color
from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.theme import Theme

PROGRAM = "file-crypter"
DESCRIPTION = "A file encrypter and decrypter"
VERSION = "0.1.2"

console = Console()


def get_default_key_path():
    system = platform.system()

    if system == "Windows":
        base = Path(os.getenv('APPDATA'))
    elif system == "Darwin":
        base = Path.home() / "Library" / "Application Support"
    else:
        base = Path.home() / ".local" / "share"

    path = base / "file-crypter"
    path.mkdir(parents=True, exist_ok=True)
    return path / "fernet.key"


DEFAULT_KEY_PATH = get_default_key_path()


def generate_key():
    return Fernet.generate_key()


def save_key(key: bytes, path: str):
    with open(path, "wb") as f:
        f.write(key)
    console.print(f"Key saved to {path}")


def read_key(path: str):
    with open(path, "rb") as f:
        return f.read()


def encrypt_file(input_path: str, key: bytes):
    fernet = Fernet(key)
    input_file = Path(input_path)

    with open(input_file, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(input_file, "wb") as f:
        f.write(encrypted)

    encrypted_path = input_file.with_suffix(input_file.suffix + ".encrypted")
    input_file.rename(encrypted_path)

    console.print(f"Encrypted: {encrypted_path}")


def decrypt_file(input_path: str, key: bytes):
    fernet = Fernet(key)
    input_file = Path(input_path)

    with open(input_file, "rb") as f:
        data = f.read()

    decrypted = fernet.decrypt(data)

    with open(input_file, "wb") as f:
        f.write(decrypted)

    if input_file.suffix == ".encrypted":
        original_path = input_file.with_suffix("")
        input_file.rename(original_path)
        input_file = original_path

    console.print(f"Decrypted: {input_file}")



def process_directory(path: str, action: str, key: bytes):
    p = Path(path)
    for file in p.rglob("*"):
        if file.is_file():
            if action == "encrypt":
                encrypt_file(file, key)
            elif action == "decrypt":
                decrypt_file(file, key)


class RichCLI:
    @staticmethod
    def blend_text(
        message: str, color1: Tuple[int, int, int], color2: Tuple[int, int, int]
    ) -> Text:
        """Blend text from one color to another."""
        text = Text(message)
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        dr = r2 - r1
        dg = g2 - g1
        db = b2 - b1
        size = len(text)
        for index in range(size):
            blend = index / size
            color = f"#{int(r1 + dr * blend):02X}{int(g1 + dg * blend):02X}{int(b1 + db * blend):02X}"
            text.stylize(color, index, index + 1)
        return text

    @staticmethod
    def print_help(parser: argparse.ArgumentParser) -> None:
        class OptionHighlighter(RegexHighlighter):
            highlights = [
                r"(?P<switch>\-\w)",
                r"(?P<option>\-\-[\w\-]+)",
            ]

        highlighter = OptionHighlighter()
        rich_console = Console(
            theme=Theme({"option": "bold cyan", "switch": "bold green"}),
            highlighter=highlighter,
        )

        console.print(
            f"\n[b]{PROGRAM}[/b] [magenta]v{VERSION}[/] \n[dim]{DESCRIPTION}\n",
            justify="center",
        )
        console.print(f"Usage: [b]{PROGRAM}[/b] [[b]options[/]] [b cyan]<...>\n")

        table = Table(highlight=True, box=None, show_header=False)
        for action in parser._actions:
            if not action.option_strings:
                continue
            opts = [highlighter(opt) for opt in action.option_strings]
            help_text = Text(action.help or "")
            if action.metavar:
                opts[-1] += Text(f" {action.metavar}", style="bold yellow")
            table.add_row(*opts, help_text)

        rich_console.print(
            Panel(table, border_style="dim", title="options", title_align="left")
        )

        footer_console = Console()
        footer_console.print(
            RichCLI.blend_text(
                "batubyte.github.io",
                Color.parse("#b169dd").triplet,
                Color.parse("#542c91").triplet,
            ),
            justify="right",
            style="bold",
        )


def main():
    parser = argparse.ArgumentParser(prog=PROGRAM, description=DESCRIPTION, add_help=False)
    parser.add_argument("-h", "--help", action="store_true", help="Show help message")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    parser.add_argument("-u", "--update", action="store_true", help="Update program")
    parser.add_argument("-g", "--generate", nargs="?", const=str(DEFAULT_KEY_PATH), help=f"Generate new key (Default: {DEFAULT_KEY_PATH})")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt file or directory")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt file or directory")
    parser.add_argument("-f", "--file", type=str, help="Path to file")
    parser.add_argument("-r", "--dir", type=str, help="Path to directory")
    parser.add_argument("-k", "--key", type=str, help="Path to key file")

    if len(sys.argv) == 1 or sys.argv[1] in ("?", "-h", "--help"):
        RichCLI.print_help(parser)
        return

    args = parser.parse_args()

    if args.version:
        console.print(f"{PROGRAM} {VERSION}")
        return

    if args.update:
        subprocess.run(
            ["pipx", "install", "--force", "git+https://github.com/batubyte/file-crypter"],
            check=True,
        )
        return


    if args.generate is not None:
        path = args.generate if isinstance(args.generate, str) else str(DEFAULT_KEY_PATH)
        key = generate_key()
        save_key(key, path)
        return

    if args.key:
        key = read_key(args.key)
    else:
        if DEFAULT_KEY_PATH.exists():
            key = read_key(DEFAULT_KEY_PATH)
        else:
            console.print("[red]No key found. Generate one first using -g[/red]")
            return

    if args.encrypt:
        if args.file:
            encrypt_file(args.file, key)
        if args.dir:
            process_directory(args.dir, "encrypt", key)

    if args.decrypt:
        if args.file:
            decrypt_file(args.file, key)
        if args.dir:
            process_directory(args.dir, "decrypt", key)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        console.print_exception()
        sys.exit(1)
