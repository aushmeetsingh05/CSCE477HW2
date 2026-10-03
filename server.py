from flask import Flask, request, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory(app.root_path, "index.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    if email == "" or password.strip() == "":
        return "Please enter your email and password.", 400

    if "@" not in email:
        return "Your email must contain @.", 400

    if len(password) < 8:
        return "Your password must be at least 8 characters.", 400

    return f"<p>Input accepted for: {email}</p>"


if __name__ == "__main__":
    app.run()