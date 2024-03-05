from flaskblog import app
# #import flask
# from flask import Flask,render_template,url_for,flash,redirect
# from forms import RegistrationForm , LoginForm 
# from flask_sqlalchemy import SQLAlchemy
# #from datetime import datetime
# app = Flask(__name__)
# app.config['SECRET_KEY'] = '929c215bf08efe96d97fce0eba848392'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)
# from models import User , Post 
# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(20), unique=True, nullable=False)
# #     email = db.Column(db.String(120), unique=True, nullable=False)
# #     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
# #     password = db.Column(db.String(60), nullable=False)
# #     posts = db.relationship('Post', backref='author', lazy=True)

# #     def __repr__(self):
# #         return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# # class Post(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     title = db.Column(db.String(100), nullable=False)
# #     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
# #     content = db.Column(db.Text, nullable=False)
# #     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# #     def __repr__(self):
# #         return f"Post('{self.title}', '{self.date_posted}')"
    
# posts =[
# {'author': 'Samer Alloush',
# 'title': 'Blog Post 1',
# 'content': 'First post content',

# 'date_posted': '03 June 2023'}
# ,
# {
# 'author': ' Mohamad Ali  ',
# 'title' : 'Blog Post 2',
# 'content': 'Second post content',

# 'date_posted': '25 May 2023'
# }

# ]

# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template('home_pg.html', posts=posts)
# @app.route("/login",methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'samer@gmail.com' and form.password.data =='123456':
#             flash('you have been logged in !!','success')
#             return redirect(url_for('home'))
#         else :
#             flash('unsuccessful login ! wrong email/password  ','danger')
#     return render_template('login_pg.html', title= 'login' , form = form)

#         #flash(f'welcome {form.username.data} , Account created successfully !','success')
# @app.route("/register",methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'welcome {form.username.data} , Account created successfully !','success')
#         return redirect(url_for('home'))
#     return render_template('register.html',title='register',form=form)
# @app.route("/about")
# def about():
#     return render_template('about_pg.html',title="aboutPg")
if __name__ =="__main__":
    app.run(debug=True)