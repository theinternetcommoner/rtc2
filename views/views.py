from flask import Blueprint, render_template, request
from models.modelref import *
from sqlalchemy import text

views = Blueprint("views", __name__, static_folder = "static", template_folder = "templates")

@views.route('/view_records')
def view_records():
	sql = """
		SELECT 
		*,
		CASE
			WHEN strftime('%m', date('now')) > strftime('%m', date(filing_date)) THEN strftime('%Y', date('now')) - strftime('%Y', date(filing_date))
			WHEN strftime('%m', date('now')) = strftime('%m', date(filing_date)) THEN
				CASE 
					WHEN strftime('%d', date('now')) >= strftime('%d', date(filing_date)) THEN strftime('%Y', date('now')) - strftime('%Y', date(filing_date))
					ELSE strftime('%Y', date('now')) - strftime('%Y', date(filing_date)) - 1
				END
			WHEN strftime('%m', date('now')) < strftime('%m', date(filing_date)) THEN strftime('%Y', date('now')) - strftime('%Y', date(filing_date)) - 1
		END as age
		FROM
		tbl_case_record
	"""
	query = text(sql)

	result = db.session.execute(query)
	rows = result.fetchall()

	return render_template('view_records.html', row = rows)

@views.route('/profile/<string:id>')
def profile(id):
	data = {'id': id,}
	sql = """
		SELECT 
		*, 
		CASE
			WHEN strftime('%m', date('now')) > strftime('%m', date(filing_date)) THEN strftime('%Y', date('now')) - strftime('%Y', date(filing_date))
			WHEN strftime('%m', date('now')) = strftime('%m', date(filing_date)) THEN
				CASE 
					WHEN strftime('%d', date('now')) >= strftime('%d', date(filing_date)) THEN strftime('%Y', date('now')) - strftime('%Y', date(filing_date))
					ELSE strftime('%Y', date('now')) - strftime('%Y', date(filing_date)) - 1
				END
			WHEN strftime('%m', date('now')) < strftime('%m', date(filing_date)) THEN strftime('%Y', date('now')) - strftime('%Y', date(filing_date)) - 1
		END as age
		FROM tbl_case_record WHERE case_id = :id
	"""
	query = text(sql)

	result = db.session.execute(query, data)
	rows = result.fetchall()

	return render_template('profile.html', row = rows)

@views.route('/search', methods = ['POST'])
def searchrecord():
	searchval = '%'+request.form['search']+'%'
	data = {
		'case_no': searchval,
		'case_title': searchval,
		'case_nature': searchval,
		'age': searchval,
	}

	sql = """
		SELECT *,
		CASE
			WHEN strftime('%m', date('now')) > strftime('%m', date(filing_date)) THEN strftime('%Y', date('now')) - strftime('%Y', date(filing_date))
			WHEN strftime('%m', date('now')) = strftime('%m', date(filing_date)) THEN
				CASE 
					WHEN strftime('%d', date('now')) >= strftime('%d', date(filing_date)) THEN strftime('%Y', date('now')) - strftime('%Y', date(filing_date))
					ELSE strftime('%Y', date('now')) - strftime('%Y', date(filing_date)) - 1
				END
			WHEN strftime('%m', date('now')) < strftime('%m', date(filing_date)) THEN strftime('%Y', date('now')) - strftime('%Y', date(filing_date)) - 1
		END as age 
		FROM tbl_case_record WHERE
		case_no LIKE :case_no OR
		case_title LIKE :case_title OR
		case_nature LIKE :case_nature OR
		age LIKE :age
	"""

	query = text(sql)

	result = db.session.execute(query, data)
	rows = result.fetchall()

	return render_template('view_records.html', row = rows)