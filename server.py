from flask import Flask
from flask import request
import json
from recommender import recommender as rcm
app = Flask(__name__)
r = rcm()

@app.route('/getdata',methods = ['POST'])
def getdata():
    return "nitin"

@app.route('/train/',methods = ['POST'])
def train():
    print(request.json)
    reqdict = request.json
    print(reqdict)
    movievalues = reqdict["movies"]
    userratings = reqdict["userratings"]
    
    r.createMoviesDF(movievalues)
    r.createUserRatingDF(userratings)
    r.mergeDF()
    r.createDataMatrix()
    r.generateUserSimilarityMatrix()

    print(request.json)
    return "weights generated"

@app.route('/getResult/',methods = ['POST'])
def getResult():
    reqdict = request.json
    usertopred = reqdict["usertopred"]
    result = r.getResultFor(usertopred)
    res = json.dumps(result)
    return res
