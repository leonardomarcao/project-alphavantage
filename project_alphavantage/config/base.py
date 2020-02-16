from settings import *
from os.path import join

API_ALPHA_VANTAGE_URL = env('api_alpha_vantage_url')
DATABASE_PATH = join(BASE_DIR, env('database_name'))