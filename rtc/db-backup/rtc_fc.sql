DROP VIEW "main"."custody";
CREATE VIEW custody AS
SELECT
tbl_case_file.case_no,
tbl_case_file.case_title,
tbl_case_file.case_nature,
tbl_date.filing_date,
tbl_date.receiving_date,
tbl_date.archive_date,
tbl_date.pretrial_date
FROM 
tbl_case_file 
JOIN 
tbl_file_status ON tbl_file_status.case_id = tbl_case_file.case_id 
JOIN 
tbl_case_status ON tbl_case_status.status_id = tbl_file_status.status_id 
JOIN 
tbl_file_category ON tbl_file_category.case_id = tbl_case_file.case_id 
JOIN 
tbl_case_category ON tbl_case_category.category_id = tbl_file_category.category_id 
JOIN 
tbl_file_subcategory ON tbl_file_subcategory.case_id = tbl_case_file.case_id 
JOIN 
tbl_case_subcategory ON tbl_case_subcategory.subcategory_id = tbl_file_subcategory.subcategory_id 
JOIN 
tbl_file_date ON tbl_file_date.case_id = tbl_case_file.case_id 
JOIN 
tbl_date ON tbl_date.date_id = tbl_file_date.date_id 
JOIN 
tbl_file_logs ON tbl_file_logs.case_id = tbl_case_file.case_id 
JOIN 
tbl_logs ON tbl_logs.log_id = tbl_file_logs.log_id 
WHERE 
tbl_case_status.case_status = 'on going' 
AND 
tbl_case_category.case_category = 'civil' 
AND 
tbl_case_subcategory.subcategory_id = '12'
ORDER BY 
tbl_case_file.case_id ASC
-------------------------------------------------------------------------
DROP VIEW "main"."adoption";
CREATE VIEW adoption AS
SELECT
tbl_case_file.case_no,
tbl_case_file.case_title,
tbl_case_file.case_nature,
tbl_date.filing_date,
tbl_date.receiving_date,
tbl_date.archive_date,
tbl_date.pretrial_date
FROM 
tbl_case_file 
JOIN 
tbl_file_status ON tbl_file_status.case_id = tbl_case_file.case_id 
JOIN 
tbl_case_status ON tbl_case_status.status_id = tbl_file_status.status_id 
JOIN 
tbl_file_category ON tbl_file_category.case_id = tbl_case_file.case_id 
JOIN 
tbl_case_category ON tbl_case_category.category_id = tbl_file_category.category_id 
JOIN 
tbl_file_subcategory ON tbl_file_subcategory.case_id = tbl_case_file.case_id 
JOIN 
tbl_case_subcategory ON tbl_case_subcategory.subcategory_id = tbl_file_subcategory.subcategory_id 
JOIN 
tbl_file_date ON tbl_file_date.case_id = tbl_case_file.case_id 
JOIN 
tbl_date ON tbl_date.date_id = tbl_file_date.date_id 
JOIN 
tbl_file_logs ON tbl_file_logs.case_id = tbl_case_file.case_id 
JOIN 
tbl_logs ON tbl_logs.log_id = tbl_file_logs.log_id 
WHERE 
tbl_case_status.case_status = 'on going' 
AND 
tbl_case_category.case_category = 'civil' 
AND 
tbl_case_subcategory.subcategory_id = '9'
ORDER BY 
tbl_case_file.case_id ASC
-------------------------------------------------------------------------
DROP VIEW "main"."age_0";
CREATE VIEW age_0 AS
SELECT 
tbl_case_file.case_no AS case_no,
tbl_case_file.case_title AS case_title,
tbl_case_file.case_nature AS case_nature,
tbl_date.filing_date AS filing_date,
tbl_date.receiving_date AS receiving_date,
cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', tbl_date.filing_date) as int) || ' years '
AS age
FROM 
tbl_case_file 
join 
tbl_file_status ON tbl_file_status.case_id = tbl_case_file.case_id 
join 
tbl_case_status ON tbl_case_status.status_id = tbl_file_status.status_id 
join 
tbl_file_date ON tbl_file_date.case_id = tbl_case_file.case_id 
join 
tbl_date ON tbl_date.date_id = tbl_file_date.date_id 
join 
tbl_file_category ON tbl_file_category.case_id = tbl_case_file.case_id 
join 
tbl_case_category ON tbl_case_category.category_id = tbl_file_category.category_id 
where 
tbl_case_status.case_status = 'ON  going'
AND
tbl_case_category.case_category = 'criminal'
AND
tbl_case_category.case_category = 'cicl'
AND
age = 0
ORDER BY
tbl_case_file.case_no ASC
-------------------------------------------------------------------------
DROP VIEW "main"."archive";
CREATE VIEW archive AS
SELECT 
tbl_case_file.case_no AS case_no,
'pp. vs. ' || tbl_case_file.case_title AS case_title,
tbl_case_file.case_nature AS case_nature,
tbl_date.filing_date AS filing_date,
tbl_date.receiving_date AS receiving_date,
tbl_date.archive_date AS archive_date 
FROM
tbl_case_file
JOIN 
tbl_file_date ON tbl_file_date.case_id = tbl_case_file.case_id 
JOIN tbl_date ON tbl_date.date_id = tbl_file_date.date_id 
JOIN tbl_file_status ON tbl_file_status.case_id = tbl_case_file.case_id 
JOIN tbl_case_status ON tbl_case_status.status_id = tbl_file_status.status_id 
WHERE 
tbl_case_status.case_status = 'archived'
ORDER BY tbl_case_file.case_no ASC
-------------------------------------------------------------------------
DROP VIEW "main"."case_ageing";
CREATE VIEW case_ageing AS
SELECT 
tbl_case_file.case_no AS case_no,
tbl_case_file.case_title AS case_title,
tbl_case_file.case_nature AS case_nature,
tbl_date.filing_date AS filing_date,
tbl_date.receiving_date AS receiving_date,
cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', tbl_date.filing_date) as int) || ' years '
AS age
FROM 
tbl_case_file 
join 
tbl_file_status ON tbl_file_status.case_id = tbl_case_file.case_id 
join 
tbl_case_status ON tbl_case_status.status_id = tbl_file_status.status_id 
join 
tbl_file_date ON tbl_file_date.case_id = tbl_case_file.case_id 
join 
tbl_date ON tbl_date.date_id = tbl_file_date.date_id 
join 
tbl_file_category ON tbl_file_category.case_id = tbl_case_file.case_id 
join 
tbl_case_category ON tbl_case_category.category_id = tbl_file_category.category_id 
where 
tbl_case_status.case_status = 'ON  going'
ORDER BY
tbl_case_file.case_no ASC
-------------------------------------------------------------------------
DROP VIEW "main"."civil_age_0";
CREATE VIEW civil_age_0 AS
SELECT 
tbl_case_file.case_no AS case_no,
tbl_case_file.case_title AS case_title,
tbl_case_file.case_nature AS case_nature,
tbl_date.filing_date AS filing_date,
tbl_date.receiving_date AS receiving_date,
cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', tbl_date.filing_date) as int) || ' years '
AS age
FROM 
tbl_case_file 
join 
tbl_file_status ON tbl_file_status.case_id = tbl_case_file.case_id 
join 
tbl_case_status ON tbl_case_status.status_id = tbl_file_status.status_id 
join 
tbl_file_date ON tbl_file_date.case_id = tbl_case_file.case_id 
join 
tbl_date ON tbl_date.date_id = tbl_file_date.date_id 
join 
tbl_file_category ON tbl_file_category.case_id = tbl_case_file.case_id 
join 
tbl_case_category ON tbl_case_category.category_id = tbl_file_category.category_id 
where 
tbl_case_status.case_status = 'ON  going'
AND
tbl_case_category.case_category = 'civil'
AND
age = 0
ORDER BY
tbl_case_file.case_no ASC
-------------------------------------------------------------------------
DROP VIEW "main"."ra_7610";
CREATE VIEW ra_7610 AS
SELECT 
tbl_case_file.case_no AS case_no, 
'pp. vs. ' || tbl_case_file.case_title AS case_title,
tbl_case_file.case_nature AS case_nature,
tbl_date.filing_date AS filing_date,
tbl_date.receiving_date AS receiving_date,
tbl_date.archive_date AS archive_date,
tbl_date.arraignment_date AS arraignment_date,
tbl_date.pretrial_date AS pretrial_date 
from 
tbl_case_file 
JOIN
tbl_file_status ON tbl_file_status.case_id = tbl_case_file.case_id 
JOIN
tbl_case_status ON tbl_case_status.status_id = tbl_file_status.status_id 
JOIN
tbl_file_category ON tbl_file_category.case_id = tbl_case_file.case_id 
JOIN
tbl_case_category ON tbl_case_category.category_id = tbl_file_category.category_id 
JOIN
tbl_file_subcategory ON tbl_file_subcategory.case_id = tbl_case_file.case_id 
JOIN
tbl_case_subcategory ON tbl_case_subcategory.subcategory_id = tbl_file_subcategory.subcategory_id 
JOIN
tbl_file_date ON tbl_file_date.case_id = tbl_case_file.case_id 
JOIN
tbl_date ON tbl_date.date_id = tbl_file_date.date_id 
JOIN
tbl_file_logs ON tbl_file_logs.case_id = tbl_case_file.case_id 
JOIN
tbl_logs ON tbl_logs.log_id = tbl_file_logs.log_id 
WHERE
tbl_case_status.case_status = 'on  going' 
AND
tbl_case_category.case_category = 'criminal' 
AND
tbl_case_subcategory.subcategory_id = '4' 
ORDER BY
tbl_case_file.case_id ASC
-------------------------------------------------------------------------
DROP VIEW "main"."disposed";
CREATE VIEW disposed AS
SELECT 
tbl_case_file.case_no AS case_no,
tbl_case_file.case_title AS case_title,
tbl_case_file.case_nature AS case_nature,
tbl_disposal.disposal_nature AS case_status,
tbl_date.filing_date AS filing_date,
tbl_date.receiving_date AS receiving_date,
tbl_date.warrant_date AS warrant_date,
tbl_date.detention_date AS detention_date,
tbl_date.bail_date AS bail_date,
tbl_date.archive_date AS archive_date,
tbl_date.arraignment_date AS arraignment_date,
tbl_date.pretrial_date AS pretrial_date,
tbl_date.disposal_date AS disposal_date 
FROM 
tbl_case_file 
JOIN 
tbl_file_date ON tbl_file_date.case_id = tbl_case_file.case_id 
JOIN 
tbl_date ON tbl_date.date_id = tbl_file_date.date_id 
JOIN 
tbl_file_disposal ON tbl_file_disposal.case_id = tbl_case_file.case_id 
JOIN 
tbl_disposal ON tbl_disposal.disposal_id = tbl_file_disposal.disposal_id
ORDER BY
tbl_case_file.case_no ASC
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------
-------------------------------------------------------------------------