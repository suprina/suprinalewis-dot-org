from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/question', methods=['GET', 'POST'])
def hello():
    """Return a friendly HTTP greeting."""
    if request.method == 'POST':
        return "No {}".format(request.form.get("myname"))
    return "<form id='myform' method='POST'><input name='myname'/></form>"

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
