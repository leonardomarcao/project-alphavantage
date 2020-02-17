from .settings import *
from os.path import join

ALPHA_VANTAGE_API_URL = env('alpha_vantage_api_url')
DATABASE_PATH = join(BASE_DIR, env('database_name'))
ALPHA_VANTAGE_API_KEY = env('alpha_vantage_api_key')
