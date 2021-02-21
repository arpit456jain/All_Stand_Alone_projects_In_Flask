from flask import Flask,render_template,request,flash,session,redirect
import smtplib #for email

app = Flask(__name__)
app.secret_key = "super-secret-key"
@app.route('/')
def hello_world():
    # return 'Hello, World!
    return redirect("/projects/calc")

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
        flash("We have recieved your Message thank you for Contacting us!!",'success')
        print(name,email,feedback,number)
        
        con = connectTOMail()
        # con.sendmail("arpit456jain@gmail.com",email,"Subject:Feed Back of Calculator app \n\n"+"Thank You for the feed back")
        con.sendmail("arpit456jain@gmail.com","111arpit1@gmail.com","Subject:Calculator \n\n" + str(feedback))
        return redirect('/')
    return render_template('contact.html')

@app.route('/projects/calc')
def projects():
    flash('Welcome Hop you like this calculator app', 'success')
    return render_template('calculator.html')

@app.route('/projects/calculate',methods=["GET","POST"])
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
