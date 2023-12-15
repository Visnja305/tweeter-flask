# !!START
from flask import Flask,render_template
from .config import Config
import random
from .tweets import tweets
app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    tweet_index=random.randint(0,3)
    tweet=tweets[tweet_index]
    return render_template("index.html", tweet=tweet)
@app.route("/feed")
def feed():
    return render_template("feed.html",tweets=tweets)
# !!END
