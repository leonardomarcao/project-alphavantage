from os.path import join, dirname, abspath
from os import getenv
from pathlib import Path
from environs import Env

BASE_DIR = str(Path(dirname(abspath(__file__))).parent.parent)
CONFIG_DIR = str(Path(dirname(abspath(__file__))))
# set env 
env = Env()
env.read_env(BASE_DIR)