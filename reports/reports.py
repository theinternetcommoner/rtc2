from flask import Blueprint, render_template, request
from models.modelref import *
from .queries import *
from sqlalchemy import text

reports = Blueprint("reports", __name__, static_folder = "static", template_folder = "templates")

#################################################################################
#routes
#################################################################################

#counting by category
@reports.route('/count_civil')
def count_civil():
    # case_status 2, 5, 6, 7, 8, 11, 12
    # case_category 1

    sql1 = count_case(2, 1)
    query1 = text(sql1)

    result1 = db.session.execute(query1)
    rows1 = result1.fetchall()

    sql2 = count_case(5, 1)
    query2 = text(sql2)

    result2 = db.session.execute(query2)
    rows2 = result2.fetchall()

    sql3 = count_case(6, 1)
    query3 = text(sql3)

    result3 = db.session.execute(query3)
    rows3 = result3.fetchall()

    sql4 = count_case(7, 1)
    query4 = text(sql4)

    result4 = db.session.execute(query4)
    rows4 = result4.fetchall()

    sql5 = count_case(8, 1)
    query5 = text(sql5)

    result5 = db.session.execute(query5)
    rows5 = result5.fetchall()

    sql6 = count_case(11, 1)
    query6 = text(sql6)

    result6 = db.session.execute(query6)
    rows6 = result6.fetchall()

    sql7 = count_case(12, 1)
    query7 = text(sql7)

    result7 = db.session.execute(query7)
    rows7 = result7.fetchall()

    return render_template(
            'report_civil_count.html', 
            row0 = rows1,
            row1 = rows2,
            row2 = rows3,
            row3 = rows4,
            row4 = rows5,
            row5 = rows6,
            row6 = rows7
        )

@reports.route('/count_criminal')
def count_criminal():
	# case_status 2, 5, 6, 7, 8, 11, 12
    # case_category 2

    sql1 = count_case(2, 2)
    query1 = text(sql1)

    result1 = db.session.execute(query1)
    rows1 = result1.fetchall()

    sql2 = count_case(5, 2)
    query2 = text(sql2)

    result2 = db.session.execute(query2)
    rows2 = result2.fetchall()

    sql3 = count_case(6, 2)
    query3 = text(sql3)

    result3 = db.session.execute(query3)
    rows3 = result3.fetchall()

    sql4 = count_case(7, 2)
    query4 = text(sql4)

    result4 = db.session.execute(query4)
    rows4 = result4.fetchall()

    sql5 = count_case(8, 2)
    query5 = text(sql5)

    result5 = db.session.execute(query5)
    rows5 = result5.fetchall()

    sql6 = count_case(11, 2)
    query6 = text(sql6)

    result6 = db.session.execute(query6)
    rows6 = result6.fetchall()

    sql7 = count_case(12, 2)
    query7 = text(sql7)

    result7 = db.session.execute(query7)
    rows7 = result7.fetchall()

    return render_template(
            'report_criminal_count.html', 
            row0 = rows1,
            row1 = rows2,
            row2 = rows3,
            row3 = rows4,
            row4 = rows5,
            row5 = rows6,
            row6 = rows7
        )

@reports.route('/count_cicl')
def count_cicl():
	# case_status 2, 5, 6, 7, 8, 11, 12
    # case_category 3

    sql1 = count_case(2, 3)
    query1 = text(sql1)

    result1 = db.session.execute(query1)
    rows1 = result1.fetchall()

    sql2 = count_case(5, 3)
    query2 = text(sql2)

    result2 = db.session.execute(query2)
    rows2 = result2.fetchall()

    sql3 = count_case(6, 3)
    query3 = text(sql3)

    result3 = db.session.execute(query3)
    rows3 = result3.fetchall()

    sql4 = count_case(7, 3)
    query4 = text(sql4)

    result4 = db.session.execute(query4)
    rows4 = result4.fetchall()

    sql5 = count_case(8, 3)
    query5 = text(sql5)

    result5 = db.session.execute(query5)
    rows5 = result5.fetchall()

    sql6 = count_case(11, 3)
    query6 = text(sql6)

    result6 = db.session.execute(query6)
    rows6 = result6.fetchall()

    sql7 = count_case(12, 3)
    query7 = text(sql7)

    result7 = db.session.execute(query7)
    rows7 = result7.fetchall()

    return render_template(
            'report_cicl_count.html', 
            row0 = rows1,
            row1 = rows2,
            row2 = rows3,
            row3 = rows4,
            row4 = rows5,
            row5 = rows6,
            row6 = rows7
        )

#displaying by category
@reports.route('/report_civil')
def report_civil():
	sql1 = case_category(2, 1)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_category(5, 1)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_category(6, 1)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_category(7, 1)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_category(8, 1)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_category(11, 1)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_category(12, 1)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_civil.html', row = result)

@reports.route('/report_criminal')
def report_criminal():
	sql1 = case_category(2, 2)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_category(5, 2)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_category(6, 2)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_category(7, 2)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_category(8, 2)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_category(11, 2)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_category(12, 2)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_criminal.html', row = result)

@reports.route('/report_cicl')
def report_cicl():
	sql1 = case_category(2, 3)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_category(5, 3)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_category(6, 3)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_category(7, 3)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_category(8, 3)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_category(11, 3)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_category(12, 3)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_cicl.html', row = result)

#displaying by subcategory
@reports.route('/report_9262')
def report_9262():
	sql1 = case_subcategory(2, 1)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 1)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 1)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 1)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 1)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 1)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 1)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7
	
	return render_template('report_9262.html', row = result)

@reports.route('/report_9165')
def report_9165():
	sql1 = case_subcategory(2, 2)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 2)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 2)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 2)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 2)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 2)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 2)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_9165.html', row = result)

@reports.route('/report_rape')
def report_rape():
	sql1 = case_subcategory(2, 3)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 3)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 3)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 3)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 3)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 3)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 3)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_rape.html', row = result)

@reports.route('/report_7610')
def report_7610():
	sql1 = case_subcategory(2, 4)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 4)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 4)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 4)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 4)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 4)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 4)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_7610.html', row = result)

@reports.route('/report_9208')
def report_9208():
	sql1 = case_subcategory(2, 5)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 5)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 5)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 5)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 5)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 5)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 5)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7
	return render_template('report_9208.html', row = result)

@reports.route('/report_othercriminal')
def report_othercriminal():
	sql1 = case_subcategory(2, 6)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 6)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 6)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 6)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 6)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 6)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 6)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_othercriminal.html', row = result)

@reports.route('/report_annulment')
def report_annulment():
	sql1 = case_subcategory(2, 7)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 7)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 7)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 7)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 7)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 7)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 7)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_annulment.html', row = result)

@reports.route('/report_legal')
def report_legal():
	sql1 = case_subcategory(2, 8)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 8)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 8)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 8)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 8)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 8)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 8)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_legalseparation.html', row = result)

@reports.route('/report_adoption')
def report_adoption():
	sql1 = case_subcategory(2, 9)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 9)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 9)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 9)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 9)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 9)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 9)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_adoption.html', row = result)

@reports.route('/report_protection')
def report_protection():
	sql1 = case_subcategory(2, 10)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 10)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 10)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 10)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 10)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 10)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 10)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_protection.html', row = result)

@reports.route('/report_guardianship')
def report_guardianship():
	sql1 = case_subcategory(2, 11)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 11)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 11)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 11)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 11)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 11)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 11)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_guardianship.html', row = result)

@reports.route('/report_custody')
def report_custody():
	sql1 = case_subcategory(2, 12)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 12)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 12)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 12)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 12)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 12)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 12)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_custody.html', row = result)

@reports.route('/report_othercivil')
def report_othercivil():
	sql1 = case_subcategory(2, 13)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_subcategory(5, 13)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_subcategory(6, 13)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_subcategory(7, 13)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_subcategory(8, 13)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_subcategory(11, 13)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_subcategory(12, 13)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_othercivil.html', row = result)

#displaying by ageing
#######################################################
#######################################################
#######################################################
@reports.route('/report_ageing_0year')
def report_ageing_0year():
	sql1 = case_age(2, 0)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_age(5, 0)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_age(6, 0)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_age(7, 0)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_age(8, 0)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_age(11, 0)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_age(12, 0)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_ageing_0year.html', row = result)

@reports.route('/report_ageing_1year')
def report_ageing_1year():
	sql1 = case_age(2, 1)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_age(5, 1)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_age(6, 1)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_age(7, 1)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_age(8, 1)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_age(11, 1)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_age(12, 1)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_ageing_1year.html', row = result)

@reports.route('/report_ageing_2years')
def report_ageing_2years():
	sql1 = case_age(2, 2)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_age(5, 2)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_age(6, 2)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_age(7, 2)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_age(8, 2)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_age(11, 2)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_age(12, 2)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_ageing_2years.html', row = result)

@reports.route('/report_ageing_3years')
def report_ageing_3years():
	sql1 = case_age(2, 3)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_age(5, 3)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_age(6, 3)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_age(7, 3)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_age(8, 3)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_age(11, 3)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_age(12, 3)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_ageing_3years.html', row = result)

@reports.route('/report_ageing_4years')
def report_ageing_4years():
	sql1 = case_age(2, 4)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_age(5, 4)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_age(6, 4)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_age(7, 4)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_age(8, 4)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_age(11, 4)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_age(12, 4)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_ageing_4years.html', row = result)

@reports.route('/report_ageing_5years')
def report_ageing_5years():
	sql1 = case_age(2, 5)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_age(5, 5)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_age(6, 5)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_age(7, 5)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_age(8, 5)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_age(11, 5)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_age(12, 5)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_ageing_5years.html', row = result)

@reports.route('/report_ageing_6years')
def report_ageing_6years():
	sql1 = case_age(2, 6)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_age(5, 6)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_age(6, 6)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_age(7, 6)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_age(8, 6)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_age(11, 6)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_age(12, 6)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_ageing_6years.html', row = result)

@reports.route('/report_ageing_7years')
def report_ageing_7years():
	sql1 = case_age(2, 7)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_age(5, 7)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_age(6, 7)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_age(7, 7)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_age(8, 7)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_age(11, 7)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_age(12, 7)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_ageing_7years.html', row = result)

@reports.route('/report_ageing_8years')
def report_ageing_8years():
	sql1 = case_age(2, 8)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_age(5, 8)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_age(6, 8)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_age(7, 8)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_age(8, 8)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_age(11, 8)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_age(12, 8)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_ageing_8years.html', row = result)

@reports.route('/report_ageing_9years')
def report_ageing_9years():
	sql1 = case_age(2, 9)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_age(5, 9)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_age(6, 9)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_age(7, 9)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_age(8, 9)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_age(11, 9)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_age(12, 9)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_ageing_9years.html', row = result)

@reports.route('/report_ageing_10years_up')
def report_ageing_10years_up():
	sql1 = case_age10(2, 9)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = case_age10(5, 9)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = case_age10(6, 9)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = case_age10(7, 9)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = case_age10(8, 9)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = case_age10(11, 9)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = case_age10(12, 9)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('report_ageing_10years_up.html', row = result)
#######################################################
#######################################################
#######################################################

#displaying by status
@reports.route('/report_archived')
def report_archived():
	sql = case_status(1)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_archived.html', row = result)

@reports.route('/report_arraignment')
def report_arraignment():
	sql = case_status(2)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_arraignment.html', row = result)

@reports.route('/report_decided')
def report_decided():
	sql = case_status(3)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_decided.html', row = result)

@reports.route('/report_dismissed')
def report_dismissed():
	sql = case_status(4)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_dismissed.html', row = result)

@reports.route('/report_mediation')
def report_mediation():
	sql = case_status(5)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_mediation.html', row = result)

@reports.route('/report_new')
def report_new():
	sql = case_status(6)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_new.html', row = result)

@reports.route('/report_defense')
def report_defense():
	sql = case_status(7)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_defense.html', row = result)

@reports.route('/report_prosecution')
def report_prosecution():
	sql = case_status(8)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_prosecution.html', row = result)

@reports.route('/report_probation')
def report_probation():
	sql = case_status(9)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_probation.html', row = result)

@reports.route('/report_provisional')
def report_provisional():
	sql = case_status(10)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_provisional.html', row = result)

@reports.route('/report_submitted')
def report_submitted():
	sql = case_status(11)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_submitted.html', row = result)

@reports.route('/report_susproc')
def report_susproc():
	sql = case_status(12)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_susproc.html', row = result)

@reports.route('/report_susjudge')
def report_susjudge():
	sql = case_status(13)
	query = text(sql)

	res = db.session.execute(query)
	result = res.fetchall()

	return render_template('report_susjudge.html', row = result)
################################
# custom ageing routes/functions
################################
def custom_age(case_category, case_status, age): # for age 1-9 yrs
    global sql
    sql = """
        SELECT 
        *,
        CASE
            WHEN strftime('%%m', date('now')) > strftime('%%m', date(filing_date)) THEN strftime('%%Y', date('now')) - strftime('%%Y', date(filing_date))
            WHEN strftime('%%m', date('now')) = strftime('%%m', date(filing_date)) THEN
                CASE 
                    WHEN strftime('%%d', date('now')) >= strftime('%%d', date(filing_date)) THEN strftime('%%Y', date('now')) - strftime('%%Y', date(filing_date))
                    ELSE strftime('%%Y', date('now')) - strftime('%%Y', date(filing_date)) - 1
                END
            WHEN strftime('%%m', date('now')) < strftime('%%m', date(filing_date)) THEN strftime('%%Y', date('now')) - strftime('%%Y', date(filing_date)) - 1
        END as age
        FROM
        tbl_case_record
        WHERE
        case_category = %d
        AND
        case_status = %d
        AND
        age = %d
    """
    return sql % (case_category, case_status, age)

# def custom_age10(case_category, case_status, age): # for age 10 yrs up
#     global sql
#     sql = """
#         SELECT 
#         *,
#         CASE
#             WHEN strftime('%%m', date('now')) > strftime('%%m', date(filing_date)) THEN strftime('%%Y', date('now')) - strftime('%%Y', date(filing_date))
#             WHEN strftime('%%m', date('now')) = strftime('%%m', date(filing_date)) THEN
#                 CASE 
#                     WHEN strftime('%%d', date('now')) >= strftime('%%d', date(filing_date)) THEN strftime('%%Y', date('now')) - strftime('%%Y', date(filing_date))
#                     ELSE strftime('%%Y', date('now')) - strftime('%%Y', date(filing_date)) - 1
#                 END
#             WHEN strftime('%%m', date('now')) < strftime('%%m', date(filing_date)) THEN strftime('%%Y', date('now')) - strftime('%%Y', date(filing_date)) - 1
#         END as age
#         FROM
#         tbl_case_record
#         WHERE
#         case_category = %d
#         AND
#         case_status = %d
#         AND
#         age > %d
#     """
#     return sql % (case_category, case_status, age)

@reports.route('/custom') # form
def custom():
	return render_template('custom.html')

@reports.route('/custom_report', methods = ['POST']) # for age 1-9 yrs
def custom_report():
	category = int(request.form['c_category'])
	age = int(request.form['c_age'])
	
	sql1 = custom_age(category, 2, age)
	query1 = text(sql1)

	result1 = db.session.execute(query1)
	rows1 = result1.fetchall()

	sql2 = custom_age(category, 5, age)
	query2 = text(sql2)

	result2 = db.session.execute(query2)
	rows2 = result2.fetchall()

	sql3 = custom_age(category, 6, age)
	query3 = text(sql3)

	result3 = db.session.execute(query3)
	rows3 = result3.fetchall()

	sql4 = custom_age(category, 7, age)
	query4 = text(sql4)

	result4 = db.session.execute(query4)
	rows4 = result4.fetchall()

	sql5 = custom_age(category, 8, age)
	query5 = text(sql5)

	result5 = db.session.execute(query5)
	rows5 = result5.fetchall()

	sql6 = custom_age(category, 11, age)
	query6 = text(sql6)

	result6 = db.session.execute(query6)
	rows6 = result6.fetchall()

	sql7 = custom_age(category, 12, age)
	query7 = text(sql7)

	result7 = db.session.execute(query7)
	rows7 = result7.fetchall()

	result = rows1 + rows2 + rows3 + rows4 + rows5 + rows6 + rows7

	return render_template('customyear.html', row = result)

#################################################################################
#end of routes
#################################################################################