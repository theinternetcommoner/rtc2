#################################################################################
#queries
#################################################################################

def count_category_status(case_status):
	global sql
	sql = """
		SELECT 
		COUNT(*)
		FROM
		tbl_case_record
		WHERE
		case_status = %d
		AND
		case_category = ?
	"""
	return sql % case_status

def select_case_status(case_status):
	global sql
	sql = """
		SELECT 
		*
		FROM
		tbl_case_record
		WHERE
		case_status = %d
	"""
	return sql % case_status

def select_age_case_status(case_status): # for age 1-9 yrs
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
		case_status = %d
		AND
		age = ?
	"""
	return sql % case_status

def select_age10_case_status(case_status): # for age 10 yrs up
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
		case_status = %d
		AND
		age > ?
	"""
	return sql % case_status

def select_category_status(case_status):
	global sql
	sql = """
		SELECT 
		*
		FROM
		tbl_case_record
		WHERE
		case_status = %d
		AND
		case_category = ?
	"""
	return sql % case_status

def select_subcategory_status(case_status):
	global sql
	sql = """
		SELECT 
		*
		FROM
		tbl_case_record
		WHERE
		case_status = %d
		AND
		case_subcategory = ?
	"""
	return sql % case_status

#################################################################################
#end of queries
#################################################################################

#################################################################################
#for backup
#################################################################################

# PS C:\rtc2\rtc> sqlite3 rtc_fc.db
# SQLite version 3.39.4 2022-09-29 15:55:41
# Enter ".help" for usage hints.
# sqlite> .backup rtc_fc.bak
# sqlite>