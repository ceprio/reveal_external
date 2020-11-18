import webbrowser
from flask import Flask
app = Flask(__name__, static_folder=".", static_url_path="")

index_file = "index.html"

@app.route('/')
def index():
        return app.send_static_file(index_file)

@app.route('/<path:path>')
def all_files(path):
    return app.send_static_file(path)

@app.route('/favicon.ico')
def ico_file():
    return "None"

if __name__ == '__main__':
    app.debug=True
    webbrowser.open("http://127.0.0.1:5000/" + index_file)
    app.run()