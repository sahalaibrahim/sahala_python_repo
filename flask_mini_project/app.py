from flask import Flask,render_template,request, redirect, url_for
import requests

import Constant
app=Flask(__name__)
@app.route("/")
def rtPage():
    return "This is Weather App"
@app.route("/weather",methods=['GET','POST'])
def WeatherInputPage():
    data2=""
    if request.method=='POST' and 'lattitude'in request.form:
        lat=float(request.form.get('lattitude'))
        lon=float(request.form.get('longitude'))
        url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Constant.api_key}'
        response = requests.get(url)
        data = response.json()
        temperatureData=f"{data['main']['temp']}"
        return redirect(url_for('successPage', temperature=temperatureData))
        
    return render_template("index.html")

@app.route("/success/<temperature>",methods=['GET','POST'])
def successPage(temperature):
     return render_template("success.html", temperature = temperature)


app.run(debug=True)