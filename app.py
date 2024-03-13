from flask import Flask, render_template
from rtc import rtc_app
from waitress import serve

app = rtc_app()

@app.route('/')
def index():
	# remove 'user' from session
	# session.pop('usr', None)
	return render_template('index.html')

# for handling error 404
@app.errorhandler(404)
def err_404(error):
    return render_template('404.html')

dev_mode = False
if __name__ == '__main__':
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