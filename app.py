from flask import Flask, jsonify,request,render_template,session
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"]='mongodb://localhost:27017/Management_App'
mongo=PyMongo(app)
# Initialize the MongoDB client and connect to a database
@app.route('/')
def index():
    return render_template('signin.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/tasks')
def details():
    return render_template('tasks.html')
@app.route('/dashboard')
def show():
    return render_template("dashboard.html")
@app.route('/signupfield',methods=["GET"])
def home():
    return render_template('signup.html')

@app.route("/validate" , methods=['POST'])
def validate():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    data=mongo.db.Login.find_one({"Email":email})
    stored_password=data.get('Password')
    if(stored_password == password):
        return render_template("dashboard.html",status="unmatch")
    else:
        return render_template("signin.html",status="short")


@app.route('/details', methods=['POST'])
def details():
    name=request.form.get("projectName")
    start_date = request.form.get("startDate")
    deadlineDate = request.form.get("deadlineDate")
    members = request.form.get("members")
    mentors = request.form.get("mentors")
    techStack= request.form.get("techStack")
    github = request.form.get("github")
    problemStatement = request.form.get("problemStatement")
    mongo.db.Projects.insert_one({
       "Project_Name":name,
       "Start_Date":start_date,
       "Deadline":deadlineDate,
       "Members":members,
 "Mentors":mentors,
"Tech_Stack":techStack,
"Github":github,
"Problem_statement":problemStatement,
    })

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get("name")
    email = request.form.get("email")
    create_pass = request.form.get("create_password")
    confirm_pass = request.form.get("confirm_password")
    if (len(create_pass)<4):
         return "PassWord Must be Greater than 4 Character"
    if create_pass == confirm_pass:
         mongo.db.Login.insert_one({"Name":name,'Email':email,"Password":create_pass,"Confirm_Password":confirm_pass})
        #  data=mongo.db.Login.find_one({})

         return render_template('dashboard.html')
    else:
       return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug=True)

