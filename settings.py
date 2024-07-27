import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

WEB_URL = os.getenv("INPUT_WEB_URL")
