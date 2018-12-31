from flask import Flask, request, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route("/get")
def get():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from data")
    data = c.fetchall()
    return "<br>".join([i[0] for i in data])


@app.route("/register")
def register():
    code = request.args.get('code')
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO data VALUES (?)", (code,))
        conn.commit()
        return f"Successfully added {code}"
    except sqlite3.Error as e:
        return str(e)


@app.route("/search")
def search():
    code = request.args.get('code')
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    try:
        c.execute("select * from data where data='" + code + "'")
        found = c.fetchall()
        if found == []:
            return "Invalid Code"
        else:
            return "Wifi Connection Established"
    except sqlite3.Error as e:
        return str(e)


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
