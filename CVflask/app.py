from flask import Flask ,url_for , redirect , render_template

app = Flask(__name__)


@app.route('/home')
@app.route('/main')
@app.route('/')
def index():
    return render_template('cv.html')


@app.route('/assignment8')
def ass8():
    name = 'Ido'
    title = 'Hobbies'
    hobbieslist = ['Cooking','Diving','Traveling']
    return render_template('assignment8.html',
                               curr_user={'firstname': name, 'lastname': 'Eitan'},
                               title=title, hobbies=hobbieslist)


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
