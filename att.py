from flask import Flask, request, render_template_string

app = Flask(__name__)

attendance = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        attendance.append({
            "roll": request.form["roll"],
            "name": request.form["name"],
            "status": request.form["status"]
        })

    return render_template_string("""

<html>

<head>
    <title>Attendance Entry System</title>
</head>

<body style="font-family:Arial; margin:40px;">

<h1>Attendance Entry System</h1>

<form method="POST">

Roll Number<br>
<input type="text" name="roll" required><br><br>

Student Name<br>
<input type="text" name="name" required><br><br>

Attendance<br>
<select name="status">
    <option>Present</option>
    <option>Absent</option>
</select><br><br>

<input type="submit" value="Save Attendance">

</form>

<hr>

<h2>Today's Attendance</h2>

<table border="1" cellpadding="8">

<tr>
    <th>Roll No</th>
    <th>Name</th>
    <th>Status</th>
</tr>

{% for s in attendance %}

<tr>
    <td>{{ s.roll }}</td>
    <td>{{ s.name }}</td>
    <td>{{ s.status }}</td>
</tr>

{% endfor %}

</table>

<br>

<b>Total Students:</b> {{ attendance|length }}

</body>

</html>

""", attendance=attendance)

if __name__ == "__main__":
    app.run(debug=True)