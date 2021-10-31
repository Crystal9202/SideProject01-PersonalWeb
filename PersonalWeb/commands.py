import click

from flask import cli
from PersonalWeb import app ,db 
from PersonalWeb.models import Message ,Story ,User


@app.cli.command()
@click.option('--drop', is_flag = True ,help = 'Create after drop.' ) # 將 is_flag 參數設為 True 可以將這個選項聲明為布爾值標誌
def initdb(drop):
    """Initialize the database"""
    if drop :
        db.drop_all()
    db.create_all()
    click.echo('Initialize database.')


@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    name = "Crystal"
    messages = [       
        {'name': '墊底辣妹', 'body': '如果你因心願沒有實現, 而正在心灰意冷, 為宏大目標而拼搏過的這段經歷，將來一定會成為你的力量｡'},
        {'name': '工作一姊', 'body': '工作是否值得驕傲, 並非靠他人的標準來衡量, 而是由自己來決定！'},
        {'name': '小海女', 'body': '人生的路很漫長, 即使迷路也沒關係, 繞遠路也沒關係｡ 人多的時候就走小路, 在哪裡遇到什麼人都不一定, 最後抵達的地方就是目的地｡'},
        {'name': '東大特訓班', 'body': '入學考試的問題, 正確答案往往只有一個, 如果沒有找到就會落榜…人生卻不一樣, 有很多正確答案｡ 不要畏懼活下去! 不要否定自己的可能性!'}   
    ] 

    user = User(name = name)
    db.session.add(user)
    for m in messages:
        message = Message(name = m['name'] , body = m['body'])
        db.session.add(message)


    stories = [
        {'title': '個人網站', 'body': '個人獨立小型專案, 支持留言板與登入系統, 進行中｡', 'site': 'https://github.com/Crystal9202/SideProject01-PersonalWeb'},
        {'title': '資料分析', 'body': '個人獨立小型專案, 支持前台後台登入系統, 準備中｡', 'site': 'https://github.com/Crystal9202/SideProject02-DataAnalysis'},
        {'title': 'LeetCode刷題記錄', 'body': '使用 Python 與 MySQL 的刷題記錄, 持續中｡', 'site': 'https://github.com/Crystal9202/LeetCode'},
        {'title': 'Datamining', 'body': '使用 pandas 與 NumPy 等套件進行資料分析, 持續中｡', 'site':'https://github.com/Crystal9202/pandas'}
    ]

    for s in stories:
        stories = Story(title=s['title'],body=s['body'],site=s.get('site','/story'))
        db.session.add(stories)
    click.echo('Done')


@app.cli.command()
@click.option('--username' ,prompt = True , help=" The username used to login")
@click.option('--password' ,prompt = True ,hide_input = True , confirmation_prompt = True , help ='The password used to login' )
def admin(username , password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo("Updating user...")
        user.username = username
        user.set_password(password)
    else:
        click.echo("Creating user...")
        user = User(username = username , name ='Admin')
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('Done')