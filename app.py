# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/key_selection')
def key_selection():
    return render_template('key_selection.html')

@app.route('/expert')
def expert():
    return render_template('expert.html')

@app.route('/prices')
def prices():
    return render_template('prices.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/urgent_buyout')
def urgent_buyout():
    return render_template('urgent_buyout.html')

@app.route('/diagnostic')
def diagnostic():
    return render_template('diagnostic.html')

@app.route('/expert_on_duty')
def expert_on_duty():
    return render_template('expert_on_duty.html')

if __name__ == '__main__':
    app.run(debug=True)