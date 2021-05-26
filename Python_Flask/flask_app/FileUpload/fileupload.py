from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
#UPLOAD_FOLDER = '/home/mani/Desktop/Python_Flask/flask_app/FileUpload/uploads/'

app=Flask(__name__)
#app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
@app.route('/upload')
def upload():
    return render_template('index.html')
    
@app.route('/uploader',methods=['POST','GET'])
def uploader():
    if request.method=='POST':
        f=request.files['file']
        f.save(secure_filename(f.filename))
    return 'File uploaded Successfully'
        
@app.route('/success')
def success():
    return 'Logged in successfully'

if __name__=='__main__':
    app.run(debug=True)
