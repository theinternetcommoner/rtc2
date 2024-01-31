from flask import *
import sqlite3 as db


views = Blueprint("views", __name__, static_folder = "static", template_folder = "templates")

def connection(database):
	global conn
	global cur
	conn = db.connect(database)
	conn.row_factory = db.Row
	cur = conn.cursor()

@views.route('/view_records')
def view_records():
	connection('./rtc_fc.db')

	query = conn.cursor()
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
	query.execute(sql)

	result = query.fetchall()
	return render_template('view_records.html', row = result)

@views.route('/profile/<string:id>')
def profile(id):
	connection('./rtc_fc.db')

	query = """
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
		FROM tbl_case_record WHERE case_id = ?
	"""
	cur.execute(query, (id,))

	rw = cur.fetchall()
	#for testing purposes
	# for x in rw:
	# 	# return x[0]+x[1]
	return render_template('profile.html', rows = rw)

@views.route('/search', methods = ['POST', 'GET'])
def searchrecord():
	if request.method == 'POST':
		connection('./rtc_fc.db')

		query = conn.cursor()
		searchVal = request.form['search']
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
			case_no LIKE ? OR
			case_title LIKE ? OR
			case_nature LIKE ? OR
			age LIKE ?
		"""
		query_inputs = ('%'+searchVal+'%', '%'+searchVal+'%', '%'+searchVal+'%', '%'+searchVal+'%')
		query.execute(sql, query_inputs)
		
		result = query.fetchall()
		return render_template('view_records.html', row = result)
	else:
		return render_template('view_records.html', row = result)

'''
--ageing query-
SELECT filing_date, date('now') as today,
CASE
	WHEN strftime('%m', date('now')) > strftime('%m', date(filing_date)) THEN strftime('%Y', date('now')) - strftime('%Y', date(filing_date))
	WHEN strftime('%m', date('now')) = strftime('%m', date(filing_date)) THEN
		CASE 
			WHEN strftime('%d', date('now')) >= strftime('%d', date(filing_date)) THEN strftime('%Y', date('now')) - strftime('%Y', date(filing_date))
			ELSE strftime('%Y', date('now')) - strftime('%Y', date(filing_date)) - 1
		END
	WHEN strftime('%m', date('now')) < strftime('%m', date(filing_date)) THEN strftime('%Y', date('now')) - strftime('%Y', date(filing_date)) - 1
END as age
FROM tbl_case_record
'''