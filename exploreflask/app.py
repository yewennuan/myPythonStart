from flask import Flask
if __name__ =="__main__":
    app = Flask(__name__)
    app.config.from_object('config')
    print app.config["MAIL_FROM_EMAIL"]
