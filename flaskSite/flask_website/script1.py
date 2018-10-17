from flask import Flask, render_template

# create object of Flask class
app = Flask(__name__)

# create url for bokeh graphs
@app.route("/plot/")
# define function to call graphs
def plot():
    from pandas_datareader import data
    import datetime
    import fix_yahoo_finance as yf
    yf.pdr_override()
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    start=datetime.datetime(2015,11,1)
    end=datetime.datetime(2016,3,10)

    df=data.get_data_yahoo(tickers="GOOG", start=start, end=end)


    def inc_dec(c, o):
        if c > o:
            value="Increase"
        elif c < o:
            value="Decrease"
        else:
            value="Equal"
        return value

    df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close,df.Open)]
    df["Middle"]=(df.Open+df.Close)/2
    df["Height"]=abs(df.Close-df.Open)

    p=figure(x_axis_type='datetime', width=1000, height=300, sizing_mode="scale_width")
    p.title.text="Candlestick Chart"
    p.grid.grid_line_alpha=0.3

    hours_12=12*60*60*1000

    p.segment(df.index, df.High, df.index, df.Low, color="Black")

    p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],
           hours_12, df.Height[df.Status=="Increase"],fill_color="#CCFFFF",line_color="black")

    p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],
           hours_12, df.Height[df.Status=="Decrease"],fill_color="#FF3333",line_color="black")

    # to embed graph code to the website
    script1, div1 = components(p)

    # get the cdns for bokeh graphs to put in the script link
    cdn_js=CDN.js_files[0] # gives list of javascript files
    cdn_css=CDN.css_files[0] # gives list of css files


    # while embedding the graph to your website you don't need below 2 lines
    # output_file("CS.html")
    #
    # show(p)

    # use render_template to call html file
    return render_template("plot.html",
    script1=script1,
    div1=div1,
    cdn_css=cdn_css,
    cdn_js=cdn_js )

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
