import flask
from flask import jsonify,request
app=flask.Flask(__name__)
app.config["DEBUG"]=True

books=[
    {'id':0,
     'title':'a fire upon deep',
     'author':'venor vinge'},
    {'id':1,
     'title':'the ones who walk away',
     'author':'ursula'},
    {'id':2,
     'title':'dhalgren',
     'author':'samuel'}

]
def hello():
    from tkinter import filedialog
    folder= filedialog.askdirectory()
    return "hello"

@app.route('/',methods=['GET'])
def home():
    return hello()



@app.route('/books/all',methods=['GET'])
def api_all():
    return jsonify(books)
app.run()