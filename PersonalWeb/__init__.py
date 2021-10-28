from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf.csrf import CSRFProtect

app = Flask('PersonalWeb')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True 


db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
csrf=CSRFProtect(app)
moment=Moment(app)






from PersonalWeb import views ,models,forms,errors,commands