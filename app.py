from flask import Flask,request
from flask.templating import render_template
from rank_correlation import calc_rank_correlation,str_to_lis

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    x = []
    y = []
    r = 0
    
    if request.method == "POST":
        val1 = request.form['list1']
        val2 = request.form['list2']
        x = str_to_lis(val1)
        y = str_to_lis(val2)
        #These two x and y are the list to be passed to the rank_correlation function
        r = calc_rank_correlation(x,y)
    return render_template('index.html',x=x,y=y,r=r)

if __name__ == "__main__":

    app.run()