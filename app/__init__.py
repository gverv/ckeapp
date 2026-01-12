# app/__init__.py

from flask import Flask
from .config import Config
from .extensions import db, migrate, login_manager, ckeditor, csrf
from .middleware import maintenance_middleware

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    csrf.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.before_request
    def before_request():
        result = maintenance_middleware()
        if result:
            return result

    # Blueprints
    from .main import main_bp
    from .auth import auth_bp
    from .admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app

