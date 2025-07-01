from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return "<h1>Welcome to ShopSphere Admin Portal</h1> <a href='/admin_login'>Login</a>"

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
