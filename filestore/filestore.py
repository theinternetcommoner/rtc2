from flask import Flask, Blueprint, render_template, session, redirect, url_for, request
from models.modelref import *
from functools import wraps
from sqlalchemy import text
import os

file_store = Blueprint("filestore", __name__, static_folder = "static", template_folder = "templates")

# for filestore functions
@file_store.route('/')
def dir():
	filestorage = tbl_file.query.all()
	# for item in filestorage:
	# 	return item.filename
	return render_template('pdf_dir.html', storage = filestorage)

@file_store.route('/pdf/<int:pdf_id>')
def show_file(pdf_id):
	file = tbl_file.query.get(pdf_id)
	return render_template('pdf_file.html', file = file)

@file_store.route('/file_upload', methods = ['POST'])
def file_upload():
	if 'pdf' not in request.files:
		return redirect(request.url)

	pdf = request.files['pdf']
	if pdf.filename == '':
		return redirect(request.url)

	pdf.save(os.path.join('static/uploads', pdf.filename))
	new_pdf = tbl_file(filename=pdf.filename)
	db.session.add(new_pdf)
	db.session.commit()
	return redirect(url_for('filestore.dir'))

@file_store.route('/uploadform')
def upload_form():
	return render_template('upload_form.html')
# end of filestore functions