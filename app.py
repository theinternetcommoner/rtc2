from flask import Flask, render_template
from views.views import views
from reports.reports import reports
from admin.admin import admin
from models.modelref import *
from waitress import serve

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e8f5355b080e98f69deeddfcd117687a8b3b104ffbf78ca91fa433dc901c42aa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rtc_fc.db'

db.init_app(app)

app.register_blueprint(reports, url_prefix = "/reports")
app.register_blueprint(views, url_prefix = "/views")
app.register_blueprint(admin, url_prefix = "/admin")

@app.route('/')
def index():
	# remove 'user' from session
	# session.pop('usr', None)
	return render_template('index.html')

# for handling error 404
@app.errorhandler(404)
def err_404(error):
    return render_template('404.html')

dev_mode = True

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
		
	if dev_mode == True:
		# app.run(host = '0.0.0.0', port = 5001, debug = True)
		app.run(port = 5001, debug = True)
	else:
		# print('Service Started Successfully')
		serve(app, host = '0.0.0.0', port = 5001)


		# equivalent to 'from hello import app'
		# waitress-serve --host 127.0.0.1 hello:app

		# equivalent to 'from hello import create_app; create_app()'
		# waitress-serve --host 127.0.0.1 --call hello:create_app
		# waitress-serve --host 0.0.0.0 --port 5001 app:app
		# call waitress-serve --listen 0.0.0.0:5001 app:app
