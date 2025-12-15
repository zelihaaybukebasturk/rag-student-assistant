from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename
import sqlite3
import os

from src.ingest import ingest_pdf
from src.query import ask_question

app = Flask(__name__)
app.secret_key = "super_secret_key"

def get_user(username):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT username, password, role FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    return result

def create_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, 'student')",
            (username, password)
        )
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False


@app.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        if session["role"] == "teacher":
            return redirect("/upload")
        return redirect("/")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = get_user(username)

        if user and user[1] == password:
            session["username"] = username
            session["role"] = user[2]

            if user[2] == "teacher":
                return redirect("/upload")
            else:
                return redirect("/")
        else:
            if user is None:
                return redirect("/register")

            return render_template("login.html", error="Invalid username or password.")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        success = create_user(username, password)

        if success:
            return redirect("/login")
        else:
            return render_template("register.html", error="Username already exists!")

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/", methods=["GET", "POST"])
def index():
    if "username" not in session:
        return redirect("/login")

    answer = None

    if request.method == "POST":
        question = request.form.get("question")
        if question:
            answer = ask_question(question)

    return render_template("index.html", answer=answer)


@app.route("/upload", methods=["GET", "POST"])
def upload_pdf():
    if "username" not in session:
        return redirect("/login")

    if session.get("role") != "teacher":
        return "Access denied: Only teachers can upload PDFs.", 403

    message = None

    if request.method == "POST":
        pdf_file = request.files.get("pdf")
        if pdf_file:
            filename = secure_filename(pdf_file.filename)
            filepath = os.path.join("uploads", filename)
            pdf_file.save(filepath)

            ingest_pdf(filepath)
            message = "PDF uploaded and processed successfully."

    return render_template("upload.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
