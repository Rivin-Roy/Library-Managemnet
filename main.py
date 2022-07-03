from flask import Flask
from public import public
from admin import admin
from staff import staff
from user import user


import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail



app=Flask(__name__)

app.secret_key="abc"

app.register_blueprint(public)

app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(staff,url_prefix='/staff')
app.register_blueprint(user,url_prefix='/user')



mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'projectsriss2020@gmail.com'
app.config['MAIL_PASSWORD'] = 'messageforall'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True




app.run(debug=True,port=5897)
 