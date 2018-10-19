from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
import pandas
import datetime
# from flask_sqlalchemy import SQLAlchemy
# from send_email import send_email
# from sqlalchemy.sql import func
from werkzeug import secure_filename

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# explicitly tell apllication that it is post method by default it considers it as get method
@app.route("/success_table/", methods=['post'])
def success_table():
    global filename
    # check if request is post or not
    if request.method=='POST':
        # get the input value of email from form using post request using input name (email_name)
        file=request.files["file"]
        try:
            df=pandas.read_csv(file)
            gc=Nominatim(scheme="http")
            df["coordinates"]=df["Address"].apply(gc.geocode)
            df["Latitude"]=df["coordinates"].apply(lambda x: x.latitude if x != None else None)
            df["Longitude"]=df["coordinates"].apply(lambda y: y.longitude if y != None else None)
            df=df.drop("coordinates",1)
            filename = datetime.now().strftime("uploads/%Y-%m-%d-%H-%M-S-%f"+".csv")
            df.to_csv(filename, index=None)
            return render_template("index.html", text=df.to_html(), btn="download.html")
        except:
            return render_template("index.html", text="Please make sure you have an address field your CSV file")

@app.route("/download-file/")
def download():
    return send_file(filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == "__main__":
    app.debug=True
    app.run()
