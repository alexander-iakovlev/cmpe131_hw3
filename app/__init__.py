from flask import Flask, render_template, escape

myobj = Flask(__name__)
myobj.config.from_mapping( SECRET_KEY = 'you-will-never-guess')

import app.routes