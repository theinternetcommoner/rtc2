from flask import *
from functools import wraps
import sqlite3 as db

admin = Blueprint("admin", __name__, static_folder = "static", template_folder = "templates")

# database connection, set to global
def connection(database):
	global conn
	global cur
	conn = db.connect(database)
	conn.row_factory = db.Row
	cur = conn.cursor()

# login/logout function
def login_required(f):
	@wraps(f)
	def _login_required(*args, **kwargs):
		if session.get('usr'):
			return f(*args, **kwargs)
		else:
			return redirect(url_for('admin.loginPage'))
	return _login_required

@admin.route('/login')
def loginPage():
	return render_template('login.html')

@admin.route('/logincheck', methods = ['GET', 'POST'])
def logincheck():
	if request.method == 'POST':
		try:
			conn = db.connect('./rtc_fc.db')
			cur = conn.cursor()

			stmt = """
				SELECT * FROM tbl_account WHERE username = ? AND password = ?
			"""
			cur.execute(stmt, (request.form['usr'], request.form['pass']))

			rw = cur.fetchall()
			for x in rw:
				x
			session['usr'] = x[1]
			# return session['usr']
			return redirect(url_for('admin.index'))
		except:
			return redirect(url_for('admin.loginPage'))
			# return '-1'

@admin.route('/logout')
def logout():
	#remove 'user' from session
	session.pop('usr', None)
	return redirect(url_for('index'))
# end-login/logout

@admin.route('/')
def index():
	if 'usr' in session:
		return render_template('adminindex.html')
	return redirect(url_for('admin.loginPage'))

@admin.route('/all_records')
@login_required
def all_records():
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
	return render_template('all_records.html', row = result)

@admin.route('/new')
@login_required
def new():
	return render_template('new.html')

@admin.route('/insert', methods = ['GET', 'POST'])
@login_required
def insertrecord():
	if request.method == 'POST':
		try:
			with db.connect('./rtc_fc.db') as conn:
				cur = conn.cursor()

				case_no = request.form['c_number']
				case_title = request.form['c_title']
				case_nature = request.form['c_nature']
				filing_date = request.form['c_filed']
				receiving_date = request.form['c_rcv']
				warrant_date = request.form['c_woa']
				detention_date = request.form['c_detain']
				bail_date = request.form['c_bail']
				archive_date = request.form['c_arch']
				arraignment_date = request.form['c_arr']
				pretrial_date = request.form['c_pt']
				prosecution_evidence_date = request.form['c_proc']
				defense_evidence_date = request.form['c_def']
				submitted_for_decision_date = request.form['c_submit']
				disposal_date = request.form['c_disposed']
				promulgation_date = request.form['c_prom']
				case_status = request.form['c_status']
				case_category = request.form['c_category']
				case_subcategory = request.form['c_subcategory']
				disposal_type = ''
				logs = request.form['c_log']

				record_inputs = (
						case_no, 
						case_title, 
						case_nature,
						filing_date, 
						receiving_date, 
						warrant_date, 
						detention_date, 
						bail_date, 
						archive_date, 
						arraignment_date, 
						pretrial_date, 
						prosecution_evidence_date,
						defense_evidence_date,
						submitted_for_decision_date, 
						disposal_date, 
						promulgation_date,
						case_status,
						case_category,
						case_subcategory,
						disposal_type,
						logs
					)

				tbl_case_record_query = """
					INSERT INTO tbl_case_record(
						case_no, 
						case_title, 
						case_nature,
						filing_date, 
						receiving_date, 
						warrant_date, 
						detention_date, 
						bail_date, 
						archive_date, 
						arraignment_date, 
						pretrial_date, 
						prosecution_evidence_date,
						defense_evidence_date,
						submitted_for_decision_date, 
						disposal_date, 
						promulgation_date,
						case_status,
						case_category,
						case_subcategory,
						disposal_type,
						logs
					)
					VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
				"""
				cur.execute(tbl_case_record_query, record_inputs)
				conn.commit()
				msg = 'Success!'
		except:
			conn.rollback()
			msg = 'Failed'
		finally:
			return render_template('result.html', message = msg)
			conn.close()

# @admin.route('/profile/<string:id>')
# def profile(id):
# 	connection('./rtc_fc.db')

# 	query = """
# 		SELECT 
# 		*, 
# 		date('now') - filing_date as age 
# 		FROM 
# 		tbl_case_record 
# 		WHERE 
# 		case_id = ?
# 	"""
# 	cur.execute(query, (id,))

# 	rw = cur.fetchall()
# 	#for testing purposes
# 	# for x in rw:
# 	# 	# return x[0]+x[1]
# 	return render_template('profile.html', rows = rw)

@admin.route('/selectdate/<string:id>')
@login_required
def selectdate(id):
	connection('./rtc_fc.db')

	query = """
		SELECT * FROM tbl_case_record WHERE case_id = ?
	"""
	cur.execute(query, (id,))

	rw = cur.fetchall()
	#for testing purposes
	# for x in rw:
	# 	# return x[0]+x[1]
	return render_template('dateform.html', rows = rw)

@admin.route('/selectinfo/<string:id>')
@login_required
def selectinfo(id):
	connection('./rtc_fc.db')

	query = """
		SELECT * FROM tbl_case_record WHERE case_id = ?
	"""
	cur.execute(query, (id,))

	rw = cur.fetchall()
	#for testing purposes
	# for x in rw:
	# 	# return x[0]+x[1]
	return render_template('infoform.html', rows = rw)

@admin.route('/selectstatus/<string:id>')
@login_required
def selectstatus(id):
	connection('./rtc_fc.db')

	query = """
		SELECT * FROM tbl_case_record WHERE case_id = ?
	"""
	cur.execute(query, (id,))

	rw = cur.fetchall()
	return render_template('statsform.html', rows = rw)

@admin.route('/selectcategory/<string:id>')
@login_required
def selectcategory(id):
	connection('./rtc_fc.db')

	query = """
		SELECT * FROM tbl_case_record WHERE case_id = ?
	"""
	cur.execute(query, (id,))

	rw = cur.fetchall()
	#for testing purposes
	# for x in rw:
	# 	# return x[0]+x[1]
	return render_template('categoryform.html', rows = rw)

@admin.route('/selectsubcategory/<string:id>')
@login_required
def selectsubcategory(id):
	connection('./rtc_fc.db')

	query = """
		SELECT * FROM tbl_case_record WHERE case_id = ?
	"""
	cur.execute(query, (id,))

	rw = cur.fetchall()
	#for testing purposes
	# for x in rw:
	# 	# return x[0]+x[1]
	return render_template('subcategoryform.html', rows = rw)

@admin.route('/editdate',methods = ['POST', 'GET'])
@login_required
def editdate():
	if request.method == 'POST':
		try:
			filing_date = request.form['c_filed']
			receiving_date = request.form['c_rcv']
			warrant_date = request.form['c_woa']
			detention_date = request.form['c_detain']
			bail_date = request.form['c_bail']
			archive_date = request.form['c_arch']
			arraignment_date = request.form['c_arr']
			pretrial_date = request.form['c_pt']
			prosecution_evidence_date = request.form['c_proc']
			defense_evidence_date = request.form['c_def']
			submitted_for_decision_date = request.form['c_submit']
			disposal_date = request.form['c_disposed']
			promulgation_date = request.form['c_prom']
			case_id = request.form['id']

			list_dates = (
				filing_date, 
				receiving_date, 
				warrant_date, 
				detention_date, 
				bail_date, 
				archive_date, 
				arraignment_date, 
				pretrial_date, 
				prosecution_evidence_date,
				defense_evidence_date,
				submitted_for_decision_date, 
				disposal_date, 
				promulgation_date,
				case_id
			)
			with db.connect('./rtc_fc.db') as conn:
				cur = conn.cursor()

				query = """
					UPDATE tbl_case_record SET
					filing_date = ?, 
					receiving_date = ?, 
					warrant_date = ?, 
					detention_date = ?, 
					bail_date = ?, 
					archive_date = ?, 
					arraignment_date = ?, 
					pretrial_date = ?,
					prosecution_evidence_date = ?,
					defense_evidence_date = ?, 
					submitted_for_decision_date = ?, 
					disposal_date = ?, 
					promulgation_date = ?
					WHERE case_id = ?
				"""
				cur.execute(query, list_dates)
				conn.commit()
				msg = 'Success'
		except:
			conn.rollback()
			msg = 'Failed'
		finally:
			return render_template('result.html', message = msg)
			conn.close()

@admin.route('/editinfo',methods = ['POST', 'GET'])
@login_required
def editinfo():
	if request.method == 'POST':
		try:
			case_no = request.form['c_number']
			case_title = request.form['c_title']
			case_nature = request.form['c_nature']
			logs = request.form['c_log']
			case_id = request.form['id']

			list_info = (
				case_no, 
				case_title, 
				case_nature,
				logs,
				case_id
			)
			with db.connect('./rtc_fc.db') as conn:
				cur = conn.cursor()

				query = """
					UPDATE tbl_case_record SET
					case_no = ?, 
					case_title = ?, 
					case_nature = ?,
					logs = ?
					WHERE case_id = ?
				"""
				cur.execute(query, list_info)
				conn.commit()
				msg = 'Success'
		except:
			conn.rollback()
			msg = 'Failed'
		finally:
			return render_template('result.html', message = msg)
			conn.close()

@admin.route('/editstatus',methods = ['POST', 'GET'])
@login_required
def editstatus():
	if request.method == 'POST':
		try:
			case_status = request.form['c_status']
			case_id = request.form['id']

			list_status = (
				case_status,
				case_id
			)

			with db.connect('./rtc_fc.db') as conn:
				cur = conn.cursor()

				query = """
					UPDATE tbl_case_record SET case_status = ? WHERE case_id = ?
				"""
				cur.execute(query, list_status)
				conn.commit()
				msg = 'Success'
		except:
			conn.rollback()
			msg = 'Failed'
		finally:
			return render_template('result.html', message = msg)
			conn.close()

@admin.route('/editcategory',methods = ['POST', 'GET'])
@login_required
def editcategory():
	if request.method == 'POST':
		try:
			case_category = request.form['c_category']
			case_id = request.form['id']

			list_category = (
				case_category,
				case_id
			)

			with db.connect('./rtc_fc.db') as conn:
				cur = conn.cursor()

				query = """
					UPDATE tbl_case_record SET case_category = ? WHERE case_id = ?
				"""
				cur.execute(query, list_category)
				conn.commit()
				msg = 'Success'
		except:
			conn.rollback()
			msg = 'Failed'
		finally:
			return render_template('result.html', message = msg)
			conn.close()

@admin.route('/editsubcategory',methods = ['POST', 'GET'])
@login_required
def editsubcategory():
	if request.method == 'POST':
		try:
			case_subcategory = request.form['c_subcategory']
			case_id = request.form['id']

			list_subcategory = (
				case_subcategory,
				case_id
			)

			with db.connect('./rtc_fc.db') as conn:
				cur = conn.cursor()

				query = """
					UPDATE tbl_case_record SET case_subcategory = ? WHERE case_id = ?
				"""
				cur.execute(query, list_subcategory)
				conn.commit()
				msg = 'Success'
		except:
			conn.rollback()
			msg = 'Failed'
		finally:
			return render_template('result.html', message = msg)
			conn.close()

@admin.route('/search', methods = ['POST', 'GET'])
@login_required
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
		return render_template('all_records.html', row = result)
	else:
		return render_template('all_records.html', row = result)