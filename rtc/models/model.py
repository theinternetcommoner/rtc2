# model.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class tbl_case_record(db.Model):
    case_id = db.Column(db.Integer, primary_key = True, nullable = False)
    case_no = db.Column(db.Text)
    case_title = db.Column(db.Text)
    case_nature = db.Column(db.Text)
    filing_date = db.Column(db.Text)
    receiving_date = db.Column(db.Text)
    warrant_date = db.Column(db.Text)
    detention_date = db.Column(db.Text)
    bail_date = db.Column(db.Text)
    archive_date = db.Column(db.Text)
    arraignment_date = db.Column(db.Text)
    pretrial_date = db.Column(db.Text)
    prosecution_evidence_date = db.Column(db.Text)
    defense_evidence_date = db.Column(db.Text)
    submitted_for_decision_date = db.Column(db.Text)
    disposal_date = db.Column(db.Text)
    promulgation_date = db.Column(db.Text)
    case_status = db.Column(db.Text)
    case_category = db.Column(db.Text)
    case_subcategory = db.Column(db.Text)
    disposal_type = db.Column(db.Text)
    logs = db.Column(db.Text)
    filename = db.Column(db.Text)

    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name
    #     }

    # def __repr__(self):
    #     return f"<MyModel {self.name}>"

    def __init__(
            self,
            case_id,
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
            logs,
            filename
        ):
        self.case_no = case_no
        self.case_title = case_title
        self.case_nature = case_nature
        self.filing_date = filing_date
        self.receiving_date = receiving_date
        self.warrant_date = warrant_date
        self.detention_date = detention_date
        self.bail_date = bail_date
        self.archive_date = archive_date
        self.arraignment_date = arraignment_date
        self.pretrial_date = pretrial_date
        self.prosecution_evidence_date = prosecution_evidence_date
        self.defense_evidence_date = defense_evidence_date
        self.submitted_for_decision_date = submitted_for_decision_date
        self.disposal_date = disposal_date
        self.promulgation_date = promulgation_date
        self.case_status = case_status
        self.case_category = case_category
        self.case_subcategory = case_subcategory
        self.disposal_type = disposal_type
        self.logs = logs
        self.filename = filename

class tbl_account(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    username = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        