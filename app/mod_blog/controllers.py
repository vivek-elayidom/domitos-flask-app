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

mod_blog = Blueprint('blog', __name__, url_prefix='/blog')



#Building Maintenance
@mod_blog.route('/building-maintenance', methods=['GET', 'POST'])
def blog1():
    print("Got the hit")
    return render_template("mod_blog/building-maintenance.html")

#Facility management Companies
@mod_blog.route('/facility-management-companies', methods=['GET', 'POST'])
def blog2():
    print("Got the hit")
    return render_template("mod_blog/facility-management-comps.html")

@mod_blog.route('/inventory-management-software', methods=['GET', 'POST'])
def blog3():
    print("Got the hit")
    return render_template("mod_blog/inventory-management-soft.html")

@mod_blog.route('/iot-in-buildings', methods=['GET', 'POST'])
def blog4():
    print("Got the hit")
    return render_template("mod_blog/iot-in-buildings.html")

@mod_blog.route('/operations-maintenance-manual', methods=['GET', 'POST'])
def blog5():
    print("Got the hit")
    return render_template("mod_blog/ops-manual.html")

@mod_blog.route('/scheduled-maintenance', methods=['GET', 'POST'])
def blog6():
    print("Got the hit")
    return render_template("mod_blog/schedule-maintenance.html")

@mod_blog.route('/warehouse-logistics', methods=['GET', 'POST'])
def blog7():
    print("Got the hit")
    return render_template("mod_blog/warehouse-logistics.html")


@mod_blog.route('/work-order-software', methods=['GET', 'POST'])
def blog8():
    print("Got the hit")
    return render_template("mod_blog/work-order-software.html")

    