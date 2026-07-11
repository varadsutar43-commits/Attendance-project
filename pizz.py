from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    result = ""
    if request.method == "POST":
        name = request.form["name"]
        qty = int(request.form["qty"])
        total = qty * 250
        result = f"""
        <h3>Order Confirmed</h3>
        Customer : {name}<br>
        Quantity : {qty}<br>
        Total Bill : ₹{total}
        """

    return render_template_string("""
    <h2> Pizza Order System</h2>

    <form method="POST">
    
    Name<br>
    <input name="name"><br><br>

    Quantity<br>
    <input type="number" name="qty"><br><br>

    <input type="submit" value="Place Order">

    </form>

    <hr>

    {{result|safe}}

    """,result=result)  

app.run(debug=True)                                




