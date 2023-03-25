from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def index():
    # Create a Bokeh plot
    p = figure(width=400,height=400)
    p.circle([1, 2, 3, 4, 5], [2, 5, 8, 6, 4], size=10)

    # Generate the JavaScript and HTML code to embed the plot in a web page
    script, div = components(p)

    # Render the HTML template that includes the generated JavaScript and HTML code
    return render_template('index.html', script=script, div=div)

if __name__=="__main__":
    app.run(host="0.0.0.0")
