#
# Pages and UI components for User details
#

from flask import Blueprint, render_template

users_bp = Blueprint("user_pages", __name__)

@users_bp.route("/")
def users_top():
    try:
        return render_template("users/index.jinja")
    except:
        return render_template("error.jinja", error_message="Error rendering users index page")

