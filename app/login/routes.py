from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user

from . import login_bp
from .forms import LoginForm


@login_bp.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'post':
        if form.validate_on_submit():
            user = form.username.data
            password = form.password.data

            return redirect(url_for('public.index'))
    return render_template("login/login.html", form=form)
