import os
from flask import Flask
from flask import render_template
from flask import send_file
from flask import Response


app = Flask(__name__)


@app.route('/')
def root(name = None):
    return render_template('hello.html',name = name)

@app.route('/index.html')
def index():
    with open('index.html','r') as fp:
        content = ''
        for line in fp.readlines():
            content +=  line
    return Response(content, mimetype="text/html")
    

@app.route( "/<path>")
def DownloadLogFile (path = None):
    try:
        return send_file(path, as_attachment=True)
    except:
        return '404'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 80)


