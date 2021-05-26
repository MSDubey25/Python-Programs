from flask import Flask, redirect, url_for, abort, render_template, request, flash
app=Flask(__name__)
app.secret_key="Random String"
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/login',methods=['POST','GET'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'admin':
            error="Invalid Username or Password. Please Try Again!!!"
        else:
            flash('You Were Successfully Logged in')
            flash('Logout before login again')
            return redirect(url_for('index'))
    return render_template('login.html',error=error)
        
@app.route('/success')
def success():
    return 'Logged in successfully'

if __name__=='__main__':
    app.run(debug=True)
