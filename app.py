# from crypt import methods
import imp
from re import X
from unicodedata import name
from urllib import request
from flask import Flask, render_template, request, session , redirect, url_for
from flask_sqlalchemy import SQLAlchemy

class User:
    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f'<User: {self.username} {self.password}>'

users = []
users.append(User(id=1,username='siddharth', password='password'))
users.append(User(id=2,username='Becca',password='secret'))

print(users[1].id)

print(users)

app = Flask(__name__)
app.secret_key = 'siddharth'
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///stud.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Stud(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(260), nullable=False)
    mob = db.Column(db.String(260), nullable=False)
    mail = db.Column(db.String(260), nullable=False)
    dob = db.Column(db.String(260), nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"{self.sno} {self.name} {self.mob} {self.dob} {self.age}"

@app.route("/")
def stud():    
    return render_template('index.html')

@app.route("/logout")
def logout():    
    session.pop('user_id',None)
    return redirect(url_for('stud'))
    # return render_template('index.html')

@app.route("/login",methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id',None)

        username = request.form['username']
        password = request.form['password']


        user = [x for x in users if x.username == username][ 0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('demo'))
            # return ('Hello World')
            # return render_template('index.html')


        return redirect(url_for('login'))
        
    return render_template('login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        name = request.form['name']
        mob = request.form['mob']
        mail = request.form['mail']
        dob = request.form['dob']
        age = request.form['age']    
        stud = Stud(name=name, mob=mob, mail=mail, dob=dob, age=age)
        db.session.add(stud)
        db.session.commit()  
        return redirect(url_for('stud'))
    return render_template('register.html')

@app.route("/demo")
def demo():
    allstud = Stud.query.all()
    print(allstud)
    return render_template('demo.html', allstud=allstud)

if __name__ == "__main__":
    app.run(debug=False)