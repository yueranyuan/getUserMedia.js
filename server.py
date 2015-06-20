from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_url_path='', static_folder='face-detection-demo')

@app.route('/')
def root():
    return render_template("cam.html")

@app.route('/lib/<filename>')
def lib_page(filename):
    return send_from_directory('lib', filename)

@app.route('/dist/fallback/<filename>')
def fallback(filename):
    return send_from_directory('dist/fallback', filename)

app.run(debug=True)
