from  flask import Flask
from app import app
from pymongo import MongoClient
from user.models import User


@app.route('/user/signup', methods=["GET","POST"])
def signup():
    if request.method == "POST":
         username = request.form.get("username")
         email = request.form.get("email")         
         password = request.form.get("password")
         return f"Name: {name}, Email: {email}, Password:{password}"
        # Insert user data into MongoDB
         user_data = {"username": username, "email": email, "password": password}
         collection.insert_one(user_data)
         return "Signup successful!"
    else:
        return render_template("login.html") 
   # return User().signup()
