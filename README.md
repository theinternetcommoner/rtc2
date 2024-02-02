# RTC Br. 1 FC System

## compatibility
python 3.6 or higher
link: https://www.python.org/downloads/

## packages used
Flask
Waitress
*refer to requirements.txt for details

## commands used for this project:
pip install virtualenv
pip install flask
python -m pip install waitress

## for creating requirements.txt (includes everything)
pip freeze > requirements.txt

## for creating requirements.txt (includes only those that are in use)
pip install pipreqs
pipreqs or pipreqs --force to override existing file

## to install using requirements.txt
pip install -r requirements.txt

## references for further reading
flask link:
https://flask.palletsprojects.com/en/3.0.x/

waitress link:
https://flask.palletsprojects.com/en/3.0.x/deploying/waitress/
https://docs.pylonsproject.org/projects/waitress/en/stable/index.html
https://nagasudhir.blogspot.com/2022/10/waitress-as-flask-server-wsgi.html

*note:
-if pip install (package) is not working, please use python -m pip install (package)
-extract database file located at rtc/ directory (rtc_fc.rar)