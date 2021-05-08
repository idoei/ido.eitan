from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')  # defines which func will run when uploading the ROOT page
def hello_world():
    return redirect(url_for('home_page'))


@app.route('/settings')  # defines which func will run when opening the settings page
def hello_settings():
    setting_once = True
    if setting_once:
        return redirect('/')
    else:
        return 'Welcome to the settings page'


@app.route('/more')
def home_page():
    return 'Welcome to the ROOT page by url_for with more'


if __name__ == '_main_':
    app.run(debug=True)