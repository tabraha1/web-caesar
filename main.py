from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <form action="/encrypt" method="post">
        <label for="rot">Rotation</label>
        <input name="rot" type="text" value="0"/>
        <textarea name="text"></textarea>
        <input type="submit" />
    </form>
    </body>
</html>

"""

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = request.form['rot']
    rots = int(rot)
    words = rotate_string(text, rots)

    sentence = '<h1>' + words + '</h1>'
    return sentence


@app.route('/')
def index():
    return form

app.run()