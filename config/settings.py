from os import getenv
from pathlib import Path
from dotenv import load_dotenv

# loads the configs from .env
load_dotenv()

BASE_URL = 'https://superheroapi.com/api/'
TOKEN = getenv('TOKEN')
ROOT = Path().resolve()
