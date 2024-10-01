from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/about')
def about():
    return 'Hi THis is from About page'

@app.route('/contactus')
def about():
    return 'Hi THis is from contactus page'

if __name__ == '__main__':
    app.run(debug=True)