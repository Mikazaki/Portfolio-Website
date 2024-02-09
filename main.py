from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import smtplib
import os

app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')



@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        user = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form['message']
        
        sendemail(user, email, phone, message)
        return render_template("contact.html", sent = True)
    return render_template("contact.html", sent = False)

def sendemail(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.environ.get("EMAIL_SEND"), password=os.environ.get("EMAIL_PASSWORD"))
            connection.sendmail(
                from_addr=os.environ.get("EMAIL_SEND"),
                to_addrs='messikazi2121@gmail.com',
                msg=f"Subject: New Message \n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            )



if __name__ == "__main__":
    app.run(debug=True)
