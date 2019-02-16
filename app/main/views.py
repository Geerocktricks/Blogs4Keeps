from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    index veiw function
    '''
    title = 'My personal Blog'
    return render_template('index.html' , title = title)