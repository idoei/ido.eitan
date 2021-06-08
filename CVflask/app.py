from flask import Flask, url_for, redirect, render_template, request, session, jsonify, Blueprint
import mysql.connector

app = Flask(__name__)
app.secret_key = '3196'

from pages.Assignment10.Assignment10 import Assignment10
app.register_blueprint(Assignment10)


@app.route('/home')
@app.route('/main')
@app.route('/')
def index():
    return render_template('cv.html')


@app.route('/assignment8')
def ass8():
    name = 'Ido'
    title = 'Hobbies'
    hobbieslist = ['Cooking', 'Diving', 'Traveling']
    return render_template('assignment8.html',
                           curr_user={'firstname': name, 'lastname': 'Eitan'},
                           title=title, hobbies=hobbieslist)


@app.route('/assignment9')
def ass9():
    name = 'Ido'
    title = 'Hobbies'
    hobbieslist = ['Cooking', 'Diving', 'Traveling']
    return render_template('assignment9.html',
                           curr_user={'firstname': name, 'lastname': 'Eitan'},
                           title=title, hobbies=hobbieslist)


@app.route('/search')
def searchform():
    users = [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ]
    if 'searchinput' in request.args:
        search = request.args['searchinput']
    else:
        search = ""
    if search == "":
        return render_template('assignment9.html', search=users)
    flag = False
    for user in users:
        if user['first_name'] == search or user['email'] == search:
            flag = True
            return render_template('assignment9.html', searchfound=user)
    if not flag:
        return render_template('assignment9.html', notfound="Item not found!")


@app.route('/register', methods=['POST'])
def registerform():
    if 'username' in request.form:
        user_name = request.form['username']
        user_pass = request.form['password']
        user_email = request.form['email']
        user_nickname = request.form['nickname']
    else:
        user_name, user_pass, user_email, user_nickname = '', '', '', ''
    session['username'] = user_name
    session['password'] = user_pass
    session['email'] = user_email
    session['nickname'] = user_nickname
    return render_template('assignment9.html', user_name=user_name, user_pass=user_pass, user_email=user_email,
                           user_nickname=user_nickname)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        session.pop('password', None)
        session.pop('email', None)
        session.pop('nickname', None)
        return render_template('assignment9.html')


@app.route('/uniqueSheet')
def uniquestyle():
    return redirect("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")


@app.route('/intagram')
def intagramlink():
    return redirect("https://www.instagram.com/idoei")


@app.route('/customers')
def customerslink():
    return render_template('customers.html')


@app.route('/facebook')
def facebooklink():
    return redirect("https://www.facebook.com/ido.eitan")


@app.route('/contacts')
def showcontacts():
    return render_template('contactList.html')


@app.route('/header')
def headeronpages():
    return render_template('header.html')


if __name__ == '__main__':
    app.run()
