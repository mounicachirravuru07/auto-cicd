#push
from flask import Flask, render_template_string
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    # """Return a friendly HTTP greeting."""
    # return 'HELLo WORLD!'
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                background: url('https://placekitten.com/1200/800') center center fixed;
                background-size: cover;
            }
            .container {
                padding: 20px;
                border: 2px solid #0073e6;
                border-radius: 10px;
                background-color: #ffcc00;
                text-align: center;
                color: #0073e6;
            }
            h1 {
                margin: 0;
                font-size: 36px;
                font-weight: bold;
            }
        </style>
        <title>Hello World</title>
    </head>
    <body>
        <div class="container">
            <h1>Hello World</h1>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/bob')
def bob():
    val = {"value": "bob"}
    return jsonify(val)

@app.route('/mounica')
def mounica():
    val = {"value": "mounica"}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)