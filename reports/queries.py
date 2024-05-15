#################################################################################
#queries
#################################################################################

def count_case(case_status, case_category):
    global sql        
    sql = """
        SELECT 
        COUNT(*) as count
        FROM
        tbl_case_record
        WHERE
        case_status = %d
        AND
        case_category = %d
    """
    return sql % (case_status, case_category)

def case_category(case_status, case_category):
    global sql
    sql = """
        SELECT 
        *
        FROM
        tbl_case_record
        WHERE
        case_status = %d
        AND
        case_category = %d
    """
    return sql % (case_status, case_category)

def case_subcategory(case_status, case_category):
    global sql
    sql = """
        SELECT 
        *
        FROM
        tbl_case_record
        WHERE
        case_status = %d
        AND
        case_subcategory = %d
    """
    return sql % (case_status, case_category)

def case_age(case_status, age): # for age 1-9 yrs
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
        age = %d
    """
    return sql % (case_status, age)

def case_age10(case_status, age): # for age 10 yrs up
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
        age > %d
    """
    return sql % (case_status, age)

def case_status(case_status):
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