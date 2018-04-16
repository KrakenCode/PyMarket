from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user


bp = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static')


@bp.route('/dashboard')
def dashboard():
    if not current_user.is_authenticated:
        return redirect(url_for('login.login'))

    return render_template('dashboard.html', title='Dashboard')
