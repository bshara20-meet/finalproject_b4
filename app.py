from flask import *


app = Flask(__name__)


@app.route("/")
def index():
	return render_template('copy.html')

@app.route("/coupons/")
def coupons():
	return render_template('coupons.html')
	
@app.route('/join-us/')
def join1():
	return render_template('join1.html')

if __name__ == '__main__':
	app.run(debug=True)