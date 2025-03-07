from flask import Flask, render_template, redirect, url_for, request
import time
import json
import os


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        if "login" in request.form:
            user = request.form.get("user")
            password = request.form.get("password")

            if user == "julian" and password == "notes":
                return redirect(url_for("notes", user=user))

    return render_template("login.html")


@app.route("/<user>/notes", methods=["POST", "GET"])
def notes(user):
    return render_template("notes.html")


if __name__ == "__main__":
    app.run(debug=True)