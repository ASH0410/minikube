from flask import Flask
import os
import socket

app = Flask(__name__)

# Application will response to HTTP `/` request.
@app.route("/")
def hello():
    html = "<h2>Hello {name},</h2>" \
           "<h3>This is Default-Page, using below convention to go the Application</h3>" \
           "<h4>Go to Flask-App-ONE : http://ip-address/app1</h4>" \
           "<h4>Go to Flask-App-TWO : http://ip-address/app2</h4><br/>" \
           "<b>Pod-Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv('NAME'), hostname=socket.gethostname())


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000, debug=True)

