from flask import Flask
from flask import render_template




#import os
#import socket
# Connect to Redis
#redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)
@app.route("/")
def statichtml():
    return render_template('index.html')

@app.route("/contact-me")
def hello():
    html = ">a href="mailto:c15755031@mydit.ie">Link Text</a>"
    #html = "<h3>Hello {name}!</h3>" \
    #       "<b>Hostname:</b> {hostname}<br/>" \
    #       "<b>Visits:</b> {visits}"
    #return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
