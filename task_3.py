import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def print_tree(path: Path, indent: str = "") -> None:
    items = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        branch = "└── " if is_last else "├── "
        next_indent = indent + ("    " if is_last else "│   ")

        if item.is_dir():
            print(indent + branch + Fore.BLUE + item.name + Style.RESET_ALL)
            print_tree(item, next_indent)
        else:
            print(indent + branch + Fore.GREEN + item.name + Style.RESET_ALL)

def main():
    if len(sys.argv) != 2:
        print("Usage: python task_3.py <path_to_directory>")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + "Error: path does not exist." + Style.RESET_ALL)
        sys.exit(1)

    if not dir_path.is_dir():
        print(Fore.RED + "Error: path is not a directory." + Style.RESET_ALL)
        sys.exit(1)

    print(Fore.BLUE + dir_path.name + Style.RESET_ALL)
    print_tree(dir_path)

if __name__ == "__main__":
    main()
