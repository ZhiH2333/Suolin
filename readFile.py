import json
import rich.console
import shutil

def LoadJson(filePath: str) -> dict:
    try:
        console = rich.console.Console()
        with open(filePath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        console.print(f"[bold red][ERROR][/bold red]: File not found - {filePath}")
        return {}
    except json.JSONDecodeError:
        console.print(f"[bold red][ERROR][/bold red]: JSON decode error - {filePath}")
        return {}

def fix_config():
    config = {
    "lang": "en",
    "APIdomain": "https://api.solian.app",
    "autoFreshPage":False,
    "logLevel":"DEBUG",
    "EncryptedUserToken":False
}
    shutil.copyfile("config.json","config.json.old")
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)