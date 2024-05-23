from flask import flash, redirect, url_for
from flask_babel import gettext
from flask_login import current_user
from functools import wraps

def check_is_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_confirmed is False:
            flash(gettext("Please confirm your account!"), "warning")
            return redirect(url_for("accounts.inactive"))
        return func(*args, **kwargs)

    return decorated_function

def check_is_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_admin is False:
            return redirect(url_for("search.index"))
        return func(*args, **kwargs)

    return decorated_function
