from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
# connect to the database using app.config['SQLALCHEMY_DATABASE_URI']="postgres://username:password@servername/database name" this is for localhost
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:pass123@localhost/height_collector'
# Create SOLAlchemy object for your application
db=SQLAlchemy(app)

class Data(db.Model):
    # create table
    __tablename__="data"
    # create table columns
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    height=db.Column(db.Integer)

    def __init__(self,email,height):
        self.email = email
        self.height = height


@app.route("/")
def index():
    return render_template("index.html")

# explicitly tell apllication that it is post method by default it considers it as get method
@app.route("/success/", methods=['post'])
def success():
    # check if request is post or not
    if request.method=='POST':
        # get the input value of email from form using post request using input name (email_name)
        email=request.form["email_name"]
        # print(email)
        # get the input value of height from form using post request using input name(height_name)
        height=request.form["height_name"]
        # get all input requests of form
        # print(request.form)
        # print(height)


        # do data validation for unique email value
        if db.session.query(Data).filter(Data.email==email).count()==0:
            # create Object instance of Data class
            data=Data(email,height)
            # send data to the table using session.add method for db object
            db.session.add(data)
            # commit the changes using session.commit method of db object
            db.session.commit()
            # calculate the average height of the data from the table
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height=round(average_height,1)
            count=db.session.query(Data.height).count()

            # call send email function to send an email
            send_email(email, height, average_height, count)
            print(average_height)
            return render_template("success.html")
        else:
            return render_template("index.html", text="Seems like we have got something from that email address already!")

if __name__ == "__main__":
    app.debug=True
    app.run()
