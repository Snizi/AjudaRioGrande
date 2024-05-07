from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    markers = json.load(open('markers.json' , encoding="utf8"))
    riskareas = json.load(open('riskareas.json' , encoding="utf8"))
    return render_template('index.html', markers=markers, riskareas=riskareas)

@app.route('/telefones')
def telefones():
    return render_template('telefones.html')

@app.route('/links-uteis')
def links_uteis():
    return render_template('links-uteis.html')
    
@app.route('/grupos')
def grupos():
    return render_template('grupos.html')

if __name__ == '__main__':
    app.run()