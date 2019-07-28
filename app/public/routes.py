from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user

from app.models import User
from . import public_bp


@public_bp.route("/public/", methods=['GET', 'POST'])
def login():
    pass
