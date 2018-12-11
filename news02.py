""" javi ruiz / News API

API key is: f0c3b74c78fb4f6ea931c1fb9c3bc883
user input = category
python output = 2 headlines
"""
import requests
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

#run this route to start, to imput category
@app.route("/news/category")
def get_category():
    return render_template("news_index.html")


#run this route to output 2 news
@app.route("/news/show", methods=['POST'])
def show_article():
    category = request.form["category_code"]
    #TODO: if category not if
    ok_category = ["business", "entertaiment", "health", "science", "sports", "technology"]
    if category not in ok_category:
        no_category = "Please choose a category from the list"
        return render_template("news_index.html", no_category= no_category)
    else:
        response = requests.get("https://newsapi.org/v2/top-headlines?country=au&category="+category+"&apiKey=f0c3b74c78fb4f6ea931c1fb9c3bc883").json()

        title1 = response["articles"][0]["title"]
        description1 =  response["articles"][0]["description"]
        url1 = response["articles"][0]["url"]
        image1 = response["articles"][0]["urlToImage"]

        title2 = response["articles"][1]["title"]
        description2 =  response["articles"][1]["description"]
        url2 = response["articles"][1]["url"]
        image2 = response["articles"][1]["urlToImage"]
        return render_template("show_index.html", category= category, title1= title1, description1= description1, url1= url1, image1= image1, title2= title2, description2= description2, url2= url2, image2= image2)


if __name__ == "__main__":
    app.run(debug=True)
