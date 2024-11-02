from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

42880914286302613

@app.route("/<html_file>")
def html_page(html_file):
    return render_template(html_file)

def write_to_file(data):
    with open("./database.txt", "a") as my_database:
        for key, value in data.items():
            my_database.write(f"{key}: {value}\n")
        my_database.write("\n")

def write_to_csv(data):
    with open("./database.csv", "a") as database_2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer = csv.writer(database_2, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "did not save to database"
    else:
        return "something went wrong. Try again!"
