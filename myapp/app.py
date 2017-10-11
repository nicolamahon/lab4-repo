from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def statichtml():
    return render_template('index.html')

@app.route("/contact-me")
def hello():
    html = "<a href=\"mailto:c15755031@mydit.ie\">Link Text</a>"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
