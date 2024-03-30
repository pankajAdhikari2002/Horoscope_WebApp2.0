from flask import Flask, render_template, request, url_for, redirect
import script
import json
import datetime

app = Flask(__name__)

today_data = None

def find_sign(dob):
    x = datetime.datetime.strptime(dob, '%Y-%m-%d')
    date_f = x.strftime('%d %B %Y').split(" ")
    day = int(date_f[0])
    month = date_f[1].lower()
    if month == 'december':  
        sun_sign = 'Sagittarius' if (day < 22) else 'Capricorn'  
    elif month == 'january':  
        sun_sign = 'Capricorn' if (day < 20) else 'Aquarius'  
    elif month == 'february':  
        sun_sign = 'Aquarius' if (day < 19) else 'Pisces'  
    elif month == 'march':  
        sun_sign = 'Pisces' if (day < 21) else 'Aries'  
    elif month == 'april':  
        sun_sign = 'Aries' if (day < 20) else 'Taurus'  
    elif month == 'may':  
        sun_sign = 'Taurus' if (day < 21) else 'Gemini'  
    elif month == 'june':  
        sun_sign = 'Gemini' if (day < 21) else 'Cancer'  
    elif month == 'july':  
        sun_sign = 'Cancer' if (day < 23) else 'Leo'  
    elif month == 'august':  
        sun_sign = 'Leo' if (day < 23) else 'Virgo'  
    elif month == 'september':  
        sun_sign = 'Virgo' if (day < 23) else 'Libra'  
    elif month == 'october':  
        sun_sign = 'Libra' if (day < 23) else 'Scorpio'  
    elif month == 'november':  
        sun_sign = 'Scorpio' if (day < 22) else 'Sagittarius'  
    return sun_sign.lower()

@app.route('/', methods=["GET", "POST"])
def home():
    user_name = None
    user_dob = None
    user_symbol = None
    if request.method == 'POST':
        user_name = request.form['name']
        user_dob = request.form['dob']
        print(user_dob)
        astro_sign = find_sign(user_dob)
        return redirect(url_for("info", astro_sign=astro_sign, name=user_name.split(" ")[0]))
    
    return render_template("homepage.html")

@app.route("/info/<astro_sign>/<name>")
def info(astro_sign, name):
    data = today_data[astro_sign.title()]
    return render_template("infopage.html", astro_sign=astro_sign, data=data, name=name)

@app.route("/runScript{UNIQUE}") # Add yours in place of UNIQUE
def runScript():
    global today_data
    script.runScript()
    try:
        with open("horoscope.json", "r", encoding="utf-8") as outfile:
            today_data = json.load(outfile)
        return {"Message": "Script Ran Successfully"}
    except Exception as e:
        return {"Error": "Error Occured"}
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', err=e), 404


if __name__ == '__main__':
    app.run(debug=True)
