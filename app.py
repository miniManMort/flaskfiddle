from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit/user", methods=["POST"])
def submit_user():
    form_data = dict(request.form)
    for key, value in form_data.items():
        print(f"Key={key},  value={value}")

    return json.dumps(form_data)

