from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    index veiw function
    '''
    return render_template('index.html')