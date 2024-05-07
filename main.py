from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    markers = json.load(open('markers.json'))
    riskareas = json.load(open('riskareas.json'))
    return render_template('index.html', markers=markers, riskareas=riskareas)

@app.route('/telefones')
def telefones():
    return render_template('telefones.html')
    
if __name__ == '__main__':
    app.run(debug=True)