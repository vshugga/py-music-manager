import os
from dotenv import load_dotenv
from flask import Flask
import config, config_debug
from .models import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    conf_obj = config
    load_dotenv()
    if os.getenv('FLASK_DEBUG'):
        print('\033[91mDEVELOPMENT MODE SET\033[0m')
        conf_obj = config_debug
    else:
        print('\033[91mPRODUCTION MODE SET\033[0m')
    
    app.config.from_object(conf_obj)

    from .routes import main
    app.register_blueprint(main)


    db.init_app(app)
    migrate = Migrate(app, db)

    return app

#TEST MODIFICATION