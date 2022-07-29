from flask import Flask

app = Flask(__name__)

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
    a.append("/<head>")
    a.append("<body>")
    a.append("<p>下面的按钮千万别点！！！</p><br><br><br><br><br><br><br><br><br><br><br><br>")
    a.append("<button class=\"b1\" href=\"https://www.w3schools.com/tags/tag_button.asp\">点这个按钮！</button><br><br><br><br><br><br><br><br>")
    a.append("<button class=\"b1\" href=\"https://zh.m.wikipedia.org/wiki/Wikipedia:%E5%8B%95%E5%93%A1%E4%BB%A4/%E7%AC%AC%E4%BA%8C%E5%8D%81%E6%AC%A1%E5%8B%95%E5%93%A1%E4%BB%A4\">别点这个按钮！</button><br><br><br><br><br><br><br><br><br><br>")
    a.append("<button class=\"b1\" href=\"https://map.baidu.com/\">别点这个按钮！</button>")
    a.append("</body>")
    a.append("</html>")
    for i in a:
        b=b+i
    return b
