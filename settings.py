import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

LYNX_WEB_URL = os.getenv("LYNX_WEB_URL")
