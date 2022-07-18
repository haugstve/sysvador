import flask
app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'PLACEHOLDER_KEY'

print("Loading app")
