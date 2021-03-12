# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:04:02 2021

@author: Harish_8055
"""

from flask import *  
from flask_mail import *  
from random import *  
app = Flask(__name__)  
mail = Mail(app)  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465      
app.config["MAIL_USERNAME"] = 'example@gmail.com'  
app.config['MAIL_PASSWORD'] = 'example007'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
mail = Mail(app)  
otp = randint(000000,999999)   
@app.route('/')  
def index():  
    return render_template("index.html")  
@app.route('/verify',methods = ["POST"])  
def verify():  
    email = request.form["email"]   
    msg = Message('Interact',sender = 'techspeaks@gmail.com', recipients = [email])  
    msg.body = 'One time password ->'+str(otp)  
    mail.send(msg)  
    return render_template('verify.html')  
@app.route('/validate',methods=["POST"])   
def validate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        return "<h3> Email  on is  successful </h3>"  
    return "<h3>failure, OTP does not match</h3>"   
if __name__ == '__main__':  
    app.run() 
