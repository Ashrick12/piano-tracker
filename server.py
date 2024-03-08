from flask import Flask, request, render_template
from tracker import read_file, write_file

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/want-to-learn.html', methods=["GET", "POST"])
def want_to_learn():
    contents = read_file()

    if request.method == "POST":
    
        title = request.form.get('title')
        link = request.form.get('link')
        delete = request.form.get('delete')

        if title != None and delete == None:
            contents['want'].append([title, link])
            write_file(contents)

        elif delete != None:
            contents['want'] = [item for item in contents['want'] if item[0] != delete]
            write_file(contents)

    return render_template('want-to-learn.html', pieces=contents['want'])

@app.route('/learned.html', methods=["GET", "POST"])
def learned():
    contents = read_file()

    if request.method == "POST":
        
        title = request.form.get('title')
        link = request.form.get('link')
        delete = request.form.get('delete')

        if title != None and delete == None:
            contents['learned'].append([title, link])
            write_file(contents)

        elif delete != None:
            contents['learned'] = [item for item in contents['learned'] if item[0] != delete]
            write_file(contents)

    return render_template('learned.html', pieces=contents['learned'])

@app.route('/learning.html', methods=["GET", "POST"])
def learning():
    contents = read_file()
    if request.method == "POST":
        
        title = request.form.get('title')
        link = request.form.get('link')
        delete = request.form.get('delete')

        if title != None and delete == None:
            contents['learning'].append([title, link])
            write_file(contents)

        elif delete != None:
            contents['learning'] = [item for item in contents['learning'] if item[0] != delete]
            write_file(contents)

    return render_template('learning.html', pieces=contents['learning'])

@app.route('/sight-speed.html', methods=["GET", "POST"])
def sight_speed():
    contents = read_file()
    return render_template('sight-speed.html', pieces=contents['sight-speed'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)