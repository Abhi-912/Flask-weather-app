from types import MethodDescriptorType
from flask import Flask, request, render_template, redirect, url_for, session
from flask.json import jsonify
import requests
from datetime import timedelta
import json

app = Flask(__name__)


var_list = {}

@app.route("/", methods = ["POST", "GET"])
def get_form_data():
    return render_template("index.html")
    
    
@app.route("/weather", methods = ["POST", "GET"])
def get_weather():
        default_name = '0'
        data = request.form.get('nm', default_name)
        url = f'http://api.openweathermap.org/data/2.5/weather?q={data}&appid=57f9f0517d659affae89b22c83a884e1&units=metric'
        datas = requests.get(url).json()
        main_temp = datas['main']
        return render_template('weather.html', data = data, cel = str(main_temp['temp']))
       

if __name__ == "__main__":
    app.run(debug = True, port = 3000)