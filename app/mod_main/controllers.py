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

mod_main = Blueprint('main', __name__, url_prefix='/')


@mod_main.route('/', methods=['GET', 'POST'])
def landing():
    print("Got the hit")
    return render_template("mod_main/home.html")


@mod_main.route('/covid-solution', methods=['GET', 'POST'])
def covid():
    print("Got the hit")
    return render_template("mod_main/covid.html")

@mod_main.route('/module-test', methods=['GET', 'POST'])
def mod_test():
    print("Got the hit")
    return render_template("mod_main/module.html")


@mod_main.route('/blog-list', methods=['GET', 'POST'])
def blog_list():
    print("Got the hit")
    return render_template("mod_main/blog-list.html")

@mod_main.route('/blog-detail', methods=['GET', 'POST'])
def blog_detail():
    print("Got the hit")
    return render_template("mod_main/blog-detail.html")

@mod_main.route('/training', methods=['GET', 'POST'])
def training():
    print("Got the hit")
    return render_template("mod_main/training.html")


@mod_main.route('/marketing-consulting', methods=['GET', 'POST'])
def marketing():
    print("Got the hit")
    return render_template("mod_main/marketing-consulting.html")

@mod_main.route('/vendor-training', methods=['GET', 'POST'])
def vendoring():
    print("Got the hit")
    return render_template("mod_main/vendor-training.html")

@mod_main.route('/support-services', methods=['GET', 'POST'])
def supportServices():
    print("Got the hit")
    return render_template("mod_main/support-services.html")

@mod_main.route('/consulting-services', methods=['GET', 'POST'])
def consultingServices():
    print("Got the hit")
    return render_template("mod_main/consulting-services.html")