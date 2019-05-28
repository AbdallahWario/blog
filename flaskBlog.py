
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '63f4fbbf9e929e637166f78c35ae87b1'
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from models import user,Post



posts = [
    {
        'author': 'Abdallah Wario',
        'Title':'FLASK',
        'content' : ' wtf forms',
        'Date_posted': 'Sep 6th, 2018',
    },
      {
        'author': 'Ali Wario',
        'Title':'MEDICINE',
        'content' : ' Bacterial infections', 
        'Date_posted': 'Sep ,8th 2018',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts = posts,title = 'abdallah')


@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'account created successfully for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template("register.html", title ='register', form = form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        if form.email.data == "admin@yahoo.com" and form.password.data == "dallas":
            flash('you are logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('unsuccessful login',success)
    return render_template("login.html", title ='login', form = form)



@app.route("/about")
def about():
   return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)