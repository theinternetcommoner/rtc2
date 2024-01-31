from flask import *
from waitress import serve
from views.views import views
from reports.reports import reports
from admin.admin import admin

app = Flask(__name__)
app.secret_key = 'nooneshouldknow'

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
	if dev_mode == True:
		# app.run(host = '0.0.0.0', port = 5001, debug = True)
		app.run(port = 5001, debug = True)
	else:
		serve(app, host = '0.0.0.0', port = 5001)