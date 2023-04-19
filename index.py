import datetime
import os
import pickle

import pandas as pd
from flask import Flask, render_template, request
from sklearn.preprocessing import minmax_scale
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return 'About'