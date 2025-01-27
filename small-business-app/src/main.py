# FILE: /small-business-app/small-business-app/src/main.py
from cli.cli_interface import CLIInterface

def main():
    cli = CLIInterface()
    cli.run()

if __name__ == "__main__":
    main()