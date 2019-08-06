from flask import *


app = Flask(__name__)


@app.route("/")
def index():
	return render_template('copy.html')

@app.route("/coupons/")
def coupons():
	return render_template('coupons.html')

if __name__ == '__main__':
	app.run(debug=True)