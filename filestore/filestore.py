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

# @file_store.route('file_upload', method = ['POST'])
# def file_upload():
# 	return 'uploads'
# end of filestore functions