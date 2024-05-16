from flask import Flask, Blueprint, render_template, session, redirect, url_for, request
from models.modelref import *
from functools import wraps
from sqlalchemy import text

admin = Blueprint("admin", __name__, static_folder = "static", template_folder = "templates")

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
			login = {
				'username': request.form.get('usr'),
				'password': request.form.get('pass'),
			}
			sql = """
				SELECT * FROM tbl_account 
				WHERE 
				username = :username AND password = :password
			"""
			query = text(sql)

			result = db.session.execute(query, login)

			rw = result.fetchall()
			for x in rw:
				x
			session['usr'] = x[1]
			# return session['usr']
			return redirect(url_for('admin.index'))
		except:
			return redirect(url_for('admin.loginPage'))
			# return '-1'
# 
@admin.route('/logout')
def logout():
	#remove 'user' from session
	session.pop('usr', None)
	return redirect(url_for('index'))
# end-login/logout

@admin.route('/')
def index():
	if 'usr' in session:
		return render_template('adminindex.html', user = session['usr'])
	return redirect(url_for('admin.loginPage'))

@admin.route('/all_records')
@login_required
def all_records():
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

	return render_template('all_records.html', row = rows)

@admin.route('/new')
@login_required
def new():
	return render_template('new.html')

# insert function
@admin.route('/insert', methods = ['POST'])
@login_required
def insertrecord():
	try:
		record = tbl_case_record(
			case_no = request.form['c_number'],
			case_title = request.form['c_title'],
			case_nature = request.form['c_nature'],
			filing_date = request.form['c_filed'],
			receiving_date = request.form['c_rcv'],
			warrant_date = request.form['c_woa'],
			detention_date = request.form['c_detain'],
			bail_date = request.form['c_bail'],
			archive_date = request.form['c_arch'],
			arraignment_date = request.form['c_arr'],
			pretrial_date = request.form['c_pt'],
			prosecution_evidence_date = request.form['c_proc'],
			defense_evidence_date = request.form['c_def'],
			submitted_for_decision_date = request.form['c_submit'],
			disposal_date = request.form['c_disposed'],
			promulgation_date = request.form['c_prom'],
			case_status = request.form['c_status'],
			case_category = request.form['c_category'],
			case_subcategory = request.form['c_subcategory'],
			disposal_type = '',
			logs = request.form['c_log']
		)

		db.session.add(record)
		db.session.commit()
		msg = 'Success!'
	except:
		db.session.rollback()
		msg = 'Failed!'
	finally:
		return render_template('result.html', message = msg)
# end of insert function

# select functions
@admin.route('/selectdate/<string:id>')
@login_required
def selectdate(id):
	model = tbl_case_record()
	data  = model.query.filter_by(case_id = id)
	return render_template('dateform.html', row = data)

@admin.route('/selectinfo/<string:id>')
@login_required
def selectinfo(id):
	model = tbl_case_record()
	data  = model.query.filter_by(case_id = id)
	return render_template('infoform.html', row = data)

@admin.route('/selectstatus/<string:id>')
@login_required
def selectstatus(id):
	model = tbl_case_record()
	data  = model.query.filter_by(case_id = id)
	return render_template('statsform.html', row = data)

@admin.route('/selectcategory/<string:id>')
@login_required
def selectcategory(id):
	model = tbl_case_record()
	data  = model.query.filter_by(case_id = id)
	return render_template('categoryform.html', row = data)

@admin.route('/selectsubcategory/<string:id>')
@login_required
def selectsubcategory(id):
	model = tbl_case_record()
	data  = model.query.filter_by(case_id = id)
	return render_template('subcategoryform.html', row = data)
# end of select functions

# update functions
@admin.route('/editdate/<string:id>',methods = ['POST'])
@login_required
def editdate(id):
	model = tbl_case_record()
	data  = model.query.filter_by(case_id = str(id)).first()

	try:
		data.filing_date = request.form['c_filed']
		data.receiving_date = request.form['c_rcv']
		data.warrant_date = request.form['c_woa']
		data.detention_date = request.form['c_detain']
		data.bail_date = request.form['c_bail']
		data.archive_date = request.form['c_arch']
		data.arraignment_date = request.form['c_arr']
		data.pretrial_date = request.form['c_pt']
		data.prosecution_evidence_date = request.form['c_proc']
		data.defense_evidence_date = request.form['c_def']
		data.submitted_for_decision_date = request.form['c_submit']
		data.disposal_date = request.form['c_disposed']
		data.promulgation_date = request.form['c_prom']

		db.session.commit()
		msg = 'Success'
	except:
		db.session.rollback()
		msg = 'Failed'
	finally:
		return render_template('result.html', message = msg)

@admin.route('/editinfo/<string:id>',methods = ['POST'])
@login_required
def editinfo(id):
	model = tbl_case_record()
	data  = model.query.filter_by(case_id = str(id)).first()

	try:
		data.case_no = request.form['c_number']
		data.case_title = request.form['c_title']
		data.case_nature = request.form['c_nature']
		data.logs = request.form['c_log']

		db.session.commit()
		msg = 'Success'
	except:
		db.session.rollback()
		msg = 'Failed'
	finally:
		return render_template('result.html', message = msg)

@admin.route('/editstatus/<string:id>',methods = ['POST'])
@login_required
def editstatus(id):
	model = tbl_case_record()
	data  = model.query.filter_by(case_id = str(id)).first()

	try:
		data.case_status = request.form['c_status']
		db.session.commit()
		msg = 'Success'
	except:
		db.session.rollback()
		msg = 'Failed'
	finally:
		return render_template('result.html', message = msg)

@admin.route('/editcategory/<string:id>',methods = ['POST'])
@login_required
def editcategory(id):
	model = tbl_case_record()
	data  = model.query.filter_by(case_id = str(id)).first()

	try:
		data.case_category = request.form['c_category']
		db.session.commit()
		msg = 'Success'
	except:
		db.session.rollback()
		msg = 'Failed'
	finally:
		return render_template('result.html', message = msg)

@admin.route('/editsubcategory/<string:id>',methods = ['POST'])
@login_required
def editsubcategory(id):
	model = tbl_case_record()
	data  = model.query.filter_by(case_id = str(id)).first()

	try:
		data.case_subcategory = request.form['c_subcategory']
		db.session.commit()
		msg = 'Success'
	except:
		db.session.rollback()
		msg = 'Failed'
	finally:
		return render_template('result.html', message = msg)
# end of update functions

# search function
@admin.route('/search', methods = ['POST'])
@login_required
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

	return render_template('all_records.html', row = rows)
# end of search function