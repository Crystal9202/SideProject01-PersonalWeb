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

@app.route('/message/delete/<int:message_id>',methods=['POST'] )
def delete_message(message_id):
    message = Message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    flash('留言已經刪除')
    return redirect(url_for('message'))


@app.route('/story',methods=["GET","POST"])
def story():
    stories=Story.query.all()
    form=PostForm()
    if form.validate_on_submit():
        title=form.title.data
        body=form.body.data
        site=form.site.data
        story=Story(title=title , body=body ,site=site)
        db.session.add(story)
        db.session.commit()
        flash('新增最新動態')
        return redirect(url_for('story'))
    return render_template('story.html' ,stories=stories , form=form)


@app.route('/story/delete/<int:story_id>' , methods=['POST'])
def delete_story(story_id):
    story = Story.query.get_or_404(story_id)
    db.session.delete(story)
    db.session.commit()
    flash('動態已刪除')
    return redirect(url_for('story'))


@app.route('/login')
def login():
    return render_template('login.html')