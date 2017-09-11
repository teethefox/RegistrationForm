from flask import Flask, render_template, request, redirect, flash
import re
app = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key="Secrettttttt"
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def process(): 
    str1=request.form['firstname']
    str2=request.form['lastname']
    if len(request.form['firstname']) < 1:
        flash("Error : All fields are required.")
    elif str1.isalpha() == False:
            flash("Error: First Name must not contain any numbers.")
    elif len(request.form['lastname']) < 1:
        flash("Error : All fields are required. ")
    elif str2.isalpha() == False:
        flash("Error: Last Name must not contain any numbers.")
    elif len(request.form['email']) <0:
        flash("Error: All fields are required.")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Error: Please enter a valid Email Address.")
    elif len(request.form["password"])<8:
        flash("Error: Password must be longer than 8 characters!")
    elif request.form["password"] != request.form["confirmpassword"]:
        flash("Error: Passwords do not match.")
    
    #     return render_template("process.html",name = request.form["name"], location = request.form["location"], language = request.form["language"], comment = request.form["comment"])
    else:
        flash("Registration successful!")
    return redirect("/")
app.run(debug=True)