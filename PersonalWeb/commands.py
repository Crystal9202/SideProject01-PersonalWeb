import click
from PersonalWeb import app ,db 
from PersonalWeb.models import Message




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

    messages = [
        
        {'name': '墊底辣妹', 'body': '如果你因心願沒有實現, 而正在心灰意冷, 為宏大目標而拼搏過的這段經歷，將來一定會成為你的力量｡'},
        {'name': '工作一姊', 'body': '工作是否值得驕傲, 並非靠他人的標準來衡量, 而是由自己來決定！'},
        {'name': '小海女', 'body': '人生的路很漫長, 即使迷路也沒關係, 繞遠路也沒關係｡ 人多的時候就走小路, 在哪裡遇到什麼人都不一定, 最後抵達的地方就是目的地｡'},
        {'name': '東大特訓班', 'body': '入學考試的問題, 正確答案往往只有一個, 如果沒有找到就會落榜…人生卻不一樣, 有很多正確答案｡ 不要畏懼活下去! 不要否定自己的可能性!'}   
    ] 

    for m in messages:
        message = Message(name = m['name'] , body = m['body'])
        db.session.add(message)
    db.session.commit()
    click.echo('Done')