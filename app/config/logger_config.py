from dotenv import load_dotenv
import os
from app.utils.config_utils import str_to_bool

load_dotenv(dotenv_path="app/env/logger_config.env")

MAIN = str_to_bool(os.getenv("MAIN"))
NOTIFICATION = str_to_bool(os.getenv("NOTIFICATION"))
FILE_UTILS = str_to_bool(os.getenv("FILE_UTILS"))
# MAIN = str_to_bool(os.getenv("MAIN"))
