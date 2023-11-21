from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)
connection = psycopg2.connect(host="localhost", dbname="DB_ass", user="postgres", password="qsxdcftat03", port=5432)

@app.route("/")
def index():
    with connection.cursor() as cur:
        cur.execute("SELECT * FROM public.user;")
        data = cur.fetchall()
    return render_template("index.html", data=data)


@app.route("/create", methods=["POST"])
def create():
    return redirect(url_for("index"))


@app.route("/update/<id>", methods=["POST"])
def update(id):
    return redirect(url_for("index"))


@app.route("/delete/<id>")
def delete(id):
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
