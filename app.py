from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
    products = [
    {"n":"Milk", "p":35, "e":""},
    {"n":"Rice", "p":60, "e":""},
    {"n":"Tea", "p":220, "e":""},
    {"n":"Sugar", "p":45, "e":""},
    {"n":"Oil", "p":140, "e":""},
    {"n":"Soap", "p":38, "e":""}
]
    return render_template("index.html",products=products)
app.run(debug=True)