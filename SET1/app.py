from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

creds = {
    'teja@gmail.com' : '1234',
    'gad@gmail.com' : '2345',
    'karan@gmail.com' : '3456',
    'ram@gmail.com' : '4567',
    'newtz@gmail.com' : '5678'
}

roles = {
    'teja@gmail.com' : 'admin',
    'gad@gmail.com' : 'admin',
    'karan@gmail.com' : 'student',
    'newtz@gmail.com' : 'student',
    'ram@gmail.com' : 'staff'
}

admin = {
    'teja@gmail.com' : 'teja',
    'gad@gmail.com' : 'GAD'
}

student = {
    'karan@gmail.com' : 'Karan',
    'newtz@gmail.com' : 'Newton'
}
staff = {
    'ram@gmail.com' :'Ram'
}

food = {
    '1' : 'apple',
    '2' : 'banana',
    '3' : 'mango',
    '4' : 'pineapple',
    '5' : 'jack fruit',
}

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "You have already logged in... <a href='/logout'>Logout</a>"

@app.route('/register')
# For showing register page
def register():
    return render_template('registration.html')

# url_for('addToCart', item = "banana")

# @app.route('/addToCart/<string:item>')
# def addToCart(item):
#     print(item)

@app.route('/register_details', methods=['POST'])
# Storeing register details
def store():
    email = request.form['email']
    uname =  request.form['username']
    passw = request.form['password']   
    role = request.form['role']       
    print(uname + " " + passw + ' ' + email + " " + role)

    creds[email] = passw

    if(role == 'Admin'):
        admin[email] = uname
        roles[email] = 'admin'
    elif(role == "Stuent"):
        student[email] = uname
        roles[email] = 'student'
    else:
        staff[email] = uname
        roles[email] = 'staff'
    
    creds[email] = passw

    print(admin)
    print(creds)
    return ("done")


@app.route('/handle', methods=['POST'])
# Login auth
def handle_data():
    print(creds)
    email =  request.form['email']
    passw = request.form['password']  
    if(creds[email] == passw):
        session['logged_in'] = True
        if(roles[email] == 'admin'):
            name =  admin[email]
            return render_template('ad&staffHome.html', name= name)
        elif(roles[email] == 'staff'):
            name =  staff[email]
            return render_template('ad&staffHome.html', name = name)
        elif(roles[email] == 'student'):
            return render_template('student.html', result = food)
    else:
        return("Wrong Password")
  
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
