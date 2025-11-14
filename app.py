from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return '<h1>Hello from a PaaS Engine! JEEVASURYA :)</h1><p>My Python web application is live!</p>'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)