# Import flask and template operators
from flask import Flask, render_template,session

from flask_session import Session
import os

from flask import app as app

import tempfile
from werkzeug.utils import secure_filename



# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy, BaseQuery

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')





# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


app.secret_key = 'super-secret-key'

app.config['SESSION_SQLALCHEMY_TABLE'] = 'sessions_domitos'
app.config['SESSION_SQLALCHEMY'] = db

session = Session(app)
session.app.session_interface.db.create_all()



# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_test.controllers import mod_test as test_module
from app.mod_main.controllers import mod_main as main_module
from app.mod_modules.controllers import mod_modules as feature_module
from app.mod_industry.controllers import mod_industry as industry_module
from app.mod_blog.controllers import mod_blog as blog_module

# Register blueprint(s)
app.register_blueprint(test_module)
app.register_blueprint(main_module)
app.register_blueprint(feature_module)
app.register_blueprint(industry_module)
app.register_blueprint(blog_module)

db.create_all()

