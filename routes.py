import subprocess
from flask import Blueprint, render_template, request, jsonify, redirect, flash, url_for

routes = Blueprint(__name__, "routes")

@routes.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html", app="musicapp.py", result="Spotify")

## Redirecting to a page - not returning redirect(url_for("routes.home"))
@routes.route("/music-app/", methods=['GET', 'POST'])
def run_app():
    print('----------------------------------')
    output = subprocess.Popen('python3 musicapp.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output.wait()
    print(output)
    return 'it ran... maybe'

## JSON reading
@routes.route("/json/")
def get_json():
    return jsonify({'app': ['valence', 'tempo', 'loudness', 'timbre']})

@routes.route("/auth/", methods=['GET', 'POST'])
def get_auth():
    error=None
    data = request.form
    if request.method == 'POST':
        email = request.form.get('email')
        if len(email) < 5:
            flash('Must be a valid email address!', 'error')
            error='Invalid email'
        else:
            flash('Loading your results!', 'success') 
            print('success')  
    print(data)
    return render_template("auth.html", error=error)

## Getting Data
# @routes.route("/data/")
# def get_data():
#     data = request.json
#     return jsonify(data)
