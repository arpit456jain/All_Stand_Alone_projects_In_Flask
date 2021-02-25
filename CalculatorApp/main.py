from flask import Flask,flash,render_template,request,flash,session,redirect
from flask_sqlalchemy import SQLAlchemy
import smtplib #for email
from datetime import datetime
import json
import smtplib
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:@localhost/codesmashersblog"
app.secret_key = "super-secret-key"
db = SQLAlchemy(app)
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    mes = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)



@app.route('/')
def index():
    flash('Welcome Hop you like this calculator app', 'success')
    return render_template('calculator.html')

@app.route('/about')
def about():
    return render_template('about.html')

def connectTOMail():
    con = smtplib.SMTP("smtp.gmail.com",587)
    con.ehlo()
    print("hello sucessfull")
    con.starttls()
    con.login("arpit456jain@gmail.com","#vanshika jain#")
    print("login succesfull")
    return con

@app.route('/contact',methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        feedback = request.form.get('feedback')
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('pnumber')
        
        print(name,email,feedback,number)
        entry = Contacts(name=name, phone_num = number, mes = feedback,email = email )
        db.session.add(entry)
        db.session.commit()
        flash("We have recieved your Message thank you for Contacting us!!",'success')
        # con = connectTOMail()
        # con.sendmail("arpit456jain@gmail.com",email,"Subject:Feed Back of Calculator app \n\n"+"Thank You for the feed back")
        # con.sendmail("arpit456jain@gmail.com","111arpit1@gmail.com","Subject:Calculator \n\n" + str(feedback))
        return redirect('/')
    return render_template('contact.html')

@app.route('/calculate',methods=["GET","POST"])
def calculate():
    
    if request.method == 'POST':
        print("post method")
        equation = request.form.get('equation')
        # x = request.form.get('var')
        print(equation)
        # Exception Handling
        try:
            ans = eval(equation)
            print(ans)
            # params = {'ans':ans,'error':False,'eq':equation}
            msg = "Great! Your Equation has been analysed : "+ equation + " = "+ str(ans)
            flash(msg, 'success')
        except:
            flash('There is some error in the equation you entered', 'danger')
    # return HttpResponse('ans')
    return render_template('calculator.html')


if __name__ == '__main__':
    app.run(debug=True)
