from flask import Flask

def rtc_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'nooneshouldknow'
	
	from rtc.views.views import views
	from rtc.reports.reports import reports
	from rtc.admin.admin import admin

	app.register_blueprint(reports, url_prefix = "/reports")
	app.register_blueprint(views, url_prefix = "/views")
	app.register_blueprint(admin, url_prefix = "/admin")

	return app