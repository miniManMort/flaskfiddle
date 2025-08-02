from flask import Flask, request, render_template
import json
from app_modules import user_pages, user_objects

# Create the DB tables
print("Creating DB Tables")
user_objects.create_user_tables()



print("Starting App")
# Create the App
app = Flask(__name__)

app.register_blueprint(user_pages.users_bp, url_prefix="/users")

@app.route("/")
def index():
    return render_template("index.jinja")

@app.route("/submit/user", methods=["POST"])
def submit_user():
    form_data = dict(request.form)
    for key, value in form_data.items():
        print(f"Key={key},  value={value}")

    return json.dumps(form_data)

