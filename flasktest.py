
from flask import Flask, render_template ,request,Response,redirect,url_for,jsonify,json
app = Flask(__name__)
@app.route("/")
def hello():
    # a = int(request.args.get('a'))
    return "hello, AAAAAAA"

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
    return render_template('page.html' , data=data,text = "text內容")

@app.route('/static')
def staticPage():

    return render_template('static.html')

@app.route('/form')
def formPage():
    return render_template('form.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    try:
        if request.method == 'POST':
            user = request.form['user']
            print("post : user =>",user)
            return redirect(url_for('success', name=user, action='post'))
        else:
            user = request.args.get('user')
            print("get : user =>",user)
            return redirect(url_for('success', name=user, action="get"))
    except:
        return 'QQQ'
@app.route('/success/<action>/<name>')
def success(name, action):
    return '{} : Welcome {} ~ !!!'.format(action, name)

@app.route('/data')
def webapi():
    return render_template('data.html')

@app.route('/data/message',methods=['GET'])
def getDataMessage():
    if request.method == 'GET':
        with open ('jerryflask\static\data\message.json','r') as f :
            data = json.load(f)
            print('text:',data)
        f.close
        return jsonify(data)

@app.route('/data/message',methods=['POST'])
def setDataMessage():
    if request.method == 'POST':
        data={
            'appInfo':{
                'id':request.form['app_id'],
                'name':request.form['app_name'],
                'version':request.form['app_version'],
                'author':request.form['app_author'],
                'remark':request.form['app_remark']
            }
        }
        print(type(data))
        with open ('jerryflask\static\data\input.json','a') as f :
            json.dump(data,f)
        f.close
        return jsonify(result='OK')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #host='0.0.0.0' 使用現在IP
