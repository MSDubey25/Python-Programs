from flask import Flask
app=Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!!!'

@app.route('/app/<name>')
def maker(name):
    return '%s!!! is Running his First Falsk Application' %name

@app.route('/exit')
def exiting():
    return 'Exiting the Application'
    
if __name__=='__main__':
    app.run('127.0.0.1',5000,True)
#app.debug=True
#app.run(debug=True)
#app.run('127.0.0.1',5000,True)
