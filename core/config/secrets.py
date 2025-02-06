import os
from dotenv import load_dotenv

load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS")

DB_ENGINE = os.getenv("DB_ENGINE")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

RESEND_API_KEY = os.getenv("RESEND_API_KEY")

SENTRY_DSN = os.getenv("SENTRY_DSN")