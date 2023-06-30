from flask import Flask, render_template
import requests
app = Flask(__name__)


app.config['STATIC_FOLDER'] = 'static'
app.config['IMAGES_FOLDER'] = 'images'

borealcoffee = f"{app.config['STATIC_FOLDER']}/{app.config['IMAGES_FOLDER']}/boreal-coffee-clone.jpeg"
dopefolio = f"{app.config['STATIC_FOLDER']}/{app.config['IMAGES_FOLDER']}/dopefolio.jpg"
wilsonport = f"{app.config['STATIC_FOLDER']}/{app.config['IMAGES_FOLDER']}/wilsonport.jpeg"
crowntemplate = f"{app.config['STATIC_FOLDER']}/{app.config['IMAGES_FOLDER']}/crowntemplate.jpg"

flutter = f"{app.config['STATIC_FOLDER']}/{app.config['IMAGES_FOLDER']}/flutter.png"
monitor = f"{app.config['STATIC_FOLDER']}/{app.config['IMAGES_FOLDER']}/monitor.png"
react = f"{app.config['STATIC_FOLDER']}/{app.config['IMAGES_FOLDER']}/react.png"