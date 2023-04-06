from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    files = os.listdir()
    if len(files) == 0:
        return "No info ava."
    else:
        return "<br>".join(files)
index()
if __name__ == '__main__':
    app.run(debug=True)


