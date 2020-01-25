from flask import Flask, render_template, json

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/organizer')
def organizer():
    return render_template('organizer.html')

@app.route('/donar')
def doner():
    return render_template('donar.html')

@app.route('/children')
def children():
    return render_template('children.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/test')
def test():
    my_dict = {"title" : "Manager", "gener" : "Alternative"}
    return json.dumps(my_dict)
    

if __name__ == "__main__":
    print(" Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)")
    app.run(debug=True)