from flask import Flask, render_template, request
import json

account_database = json.load(open("databases/accounts.json", "r"))

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        designation = request.form.get('designation')

        if username not in account_database['users']:
            uid = len(account_database['users'])
    
            account_database['accounts'][uid] = {
                "username": username,
                "password": password,
                "designation": designation 
            }
    
            account_database['users'].append(username)

            json.dump(account_database, open("databases/accounts.json", "w"))

        return render_template("signup.html")
    else:
        return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username in account_database['users']:
            uid = str(account_database['users'].index(username))
            if password == account_database['accounts'][uid]['password']:
                return "Login successful"
        
        return "Login failed"

    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
