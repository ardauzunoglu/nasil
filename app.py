import re
import json
import time
import random
import boto3
import pandas as pd
from flask import Flask, flash, request, redirect, send_file, url_for, render_template, Response
from werkzeug.utils import secure_filename

app = Flask(__name__)

s3_client = boto3.client('s3',
                        aws_access_key_id="AKIAW3MNVVBF2QXVLXUM",
                        aws_secret_access_key="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")
bucket = boto3.resource('s3', 
                        aws_access_key_id="AKIAW3MNVVBF2QXVLXUM",
                        aws_secret_access_key="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").Bucket('nasil')

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
        
        related_titles = [title.title() for title in tutorial_titles if (search.lower() in title) and improve_search(search.lower().strip(), title)]
        found_related_titles = (not(len(related_titles) == 0))

        redirect(url_for("index", found_tutorials=related_titles, found_related_titles=found_related_titles, sent_query=sent_query))
    
    else:
        sent_query = False
        found_related_titles = False
        related_titles = []

    return render_template("index.html", found_tutorials=related_titles, sent_query=sent_query, found_related_titles=found_related_titles)

@app.route("/rehber/<baslik>")
def rehber(baslik):

    with open('data.json', 'wb') as f:
        s3_client.download_fileobj('nasil', "ultimate-wikihow-tr/"+baslik+".json", f)

    data = json.load(open('data.json', "r", encoding="utf-8"))
    if "methods" in data.keys():
        for method in data["methods"]:
            method["index"] = data["methods"].index(method) + 1
            for step in method["steps"]:
                step["description"] = re.sub(r'{.+?}', '', step["description"])
                step["index"] = method["steps"].index(step) + 1

    if "parts" in data.keys():
        for part in data["parts"]:
            part["index"] = data["parts"].index(part) + 1
            for step in part["steps"]:
                step["description"] = re.sub(r'{.+?}', '', step["description"])
                step["index"] = part["steps"].index(step) + 1

    if "steps" in data.keys():
        for step in data["steps"]:
            step["description"] = re.sub(r'{.+?}', '', step["description"])
            step["index"] = data["steps"].index(step) + 1

    categories = " >> ".join(data["category_hierarchy"])

    return render_template("rehber.html", data=data, categories=categories)

@app.route("/ekip")
def ekip():
    return render_template("ekip.html")

@app.route("/hedefler")
def hedefler():
    return render_template("hedefler.html")

@app.route("/kullanim_rehberi")
def kullanim_rehberi():
    return render_template("kullanim_rehberi.html")

if __name__ == "__main__":
    app.run(debug=True)