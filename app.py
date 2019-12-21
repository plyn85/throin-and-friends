import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
# provding a a secret key for flash messages
app.secret_key = "some_secret"


@app.route("/")
def index():
    return render_template("index.html")

    # setting an empty array
    # opening the company json file then reading the data as json data
    # then loading the data json variable and adding it to the data array
    # changing the data that being passed through to a comapny variable when its being returned


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


# route is about image link about html page link
# function is called about member and takes on agrument member name
# empty member object created
# opening and reading json data file an adding json data var
# adding data var setting loaded json data to it
# looping through json data
# if the url is equal to member name
# then add it to the empty member object from above
# retrun the member html page and making the member object equal to the member var
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


# routes to the contact html page and also uses get an request methods
# if the request method is equal to a post in the contact form page then print it
# print(request.form) would send the users infomation to the terminal
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {} we have got your message".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)

