from flask import Flask, request, render_template
from tracker import read_file, write_file

app = Flask(__name__)

# Route for the home page
@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

# Route for the "Want to Learn" page
@app.route('/want-to-learn.html', methods=["GET", "POST"])
def want_to_learn():
    # Read existing data from the file
    contents = read_file()

    if request.method == "POST":
        # Get form data
        title = request.form.get('title')
        link = request.form.get('link')
        delete = request.form.get('delete')

        if title is not None and delete is None:
            # Add new entry
            contents['want'].append([title, link])
            write_file(contents)
        elif delete is not None:
            # Delete selected entry
            contents['want'] = [item for item in contents['want'] if item[0] != delete]
            write_file(contents)

    # Render the template with the updated data
    return render_template('want-to-learn.html', pieces=contents['want'])

# Similar structure for the "Learned" and "Learning" pages...

# Route for the "Learned" page
@app.route('/learned.html', methods=["GET", "POST"])
def learned():
    contents = read_file()

    if request.method == "POST":
        title = request.form.get('title')
        link = request.form.get('link')
        delete = request.form.get('delete')

        if title is not None and delete is None:
            contents['learned'].append([title, link])
            write_file(contents)
        elif delete is not None:
            contents['learned'] = [item for item in contents['learned'] if item[0] != delete]
            write_file(contents)

    return render_template('learned.html', pieces=contents['learned'])

# Route for the "Learning" page
@app.route('/learning.html', methods=["GET", "POST"])
def learning():
    contents = read_file()

    if request.method == "POST":
        title = request.form.get('title')
        link = request.form.get('link')
        delete = request.form.get('delete')

        if title is not None and delete is None:
            contents['learning'].append([title, link])
            write_file(contents)
        elif delete is not None:
            contents['learning'] = [item for item in contents['learning'] if item[0] != delete]
            write_file(contents)

    return render_template('learning.html', pieces=contents['learning'])

# Route for the "Sight Speed" page
@app.route('/sight-speed.html', methods=["GET", "POST"])
def sight_speed():
    contents = read_file()

    if request.method == "POST":
        date = request.form.get('date')
        time = request.form.get('time')
        hits = request.form.get('hits')
        misses = request.form.get('misses')
        note_count = request.form.get('note-count')
        delete = request.form.get('delete')

        if hits is not None and delete is None:
            # Validate time format
            if ':' not in time:
                return render_template('sight-speed.html', pieces=contents['sight-speed'], message='Error: Invalid Time')
            
            # Calculate hits per minute
            hpm = time.split(':')
            hpm = float(hpm[0]) + float(hpm[1]) / 60
            hpm = float(hits) / hpm

            entry = {
                "time": time,
                "hits": hits,
                "misses": misses,
                "hpm": str(hpm),
                "note-count": note_count,
                "date": date
            }
            contents['sight-speed'].append(entry)
            write_file(contents)
        elif delete is not None:
            contents['sight-speed'] = [item for item in contents['sight-speed'] if str(item) != delete]
            write_file(contents)

    return render_template('sight-speed.html', pieces=contents['sight-speed'])

# Route for the "Scales Speed" page
@app.route('/scales-speed.html', methods=["GET", "POST"])
def scales_speed():
    contents = read_file()

    if request.method == "POST":
        date = request.form.get('date')
        time = request.form.get('time')
        cat = request.form.get('category')
        delete = request.form.get('delete')
        delete_cat = request.form.get('delete-cat')

        if time is not None and delete is None:
            # Validate time format
            if ':' not in time:
                return render_template('scales-speed.html', categories=contents['scale-speed'], message='Error: Invalid Time')

            entry = {
                "time": time,
                "date": date,
            }
            if cat in contents['scale-speed']:
                contents['scale-speed'][cat].append(entry)
                write_file(contents)
            else:
                contents['scale-speed'][cat] = [entry]
                write_file(contents)
        elif delete is not None:
            contents['scale-speed'][delete_cat] = [item for item in contents['scale-speed'][delete_cat] if str(item) != delete]
            if not contents['scale-speed'][delete_cat]:
                del contents['scale-speed'][delete_cat]
            write_file(contents)

    return render_template('scales-speed.html', categories=contents['scale-speed'])

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
