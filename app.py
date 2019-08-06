from flask import *


app = Flask(__name__)


@app.route("/")
def index():
	return render_template('coupons.html')

if __name__ == '__main__':
	app.run(debug=True)