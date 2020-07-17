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

mod_modules = Blueprint('module', __name__, url_prefix='/module')


@mod_modules.route('/lead-management', methods=['GET', 'POST'])
def lead_mgmt():
    print("Got the hit")
    return render_template("modules/lead-management.html")


@mod_modules.route('/proposals', methods=['GET', 'POST'])
def proposals():
    print("Got the hit")
    return render_template("modules/proposals.html")


@mod_modules.route('/on-off-boarding', methods=['GET', 'POST'])
def onOffBoarding():
    print("Got the hit")
    return render_template("modules/on-off-boarding.html")

@mod_modules.route('/availability-management', methods=['GET', 'POST'])
def availibility():
    print("Got the hit")
    return render_template("modules/availability.html")


@mod_modules.route('/facility-overview', methods=['GET', 'POST'])
def facility():
    print("Got the hit")
    return render_template("modules/facility-overview.html")

@mod_modules.route('/erp-integrations', methods=['GET', 'POST'])
def erpIntegrations():
    print("Got the hit")
    return render_template("modules/erp-integrations.html")

@mod_modules.route('/accounting-module', methods=['GET', 'POST'])
def accounting():
    print("Got the hit")
    return render_template("modules/accounting-module.html")

@mod_modules.route('/client-management', methods=['GET', 'POST'])
def clientManagement():
    print("Got the hit")
    return render_template("modules/client_management.html")


@mod_modules.route('/unit-management', methods=['GET', 'POST'])
def unitManagement():
    print("Got the hit")
    return render_template("modules/unit-management.html")

@mod_modules.route('/tenant-management', methods=['GET', 'POST'])
def tenantManagement():
    print("Got the hit")
    return render_template("modules/tenant-management.html")

@mod_modules.route('/payment-management', methods=['GET', 'POST'])
def paymentManagement():
    print("Got the hit")
    return render_template("modules/payment-management.html")


@mod_modules.route('/issues-management', methods=['GET', 'POST'])
def issueManagement():
    print("Got the hit")
    return render_template("modules/issue-management.html")

@mod_modules.route('/field-service', methods=['GET', 'POST'])
def fieldServiceManagement():
    print("Got the hit")
    return render_template("modules/field-service.html")

@mod_modules.route('/inspection-audits', methods=['GET', 'POST'])
def inspectionAudits():
    print("Got the hit")
    return render_template("modules/inspections.html")

@mod_modules.route('/property-maintenance', methods=['GET', 'POST'])
def propertyMaintenance():
    print("Got the hit")
    return render_template("modules/property-maintenance.html")

@mod_modules.route('/assets-management', methods=['GET', 'POST'])
def assetsManagement():
    print("Got the hit")
    return render_template("modules/assets-management.html")

@mod_modules.route('/vendor-management', methods=['GET', 'POST'])
def vendorManagement():
    print("Got the hit")
    return render_template("modules/vendor-management.html")

@mod_modules.route('/inspections-management', methods=['GET', 'POST'])
def inspections():
    print("Got the hit")
    return render_template("modules/inspections.html")


@mod_modules.route('/reports', methods=['GET', 'POST'])
def reports():
    print("Got the hit")
    return render_template("modules/reports.html")

@mod_modules.route('/enterprise-search', methods=['GET', 'POST'])
def searchEnterprise():
    print("Got the hit")
    return render_template("modules/ent-search.html")