import solar_network_sdk
from flask import render_template,Flask
import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) ## set work dir
app = Flask(__name__,template_folder="UI",static_folder="UI/static/")


def load_local_cfg() ->dict: ## load local config
    DEFAULT_CONFIG = {
        "token":"",
        "app_setting":{
            "language":"zh_cn",
            "theme":"dark",
            "font":"a local path",
            "message_style": "bubble",
            "attachments_list_style":"row",
            "color_theme":"seedcolor",
            "card_opacity":0.8,
            "bg_img":"a local path"
        },
        "server_setting":{
            "server_URL":"https://api.solian.app",
            "attachments_pool":"SolarNetworkShared",
            "proxy":"a url",
            "timeout":10,
            "verify_ssl":True
        },
        "app_action":{
            "Sound_effects":True,
            "send_use_enter":True,
            "opacity_status_bar":True,
            "data_saver_mode":False,
            "show_chat_event_message":"none",
            "homepage":"dashboard",
            "search_engine":"https://www.bing.com/search?q={}"
        }
    }
    try:
        with open("data/user_cfg.json","r") as f:
            data = json.load(f)
            return data
    except (FileNotFoundError,json.JSONDecodeError,OSError,PermissionError):
        return DEFAULT_CONFIG

@app.route("/")
def index() -> None:
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True,port=5000)