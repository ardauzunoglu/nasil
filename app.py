import os
import json
import time
import random
import boto3
import pandas as pd
from flask import Flask, flash, request, redirect, send_file, url_for, render_template, Response
from werkzeug.utils import secure_filename

app = Flask(__name__)

s3_client = boto3.client('s3',
                        aws_access_key_id="key_id",
                        aws_secret_access_key="access_key")
bucket = boto3.resource('s3', 
                        aws_access_key_id="key_id",
                        aws_secret_access_key="access_key").Bucket('nasil')

def remove_punc(str):
    import string
    new_string = str.translate(str.maketrans('', '', string.punctuation))
    return new_string

def improve_search(search, title):
    search_words = search.split()
    title_words = title.split()

    for search_word in search_words:
        if search_word in title_words:
            return True

    return False

@app.route("/", methods=["GET", "POST"])
@app.route("/anasayfa", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search = request.form["search"]
        sent_query = True
        tutorial_titles = [remove_punc(obj.key.split("/")[-1].replace(".json", "")).lower() for obj in bucket.objects.all()]
        
        related_titles = [title.title() for title in tutorial_titles if (search.lower() in title) and improve_search(search.lower(), title)]
        found_related_titles = (not(len(related_titles) == 0))

        redirect(url_for("index", found_tutorials=related_titles, found_related_titles=found_related_titles, sent_query=sent_query))
    
    else:
        sent_query = False
        found_related_titles = False
        related_titles = []

    return render_template("index.html", found_tutorials=related_titles, sent_query=sent_query, found_related_titles=found_related_titles)

@app.route("/ekip")
def ekip():
    return render_template("ekip.html")

@app.route("/hedefler")
def hedefler():
    return render_template("hedefler.html")

@app.route("/rehber")
def rehber():
    return render_template("rehber.html")

if __name__ == "__main__":
    app.run(debug=True)
