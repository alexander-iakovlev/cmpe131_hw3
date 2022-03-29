from flask import Flask, render_template, escape

myapp_obj = Flask(__name__)
myapp_obj.config.from_mapping( SECRET_KEY = 'you-will-never-guess')

import app.routes