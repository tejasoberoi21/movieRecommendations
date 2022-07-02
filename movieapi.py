from flask import Flask, jsonify, request
import pandas as pd
import csv

    

movies = pd.read_csv("/Users/tejasoberoi/Downloads/movies.csv")
movieDf = movies

#print(movieDf)

movieList = []

#print(len(movieDf))

for numRows in range(len(movieDf)):
    movieList.append({})

for column in movieDf:
    for index,val in enumerate(movieDf[column]):
        movieList[index][column] = val

#print(movieList)
print(len(movieList))
print(movieList[0])


likedMovies = []
dislikedMovies = []
didNotWatch = []

app = Flask(__name__)

@app.route("/GET")
def getMovie():
    return jsonify({
        "data": movieList[0],
        "status":"Success",
        })

@app.route("/likedMovies", methods = ["POST"])
def addLike():
    like = movieList[0]
    movieList = movieList[1:]

    likedMovies.append(like)

    return jsonify({
        "status":"Success"
        })

@app.route("/dislikedMovies", methods = ["POST"])
def addDislike():
    dlike = movieList[0]
    movieList = movieList[1:]

    dislikedMovies.append(dlike)

    return jsonify({
        "status":"Success"
        })

@app.route("/didNotWatch", methods = ["POST"])
def addDNW():
    dnw = movieList[0]
    movieList = movieList[1:]

    didNotWatch.append(dnw)

    return jsonify({
        "status":"Success"
        })


if(__name__ == "__main__"):
    app.run()
    



    
