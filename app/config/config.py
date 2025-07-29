from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="app/env/config.env")

NOTIFICATION_FLAG=os.getenv("NOTIFICATION")



ENV_DIRECTORY=fr"{os.getcwd()}\app\env"

