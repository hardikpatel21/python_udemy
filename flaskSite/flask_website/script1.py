from flask import Flask, render_template

# create object of Flask class
app = Flask(__name__)

# call root file which in this case script1.py
@app.route('/')
# define function for default file
def home():
    # use render_template to call html file
    return render_template("home.html")

# create the url for about page e.g. localhost:5000/about
@app.route('/about/')
# fefine function for about page
def about():
    # use render_template to call html file
    return render_template("about.html")

# check weater name is main or not in this case main is True but if we are imprting
# file from somewhere else than __main__ should be the file name like script.py
if __name__=="__main__":
    # run the web app and seting up debuging mode to True
    app.run(debug=True)
