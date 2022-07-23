import environ
import os
from pathlib import Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR1 = Path(__file__).resolve().parent.parent
from django.core.management.utils import get_random_secret_key
import django
env = environ.Env()
env.read_env(BASE_DIR1 / '.env')

print(env('DEBUG'))
print(get_random_secret_key())
print(env('SECRET_KEY'))
print(env('DB_ENGINE'))
print(f'django.db.backends.{env("DB_ENGINE", "sqlite3")}')
print(env('DB_NAME'))
print(env('DB_USER'))
print(env('DB_PASSWORD'))