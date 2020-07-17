from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify

# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

# Import the database object from the main app module
from app import db
from app import app
import time 
from datetime import datetime
import os

mod_test = Blueprint('test', __name__, url_prefix='/test')


@mod_test.route('/sample', methods=['GET', 'POST'])
def landing():
    print("Got the hit")
    return render_template("mod_test/sample.html")