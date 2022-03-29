from flask import Flask
from flask import escape

myobj = Flask(__name__)

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myobj.route("/")
def home():
    return "<h1>Welcome " + name + "!</h1> <p><ahref=\"www.google.com\">notgoogle</a></p> <ul> <li>"+city_names[0]+"</li><li>"+city_names[1]+"</li><li>"+city_names[2]+"</li><li>"+city_names[3]+"</li> </ul>"
#myapp_obj.run()