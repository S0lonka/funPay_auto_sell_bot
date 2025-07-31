from dotenv import load_dotenv
import os
from app.utils.config_utils import str_to_bool

load_dotenv(dotenv_path="app/env/logger_config.env")

TEST = str_to_bool(os.getenv("TEST"))