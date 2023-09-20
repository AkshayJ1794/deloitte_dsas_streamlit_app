# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 00:59:50 2023

@author: akshaypjadhav
"""

import os
import win32com.client as win32
import re

def convert_rtf_to_docx(input_path, output_path):
    word = win32.Dispatch("Word.Application")
    word.Visible = False

    doc = word.Documents.Open(input_path)
    doc.SaveAs(output_path, FileFormat=16)  # FileFormat=16 for .docx
    doc.Close()

    word.Quit()


cwd = re.sub(r'\\','/',str(os.getcwd()))
cwd = cwd[:cwd.rfind('/')+1]
cwd = cwd +'data/VB/A&D transcripts'
print (cwd)
# Load data




# def convert_rtf_to_docx(input_path, output_path):
#     doc = Document(input_path)
#     doc.save(output_path)


input_directory = r'C:\Users\akshaypjadhav\Deloitte (O365D)\DSAS 2.0 - Documents\Projects - Active\2023_09_19_CGI_streamlit_app\data\VB\A&D transcripts'

# output_cwd = re.sub(r'\\','/',str(os.getcwd()))
# output_cwd = output_cwd[:output_cwd.rfind('/')+1]
# output_cwd = output_cwd +'results'

output_directory = r'C:\Users\akshaypjadhav\Deloitte (O365D)\DSAS 2.0 - Documents\Projects - Active\2023_09_19_CGI_streamlit_app\results'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    if filename.endswith(".rtf"):
        input_path = os.path.join(input_directory, filename)
        output_filename = os.path.splitext(filename)[0] + '.docx'
        output_path = os.path.join(output_directory, output_filename)

        convert_rtf_to_docx(input_path, output_path)
