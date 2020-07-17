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

mod_industry = Blueprint('industry', __name__, url_prefix='/industry')

@mod_industry.route('/government', methods=['GET', 'POST'])
def government():
    print("Got the hit")
    return render_template("mod_industry/government.html")


@mod_industry.route('/retail', methods=['GET', 'POST'])
def retail():
    print("Got the hit")
    return render_template("mod_industry/retail.html")

@mod_industry.route('/luxury-retail', methods=['GET', 'POST'])
def luxury_retail():
    print("Got the hit")
    return render_template("mod_industry/luxury-retail.html")

@mod_industry.route('/restaurants', methods=['GET', 'POST'])
def restaurants():
    print("Got the hit")
    return render_template("mod_industry/restaurants.html")

# grocery/supermarkets, other industries
@mod_industry.route('/convenience-store', methods=['GET', 'POST'])
def constores():
    print("Got the hit")
    return render_template("mod_industry/convenience-store.html")

@mod_industry.route('/retail-healthcare', methods=['GET', 'POST'])
def retailHealthcare():
    print("Got the hit")
    return render_template("mod_industry/retail-healthcare.html")

@mod_industry.route('/financial', methods=['GET', 'POST'])
def financial():
    print("Got the hit")
    return render_template("mod_industry/financial.html")

@mod_industry.route('/spas-fitness', methods=['GET', 'POST'])
def spaFitness():
    print("Got the hit")
    return render_template("mod_industry/spas-fitness.html")

@mod_industry.route('/self-storage', methods=['GET', 'POST'])
def selfStorage():
    print("Got the hit")
    return render_template("mod_industry/self-storage.html")

@mod_industry.route('/grocery-supermarkets', methods=['GET', 'POST'])
def grocerySupermarkets():
    print("Got the hit")
    return render_template("mod_industry/grocery-supermarkets.html")

@mod_industry.route('/other-industries', methods=['GET', 'POST'])
def otherIndustries():
    print("Got the hit")
    return render_template("mod_industry/other-industries.html")
