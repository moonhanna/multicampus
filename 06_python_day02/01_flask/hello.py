from flask import Flask, render_template, request
import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('index.html')

@app.route('/t4ir')
def t4ir():
    return 'this is t4ir'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end = datetime.datetime(2020, 4, 21)
    td = end - today
    return f'{td.days}일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>this is html h1 tag</h1>'

@app.route('/html_line')
def html_line():
    return """
    <h1>여러 줄을 보내봅시다.</h1>
    <ul>
        <li>1줄</li>
        <li>2줄</li>
    </ul>
    """

@app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다! {name}님'
    return render_template('greeting.html',html_name=name)

@app.route('/cube/<int:number>')
def cube(number):
    # return f'{number}의 3제곱 {number**3} 입니다.'
    result = number**3
    return render_template('cube.html',result=result,number=number)

@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['치킨','피자','삼겹살','짬뽕','탕수육']
    order = random.sample(menu,people)
    return str(order)

@app.route('/movie')
def movie():
    movies = ['겨울왕국2','포레스트검프','주먹왕랄프','주먹왕랄프2']
    return render_template('movie.html',movies=movies) 

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html',age_in_html=age)              

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/isitbirth')
def isitbirth():
    today = datetime.datetime.now()
    if today.month == 2 and today.day == 28:
        res = True
    else:
        res = False
    return render_template('isitbirth.html',res=res)

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/godname')
def godname():
    name = request.args.get('name')
    first_list=['돈','외모','일복']
    second_list=['순수함','사랑','건물']
    third_list=['똘끼','사랑','한가함']

    first = random.sample(first_list,1)
    seconde = random.sample(second_list,1)
    third = random.sample(third_list,1)

    return render_template('godname.html',name=name,first=first,seconde=seconde,third=third)

if __name__=='__main__':
    app.run(debug=True)