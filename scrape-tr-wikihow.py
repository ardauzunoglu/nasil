from bs4 import BeautifulSoup
import requests
import re
import json
import os
import shutil
import xml.etree.ElementTree as ET

def create_json_file(url):
    special_chars = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "\\", "/", ":", ";", '"', "'", "<", ">", ",", ".", "?"]

    json_dict = {
    }

    url = url
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    article_title = doc.find(id="section_0").text
    json_dict["title"] = article_title

    json_dict["url"] = url

    article_description = doc.find(class_="mf-section-0").text.replace("\n", "")
    json_dict["title_description"] = article_description

    category_hierarchy = []
    try:
        for category_list in doc.find(id="breadcrumb"):
            for category in category_list.find_all():
                if category.text != "Categories":
                    category_hierarchy.append(category.text)
    except:
        pass
    json_dict["category_hierarchy"] = category_hierarchy

    author_dict = {}
    try:
        coauthor_label = doc.find(class_="sp_coauthor_label")
        author_dict["name"] = doc.find(class_="sp_expert_name").text

    except:
        author_dict["name"] = "Unknown"

    try:
        author_dict["blurb"] = doc.find(class_="sp_expert_blurb").text
    except:
        author_dict["blurb"] = "Unknown"

    json_dict["author"] = author_dict

    stats = doc.find(class_="page_stats").text.split()
    n_views = stats[stats.index("sayfaya")+1]
    json_dict["n_views"] = n_views

    related_articles = []
    related_wikihows = doc.find_all(class_="related-wh")
    for related_wh in related_wikihows:
        for tag in related_wh.find_all():
            if tag.name == "img":
                img = tag.get("src")

        article_dict = {"title": related_wh.get("href").replace("-", " ").replace("/", ""),
                        "link": "https://www.wikihow.com" + related_wh.get("href"),
                        "img": img}

        related_articles.append(article_dict)
    json_dict["related_articles"] = related_articles[:14]

    tip_list = []
    tips = doc.find(id="ipuçları")
    try:
        for tip in tips.find_all():
            if tip.name == "li":
                tip_text = tip.div.text
                tip_list.append(tip_text.replace("\u2019", "'").replace("\n", "").replace("\t", ""))
    except:
        pass
    json_dict["tips"] = tip_list

    warning_list = []
    warnings = doc.find(id="uyarılar")
    try:
        for warning in warnings.find_all():
            if warning.name == "li":
                warning_text = warning.div.text
                warning_list.append(warning_text.replace("\u2019", "'").replace("\n", "").replace("\t", ""))
    except:
        pass
    json_dict["warnings"] = warning_list

    references = []
    reference_list = doc.find_all(class_="references")
    for reference in reference_list:
        references.append(reference.text.replace("↑", "").strip())

    references = list(set("".join(references).replace("Referanslar", "").split("\n\n\n")))
    for reference in references:
        references[references.index(reference)] = reference.strip("\n").strip()
        if len(reference) == 0:
            references.remove(reference)
    try:
        references[0] = references[0][1:]
    except IndexError:
        pass
    json_dict["references"] = references

    languages_dict = {}
    language_links = doc.find_all(class_="language_link")
    for link in language_links:
        language = link.span.text
        language_link = link.a.get("href")
        languages_dict[str(language)] = language_link

    json_dict["other_languages"] = languages_dict

    sections = doc.find_all(class_="section")
    spans = [section.find(class_="mw-headline") for section in sections]
    pm_titles = []
    for span in spans:
        try:
            pm_titles.append(span.get("id").replace("-", " "))
        except:
            pass
    
    try:
        material_type = doc.find(class_="method_label").text
        if "method" in material_type.lower():
            material_type="methods"
        elif "part" in material_type.lower():
            material_type="parts"
    except:
        material_type="steps"

    json_dict["methods"] = []
    json_dict["parts"] = []
    json_dict["steps"] = [] 
    max_no = int(doc.find_all("div", id=re.compile("^adımlar_"))[-1].get("id").replace("adımlar_", ""))
    print(max_no)
    pm_titles = pm_titles[:max_no]
    print(pm_titles)
    for title in pm_titles:
        steps_div = doc.find(id="adımlar_"+str(pm_titles.index(title) + 1))
        try:
            steps_list = steps_div.find(class_="steps_list_2")
        except AttributeError:
            pass
        try:
            filtered_steps = list(filter(lambda steps: str(type(steps)) == "<class 'bs4.element.Tag'>", steps_list))
        except TypeError:
            filtered_steps = []
        pm_dict = {}
        pm_dict["name"] = title.replace(".C3.A7", "ç").replace(".C4.B1", "ı").replace(".C4.B0", "İ").replace(".C5.9E", "Ş").replace(".C4.9F", "ğ").replace(".C3.9C", "Ü").replace(".C3.BC", "ü").replace(".C5.9F", "ş").replace(".C3.87", "Ç").replace(".C3.96", "Ö").replace(".C3.B6", "ö").replace(".E2.80.99", "'")
        pm_dict["steps"] = []
        
        for steps in filtered_steps:
            step = steps.find(class_="step")
            if step != None:
                tags = step.find_all()
                internal_links = []
                for tag in tags:
                    if (tag.name == "a") and ("/" in tag.get("href")):
                        if tag.get("href")[0] == "/":
                            internal_links.append("https://www.wikihow.com" + tag.get("href"))
                        else:
                            internal_links.append(tag.get("href"))
                step_text = step.text.replace("\n", " ").replace("X Research source", "").replace("Reklam", "").replace("\t", "")
                step_text = re.sub('\{.*?}','',step_text, flags=re.DOTALL)
                step_text = re.sub('\[.*?]','',step_text, flags=re.DOTALL)
                step_text = re.sub(' +', ' ', step_text)
                step_headline = step_text.split(".")[0] + ".".strip()
                step_description = ".".join(step_text.split(".")[1:]).strip()
                try:
                    image = step.parent.find(class_="image")
                    image_url = "https://www.wikihow.com/" + article_title.replace(" ", "-").replace("How-to-", "") + image.get("href")
                except:
                    image_url = None
                step_dict = {}
                step_dict["headline"] = step_headline[1:]
                step_dict["description"] = step_description
                step_dict["img"] = image_url
                step_dict["internal_links"] = list(set(internal_links))
                step_dict["image_license"] = "Creative Common"

                pm_dict["steps"].append(step_dict)

        if material_type.lower() == "parts":
            json_dict["parts"].append(pm_dict)
        elif material_type.lower() == "methods":
            json_dict["methods"].append(pm_dict)
        else: 
            json_dict["steps"].append(pm_dict)
    
    for char in special_chars:
        article_title = article_title.replace(char, "")

    with open("wikihow_13_07_2022/"+article_title+".json", "w", encoding="utf-8") as outfile:
        json.dump(json_dict, outfile, indent=4, ensure_ascii=False)

urls = []

for url in urls:
    try:
        create_json_file(url)
    except:
        pass