from dotenv import load_dotenv
import os

from app.config.config_utils import *


load_dotenv(dotenv_path="app/env/config.env")


SHOW_NOTIFICATION=str_to_bool((os.getenv("NOTIFICATION")))


ENV_DIRECTORY=fr"app\env"
# ENV_DIRECTORY=fr"{os.getcwd()}\app\env"