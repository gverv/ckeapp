# app/config.py
import os
from dotenv import load_dotenv
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '..', '.env'))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
        f"@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DB')}"
    )

    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")
    # SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    CKEDITOR_PKG_TYPE = "standard"
    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = "main.upload_image"
    UPLOAD_FOLDER = "instance/uploads"
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
