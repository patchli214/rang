from flask import Flask, render_template, request
from flask_mongoengine import MongoEngine
import mongoengine

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(0)
IP = ''
try:
    # doesn't even have to be reachable
    s.connect(('10.254.254.254', 1))
    IP = s.getsockname()[0]
except Exception:
        IP = '127.0.0.1'
finally:
        s.close()

ip = '127.0.0.1'

if IP == '192.168.1.17':
    ip = '192.168.1.34'
print('[DB]'+ip)
mongoengine.connect(host="mongodb://"+ip+":27017/subway")

app = Flask(__name__)

class line(mongoengine.Document):
    name = mongoengine.StringField()
    startdate = mongoengine.DateTimeField()
    company = mongoengine.StringField()

class station(mongoengine.Document):
    name = mongoengine.StringField()
    longitude = mongoengine.StringField()
    latitude = mongoengine.StringField()
    district = mongoengine.StringField()
    startdate = mongoengine.DateTimeField()
    latin = mongoengine.StringField()
    isRunning = mongoengine.BooleanField()
    code = mongoengine.StringField()


class linestation(mongoengine.Document):
    stationName = mongoengine.StringField()
    startdate = mongoengine.DateTimeField()
    lineName = mongoengine.StringField()
    isRunning = mongoengine.BooleanField()
    order = mongoengine.IntField()
    distance = mongoengine.IntField()
    type = mongoengine.IntField()
    typeName = mongoengine.StringField()
    underground = mongoengine.BooleanField()

class stationtype(mongoengine.Document):
    name = mongoengine.StringField()
    typeId = mongoengine.IntField()

@app.route("/")
def hello_world():
    a = []
    b=""
    a.append("<html>")
    a.append("<head>")
    a.append("<style>")
    a.append("p{")
    a.append("color:#FF8800;")
    a.append("font-style:courier new;")
    a.append("font-size:30px;")
    a.append("background:#0077FF")
    a.append("}")
    a.append(".b1{")
    a.append("background-color: #000000;color:#DDDDDD;padding:20px 35px;text-align: center;font-size: 20px;margin: 8px 5px;}")
    a.append(".b1:hover{background-color:#FF0000;color:#0000FF}")
    a.append("</style>")
    a.append("<title>teeeeeeeeest</title>")
    a.append("<meta charset=\"utf-8\">")
    a.append("</head>")
    a.append("<body>")
    a.append("<p>下面的按钮千万别点！！！</p><br><br><br><br><br><br><br><br><br><br><br><br>")
    a.append("<a href=\"https://www.w3schools.com/tags/tag_button.asp\"><button class=\"b1\"> 点这个按钮！</button></a><br><br><br><br><br><br><br><br>")
    a.append("<button class=\"b1\" href=\"https://zh.m.wikipedia.org/wiki/Wikipedia:%E5%8B%95%E5%93%A1%E4%BB%A4/%E7%AC%AC%E4%BA%8C%E5%8D%81%E6%AC%A1%E5%8B%95%E5%93%A1%E4%BB%A4\">别点这个按钮！</button><br><br><br><br><br><br><br><br><br><br>")
    a.append("<button class=\"b1\" href=\"https://map.baidu.com/\">别点这个按钮！</button>")
    a.append("</body>")
    a.append("</html>")
    for i in a:
        b=b+i
    return b
@app.route("/test2")
def test2():
    stations = []
    try:
        stations = linestation.objects()
    except:
        err = 1
    return render_template('/test2.html', test=len(stations),stations=stations)

@app.route("/search", methods=['GET', 'POST'])
def search():
    stations=[]
    keyword = ''
    n = 0
    if request.method == "POST":
        try:
            keyword=request.form['keyword']
            stations=station.objects(name__contains=keyword).order_by('latin')
            n = len(stations)
        except Exception as e:
            err = 1
    return render_template('/search.html',stations=stations,number=n,keyword=keyword)

@app.route("/station", methods=['GET','POST'])
def showStation():
    stations=[]
    temp = []
    stationName = None
    lineName = None
    theStation = None
    theLine = None
    n = 0
    searchType = 'station'
    try:
        types = stationtype.objects()
        stationName=request.args['stationName']
        lineName=request.args['lineName']
        if stationName and len(stationName)>1:
            theStation = station.objects(name=stationName)[0]
            stations=linestation.objects(stationName=stationName).order_by('startdate')
        elif lineName and len(lineName)>1:
            searchType = 'line'
            stations=linestation.objects(lineName=lineName).order_by('order')
            theLine = line.objects(name=lineName)[0]
        for s in stations:
            for t in types:
                if s.type == t.typeId:
                    s.typeName = t.name
            temp.append(s)
        n = len(temp)
    except Exception as e:
        err = 1

    return render_template('/station.html',stations=temp,number=n,station=theStation,searchType=searchType,line=theLine)

@app.route("/lines", methods=['GET','POST'])
def showLines():
    lines=[]
    n = 0
    try:
        lines=line.objects().order_by('startdate')
        n = len(lines)
    except Exception as e:
        err = 1
    return render_template('/lines.html',lines=lines,number=n)
