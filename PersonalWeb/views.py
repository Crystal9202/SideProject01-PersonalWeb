from flask.helpers import url_for
from werkzeug.utils import redirect
from  PersonalWeb import app ,db
from flask import render_template ,flash,redirect
from PersonalWeb.forms import HelloForm ,PostForm
from PersonalWeb.models import Message ,Story
from werkzeug.utils import redirect
from flask_wtf import form


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/message',methods = ["GET","POST"])
def message():
    form = HelloForm()
    if form.validate_on_submit():
       name = form.name.data
       body = form.body.data 
       message = Message(name=name , body=body)
       db.session.add(message)
       db.session.commit()
       flash('留言成功, 謝謝您提供的寶貴意見與經驗分享｡')
       return redirect(url_for("message"))
    

    messages=Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('message.html' , form = form ,messages=messages)



@app.route('/story',methods=["GET","POST"])
def story():
    stories=Story.query.all()
    form=PostForm()
    if form.validate_on_submit():
    return render_template('story.html' ,stories=stories , form=form)


@app.route('/login')
def login():
    return render_template('login.html')