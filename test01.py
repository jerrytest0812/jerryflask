from dataclasses import dataclass
from flask import Flask, render_template ,request,Response
app = Flask(__name__)
@app.route("/")
def hello():
    # a = int(request.args.get('a'))
    return "hello, world"

@app.route("/<int:id>",methods=['GET'])
def queryDataMessageByName(id):
    print('type(id):',type(id))
    return 'int => {}'.format(id)

@app.route("/text")
def text():
    return '<html><body><h1>Hello World</h1></body></html>'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/page/text')
def pageText():
    return render_template('page.html', text="Python Flask !")

@app.route('/page/app')
def pageAppInfo():
    appInfo = {'id': 5 ,
    'name' : 'python - Flask',
    'version' : '1.0.1',
    'author' : 'Enoxs',
    'remark' : 'python - Web Framework'
    }
    return render_template('page.html', appInfo=appInfo)

@app.route('/page/data')
def pageDate():
    data = {
        '01' : '111 222 333',
        '02' : 'AAA BBB CCC',
        '03' : 'text text text',
        '04' : 'QQQ QQQ QQQ',
        '05' : '中文 可以 嗎?'
    }
    return render_template('page.html' , data=data)

@app.route('/static')
def staticPage():
    return render_template('static.html')

if __name__ == '__main__':
    app.run()