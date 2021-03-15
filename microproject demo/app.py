from flask import Flask, render_template, request
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

from SCRAPER import delish,epicurious

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Home Page')

@app.route('/listing.html', methods =['POST'])
def result():
   
    recipename = request.form['recipe']
    e1,e2,e3,e4= epicurious(recipename)
    d1,d2,d3,d4= delish(recipename)
    
    
    rn= d1 + e1
    src= d2 + e2
    desc= d3 + e3
    alink= d4 + e4    
    n=len(rn)

    data= zip(rn,src,desc,alink)
    return render_template('listing.html', search = recipename, data=data, n=n)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('index.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
