from flask import Flask, render_template,request, make_response, session, url_for, redirect
app=Flask(__name__)
app.secret_key="any random string"
@app.route('/')
def index():
    if 'user' in session:
        username=session['user']
        return 'Logged in as '+username+'<br>'+ \
            "<b><a href='/logout'>Click Here to Logout</a></b>"
    return "You are not logged in <br><a href='/login'></b>"+ \
        "Click Here to Login</b></a>"
    
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        session['user']=request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')
        
@app.route('/logout')
def logout():
#remove the username from the session if it is there
    session.pop('user',None)
    return redirect(url_for('index'))
        
if __name__=='__main__':
    app.run(debug=True)
