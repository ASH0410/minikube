from flask import Flask
import os
import socket

app = Flask(__name__)

# Application will response to HTTP `/` request.
@app.route("/")
def hello():
    html = "<h2>Hello {name},</h2>" \
           "<h3>Welcome to Flask-App-ONE !!</h3>" \ 
           "<b>Pod-Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv('NAME'), hostname=socket.gethostname())


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000, debug=True)

