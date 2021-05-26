from flask import Flask
from flask_mail import Mail, Message
app = Flask('__main__')
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'disastercoc@gmail.com'
app.config['MAIL_PASSWORD'] = '9168317083'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def index():
    msg = Message('Hello', sender='disastercoc@gmail.com', recipients=['manikant.dubey1995@gmail.com'])
    msg.body = "Hello Flask! This Message is sent from Flask-Mail"
    mail.send(msg)
    return 'Message Sent'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
