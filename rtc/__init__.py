from flask import Flask

def rtc_app():
	app = Flask(__name__)

	app.config['SECRET_KEY'] = 'nooneshouldknow'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rtc_fc.db'
	
	from rtc.views.views import views
	from rtc.reports.reports import reports
	from rtc.admin.admin import admin
	from models.modelref import *

	app.register_blueprint(reports, url_prefix = "/reports")
	app.register_blueprint(views, url_prefix = "/views")
	app.register_blueprint(admin, url_prefix = "/admin")

	return app