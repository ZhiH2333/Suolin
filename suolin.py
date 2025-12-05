## coding: utf-8
## suolin.py

## Import standard modules
import os
import sys
import time
import logging
import threading

## Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='laster.log', filemode='w')


## Import necessary modules
try:
    import rich
except ImportError:
    logger.error("necessary module missing.", exc_info=True)
    print("[ERROR]: Some important modules are missing. Please run 'pip install -r requirements.txt' to install them.For more information, please refer to the logs in the program directory.")
    sys.exit(1)
## Initialize the console
console = rich.console.Console()

## Import internal modules
try:
    import readFile
    import langToLocal
    import setting
except ImportError:
    console.print("[bold red][ERROR][/bold red]: some internal modules are missing. Please try fix this or reinstall the application.For more information, please refer to the logs in the program directory.")
    logger.error("Internal modules missing", exc_info=True)
    sys.exit(1)

def load_config() -> dict:
    try:
        config = readFile.LoadJson("config.json")
    except FileNotFoundError:
        logger.warning("config.json not found or corrupted.")
        readFile.fix_config()
        config = readFile.LoadJson("config.json")
    if config["logLevel"] == "INFO":#set log level
        logger.setLevel(logging.INFO)
    elif config["logLevel"] == "WARNING":
        logger.setLevel(logging.WARNING)
    return config


def main():
    while True:
        command = console.input("[bold green]> [/bold green]")
        console.clear()
        if command.lower() in ["exit", "q"]:
            console.print("[bold yellow]Exiting...[/bold yellow]")
            break
        elif command.lower() == "clear":
            console.clear()
        elif command.lower() == "help":
            console.print("""[bold blue]Available commands:[/bold blue]
- help: Show this help message
- clear: Clear the console
- exit or q: Exit the application
- page or tp: Go to the designated page
- post: Create a new post
- settings: Open the settings menu
""")
        elif command.lower() == "settings":
            setting.start()
        else:
            console.print(f"[bold red][ERROR][/bold red]: Unknown command '{command}'")

if __name__ == "__main__":
    config = load_config()
    main()