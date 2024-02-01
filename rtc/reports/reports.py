from flask import Flask, Blueprint, render_template
import sqlite3 as db
from .queries import *

reports = Blueprint("reports", __name__, static_folder = "static", template_folder = "templates")

#################################################################################
#global functions
#################################################################################

def connection(database):
	global conn
	conn = db.connect(database)
	conn.row_factory = db.Row

def age_query(age): #for age 1-9 yrs
	global result
	query0 = conn.cursor()
	sql0 = select_age_case_status(2)

	query1 = conn.cursor()
	sql1 = select_age_case_status(5)

	query2 = conn.cursor()
	sql2 = select_age_case_status(6)

	query3 = conn.cursor()
	sql3 = select_age_case_status(7)

	query4 = conn.cursor()
	sql4 = select_age_case_status(8)

	query5 = conn.cursor()
	sql5 = select_age_case_status(11)

	query6 = conn.cursor()
	sql6 = select_age_case_status(12)

	age_var = (age,)

	query0.execute(sql0, age_var)
	query1.execute(sql1, age_var)
	query2.execute(sql2, age_var)
	query3.execute(sql3, age_var)
	query4.execute(sql4, age_var)
	query5.execute(sql5, age_var)
	query6.execute(sql6, age_var)

	result0 = query0.fetchall()
	result1 = query1.fetchall()
	result2 = query2.fetchall()
	result3 = query3.fetchall()
	result4 = query4.fetchall()
	result5 = query5.fetchall()
	result6 = query6.fetchall()

	result = result0 + result1 + result2 + result3 + result4 + result5 + result6

def age10_query(age): #for age 10 up
	global result
	query0 = conn.cursor()
	sql0 = select_age10_case_status(2)

	query1 = conn.cursor()
	sql1 = select_age10_case_status(5)

	query2 = conn.cursor()
	sql2 = select_age10_case_status(6)

	query3 = conn.cursor()
	sql3 = select_age10_case_status(7)

	query4 = conn.cursor()
	sql4 = select_age10_case_status(8)

	query5 = conn.cursor()
	sql5 = select_age10_case_status(11)

	query6 = conn.cursor()
	sql6 = select_age10_case_status(12)

	age_var = (age,)

	query0.execute(sql0, age_var)
	query1.execute(sql1, age_var)
	query2.execute(sql2, age_var)
	query3.execute(sql3, age_var)
	query4.execute(sql4, age_var)
	query5.execute(sql5, age_var)
	query6.execute(sql6, age_var)

	result0 = query0.fetchall()
	result1 = query1.fetchall()
	result2 = query2.fetchall()
	result3 = query3.fetchall()
	result4 = query4.fetchall()
	result5 = query5.fetchall()
	result6 = query6.fetchall()

	result = result0 + result1 + result2 + result3 + result4 + result5 + result6

def category_query(category):
	global result
	query0 = conn.cursor()
	sql0 = select_category_status(2)

	query1 = conn.cursor()
	sql1 = select_category_status(5)

	query2 = conn.cursor()
	sql2 = select_category_status(6)

	query3 = conn.cursor()
	sql3 = select_category_status(7)

	query4 = conn.cursor()
	sql4 = select_category_status(8)

	query5 = conn.cursor()
	sql5 = select_category_status(11)

	query6 = conn.cursor()
	sql6 = select_category_status(12)

	category_var = (category,)

	query0.execute(sql0, category_var)
	query1.execute(sql1, category_var)
	query2.execute(sql2, category_var)
	query3.execute(sql3, category_var)
	query4.execute(sql4, category_var)
	query5.execute(sql5, category_var)
	query6.execute(sql6, category_var)

	result0 = query0.fetchall()
	result1 = query1.fetchall()
	result2 = query2.fetchall()
	result3 = query3.fetchall()
	result4 = query4.fetchall()
	result5 = query5.fetchall()
	result6 = query6.fetchall()

	result = result0 + result1 + result2 + result3 + result4 + result5 + result6

def subcategory_query(subcategory):
	global result
	query0 = conn.cursor()
	sql0 = select_subcategory_status(2)

	query1 = conn.cursor()
	sql1 = select_subcategory_status(5)

	query2 = conn.cursor()
	sql2 = select_subcategory_status(6)

	query3 = conn.cursor()
	sql3 = select_subcategory_status(7)

	query4 = conn.cursor()
	sql4 = select_subcategory_status(8)

	query5 = conn.cursor()
	sql5 = select_subcategory_status(11)

	query6 = conn.cursor()
	sql6 = select_subcategory_status(12)

	subcategory_var = (subcategory,)

	query0.execute(sql0, subcategory_var)
	query1.execute(sql1, subcategory_var)
	query2.execute(sql2, subcategory_var)
	query3.execute(sql3, subcategory_var)
	query4.execute(sql4, subcategory_var)
	query5.execute(sql5, subcategory_var)
	query6.execute(sql6, subcategory_var)

	result0 = query0.fetchall()
	result1 = query1.fetchall()
	result2 = query2.fetchall()
	result3 = query3.fetchall()
	result4 = query4.fetchall()
	result5 = query5.fetchall()
	result6 = query6.fetchall()

	result = result0 + result1 + result2 + result3 + result4 + result5 + result6

def status_query(status):
	global result
	query = conn.cursor()
	sql = select_case_status(status)

	query.execute(sql)

	result = query.fetchall()

def count_category_query(category):

	global result0, result1, result2, result3, result4, result5, result6

	query0 = conn.cursor()
	sql0 = count_category_status(2)
	query0.execute(sql0, (category,))
	result0 = query0.fetchall()

	query1 = conn.cursor()
	sql1 = count_category_status(5)
	query1.execute(sql1, (category,))
	result1 = query1.fetchall()

	query2 = conn.cursor()
	sql2 = count_category_status(6)
	query2.execute(sql2, (category,))
	result2 = query2.fetchall()

	query3 = conn.cursor()
	sql3 = count_category_status(7)
	query3.execute(sql3, (category,))
	result3 = query3.fetchall()

	query4 = conn.cursor()
	sql4 = count_category_status(8)
	query4.execute(sql4, (category,))
	result4 = query4.fetchall()

	query5 = conn.cursor()
	sql5 = count_category_status(11)
	query5.execute(sql5, (category,))
	result5 = query5.fetchall()

	query6 = conn.cursor()
	sql6 = count_category_status(12)
	query6.execute(sql6, (category,))
	result6 = query6.fetchall()

#################################################################################
#end of global functions
#################################################################################

#################################################################################
#routes
#################################################################################

#counting by category
@reports.route('/count_civil')
def count_civil():
	connection('./rtc/rtc_fc.db')
	count_category_query(1)
	return render_template('report_civil_count.html', row0 = result0, row1 = result1, row2 = result2, row3 = result3, row4 = result4, row5 = result5, row6 = result6)

@reports.route('/count_criminal')
def count_criminal():
	connection('./rtc/rtc_fc.db')
	count_category_query(2)
	return render_template('report_criminal_count.html', row0 = result0, row1 = result1, row2 = result2, row3 = result3, row4 = result4, row5 = result5, row6 = result6)

@reports.route('/count_cicl')
def count_cicl():
	connection('./rtc/rtc_fc.db')
	count_category_query(3)
	return render_template('report_cicl_count.html', row0 = result0, row1 = result1, row2 = result2, row3 = result3, row4 = result4, row5 = result5, row6 = result6)

#displaying by category
@reports.route('/report_civil')
def report_civil():
	connection('./rtc/rtc_fc.db')
	category_query(1)
	return render_template('report_civil.html', row = result)

@reports.route('/report_criminal')
def report_criminal():
	connection('./rtc/rtc_fc.db')
	category_query(2)
	return render_template('report_criminal.html', row = result)

@reports.route('/report_cicl')
def report_cicl():
	connection('./rtc/rtc_fc.db')
	category_query(3)
	return render_template('report_cicl.html', row = result)

#displaying by subcategory
@reports.route('/report_9262')
def report_9262():
	connection('./rtc/rtc_fc.db')
	subcategory_query(1)
	return render_template('report_9262.html', row = result)

@reports.route('/report_9165')
def report_9165():
	connection('./rtc/rtc_fc.db')
	subcategory_query(2)
	return render_template('report_9165.html', row = result)

@reports.route('/report_rape')
def report_rape():
	connection('./rtc/rtc_fc.db')
	subcategory_query(3)
	return render_template('report_rape.html', row = result)

@reports.route('/report_7610')
def report_7610():
	connection('./rtc/rtc_fc.db')
	subcategory_query(4)
	return render_template('report_7610.html', row = result)

@reports.route('/report_9208')
def report_9208():
	connection('./rtc/rtc_fc.db')
	subcategory_query(5)
	return render_template('report_9208.html', row = result)

@reports.route('/report_othercriminal')
def report_othercriminal():
	connection('./rtc/rtc_fc.db')
	subcategory_query(6)
	return render_template('report_othercriminal.html', row = result)

@reports.route('/report_annulment')
def report_annulment():
	connection('./rtc/rtc_fc.db')
	subcategory_query(7)
	return render_template('report_annulment.html', row = result)

@reports.route('/report_legal')
def report_legal():
	connection('./rtc/rtc_fc.db')
	subcategory_query(8)
	return render_template('report_legalseparation.html', row = result)

@reports.route('/report_adoption')
def report_adoption():
	connection('./rtc/rtc_fc.db')
	subcategory_query(9)
	return render_template('report_adoption.html', row = result)

@reports.route('/report_protection')
def report_protection():
	connection('./rtc/rtc_fc.db')
	subcategory_query(10)
	return render_template('report_protection.html', row = result)

@reports.route('/report_guardianship')
def report_guardianship():
	connection('./rtc/rtc_fc.db')
	subcategory_query(11)
	return render_template('report_guardianship.html', row = result)

@reports.route('/report_custody')
def report_custody():
	connection('./rtc/rtc_fc.db')
	subcategory_query(12)
	return render_template('report_custody.html', row = result)

@reports.route('/report_othercivil')
def report_othercivil():
	connection('./rtc/rtc_fc.db')
	subcategory_query(13)
	return render_template('report_othercivil.html', row = result)

#displaying by ageing
@reports.route('/report_ageing_0year')
def report_ageing_0year():
	connection('./rtc/rtc_fc.db')
	age_query(0)
	return render_template('report_ageing_0year.html', row = result)

@reports.route('/report_ageing_1year')
def report_ageing_1year():
	connection('./rtc/rtc_fc.db')
	age_query(1)
	return render_template('report_ageing_1year.html', row = result)

@reports.route('/report_ageing_2years')
def report_ageing_2years():
	connection('./rtc/rtc_fc.db')
	age_query(2)
	return render_template('report_ageing_2years.html', row = result)

@reports.route('/report_ageing_3years')
def report_ageing_3years():
	connection('./rtc/rtc_fc.db')
	age_query(3)
	return render_template('report_ageing_3years.html', row = result)

@reports.route('/report_ageing_4years')
def report_ageing_4years():
	connection('./rtc/rtc_fc.db')
	age_query(4)
	return render_template('report_ageing_4years.html', row = result)

@reports.route('/report_ageing_5years')
def report_ageing_5years():
	connection('./rtc/rtc_fc.db')
	age_query(5)
	return render_template('report_ageing_5years.html', row = result)

@reports.route('/report_ageing_6years')
def report_ageing_6years():
	connection('./rtc/rtc_fc.db')
	age_query(6)
	return render_template('report_ageing_6years.html', row = result)

@reports.route('/report_ageing_7years')
def report_ageing_7years():
	connection('./rtc/rtc_fc.db')
	age_query(7)
	return render_template('report_ageing_7years.html', row = result)

@reports.route('/report_ageing_8years')
def report_ageing_8years():
	connection('./rtc/rtc_fc.db')
	age_query(8)
	return render_template('report_ageing_8years.html', row = result)

@reports.route('/report_ageing_9years')
def report_ageing_9years():
	connection('./rtc/rtc_fc.db')
	age_query(9)
	return render_template('report_ageing_9years.html', row = result)

@reports.route('/report_ageing_10years_up')
def report_ageing_10years_up():
	connection('./rtc/rtc_fc.db')
	age10_query(9)
	return render_template('report_ageing_10years_up.html', row = result)

#displaying by status
@reports.route('/report_archived')
def report_archived():
	connection('./rtc/rtc_fc.db')
	status_query(1)
	return render_template('report_archived.html', row = result)

@reports.route('/report_arraignment')
def report_arraignment():
	connection('./rtc/rtc_fc.db')
	status_query(2)
	return render_template('report_arraignment.html', row = result)

@reports.route('/report_decided')
def report_decided():
	connection('./rtc/rtc_fc.db')
	status_query(3)
	return render_template('report_decided.html', row = result)

@reports.route('/report_dismissed')
def report_dismissed():
	connection('./rtc/rtc_fc.db')
	status_query(4)
	return render_template('report_dismissed.html', row = result)

@reports.route('/report_mediation')
def report_mediation():
	connection('./rtc/rtc_fc.db')
	status_query(5)
	return render_template('report_mediation.html', row = result)

@reports.route('/report_new')
def report_new():
	connection('./rtc/rtc_fc.db')
	status_query(6)
	return render_template('report_new.html', row = result)

@reports.route('/report_defense')
def report_defense():
	connection('./rtc/rtc_fc.db')
	status_query(7)
	return render_template('report_defense.html', row = result)

@reports.route('/report_prosecution')
def report_prosecution():
	connection('./rtc/rtc_fc.db')
	status_query(8)
	return render_template('report_prosecution.html', row = result)

@reports.route('/report_probation')
def report_probation():
	connection('./rtc/rtc_fc.db')
	status_query(9)
	return render_template('report_probation.html', row = result)

@reports.route('/report_provisional')
def report_provisional():
	connection('./rtc/rtc_fc.db')
	status_query(10)
	return render_template('report_provisional.html', row = result)

@reports.route('/report_submitted')
def report_submitted():
	connection('./rtc/rtc_fc.db')
	status_query(11)
	return render_template('report_submitted.html', row = result)

@reports.route('/report_susproc')
def report_susproc():
	connection('./rtc/rtc_fc.db')
	status_query(12)
	return render_template('report_susproc.html', row = result)

@reports.route('/report_susjudge')
def report_susjudge():
	connection('./rtc/rtc_fc.db')
	status_query(13)
	return render_template('report_susjudge.html', row = result)
#################################################################################
#end of routes
#################################################################################