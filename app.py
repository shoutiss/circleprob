from flask import Flask, redirect, render_template, request, url_for

import os
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plot")
def plot():
    num_chords = request.args.get("num_chords", "")
    return render_template("plot.html", num_chords = num_chords, chart = app.send_static_file("test.png"))