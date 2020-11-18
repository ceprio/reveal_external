from flask import Flask
app = Flask(__name__, static_folder='.')

@app.route('/')
def example():
        return app.send_static_file('index.html')

@app.route('/<path:path>')
def all_files(path):
    try:
        return app.send_static_file(path)
    except NotFound:  # Not needed (from werkzeug.exceptions)
        abort(404) # from flask


if __name__ == '__main__':
    app.debug=True
    app.run()