#!/usr/bin/env python

"""
This api.py file links between the html page and nlp modules

NOTE: Install the requirement file before running the api.py
To run the webapp:
    $python3 api.py
    Note: Open the given link
"""

__author__      = "Pema Gurung"
__version__     = "0.0.2"
__maintainer__  = "Pema Gurung"
__email__       = "st186867@stud.uni-stuttgart.de"
__status__      = "Production"

# Flask is a micro web framework written in Python. Import flask library to load the html pages and to display the result to the webpage
import os
from flask import Flask, request, render_template,redirect, Response, url_for

# import the module created to scrape tables from module folder
from modules.url_tableExtract import url_extract_table
from modules.pdf_tableExtract import pdf_extract_table
from modules.table_summary import html_table_summary

# os.chdir('..')

app = Flask(__name__) # creates a Flask application object — app — in the current Python module. 

UPLOAD_FOLDER = "static/uploaded_files/"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

output_folder = "pdf_output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

################# Display UI ################
@app.route('/',methods=["GET"])
def homepage():
    """
    This function loads the homepage index.html
    """
    return render_template('index.html')

@app.route('/url_type',methods=["GET"])
def url_type():
    """
    This function loads the homepage for UrlIndex.html
    """
    return render_template('urlIndex.html')

@app.route('/file_type',methods=["GET"])
def file_type():
    """
    This function loads the homepage fileindex.html
    """
    return render_template('upload.html')

@app.route('/fileIndex',methods=["GET"])
def fileIndex():
    """
    This function loads the homepage index.html
    """
    print("====rendering fileIndex.html=====")
    print("===stored_file_name",stored_file_name)
    return render_template('fileIndex.html',filename=stored_file_name)

################# For URL ################

@app.route('/selected_action', methods=["GET","POST"])
def selected_action():
    """
    This route is called from the index.html page through ajax query
    Based on the choices(table extraction, row summary, table summary) choosen by the user, it does the respective functions and returns the result to the index.html
    """
    data = request.get_json() # retrieve the data sent from webpage JavaScript 
    url = data['url_text']

    if data['choices'] == "Table Extraction":
        print("Selected Choice: Table Extraction")
        table_html, list_of_tables = url_extract_table(url) #scrape_table() returns both list of df and html tables
        
        list_of_tableJson = [df.to_html() for df in list_of_tables] #convert the DataFrame to html
        print("# of Tables found:", len(list_of_tableJson))

        response = {
            "response": list_of_tableJson
        }

        return response

        
    elif data['choices'] == "Table Summary":
        print("Selected Choice: Table Summary")
        
        list_of_htmltable, list_of_tables = url_extract_table(url)
        print("# of Tables found:", len(list_of_tables))
        
        each_table_summary = html_table_summary(list_of_htmltable)
            
        response = {
                    "response": each_table_summary
        }

        return response
                                
    else:
        return None

#################  For PDF ################

@app.route('/file_upload',methods=["GET","POST"])
def file_upload():
    """The route called after uploading from the upload.html file. 
    This method takes the file and saves it to the upload folder.
    """
    uploaded_file = request.files['file']
    global stored_file_name
    
    
    if uploaded_file.filename != '':
        stored_file_name = UPLOAD_FOLDER+uploaded_file.filename
        uploaded_file.save(stored_file_name)
        return (redirect(url_for('fileIndex')))
        # return render_template('fileIndex.html', filename=stored_file_name)
    

@app.route('/file_selected_action',methods=["GET","POST"])
def file_selected_action():
    """
    This route is called from the fileIndex.html page through ajax query
    Based on the choices(table extraction, row summary, table summary) choosen by the user after uploading the file, 
    it does the respective functions and returns the result to the index.html
    """
    data = request.get_json() # retrieve the data sent from webpage JavaScript 
    # choices = data['choices']

    if data['choices'] == "Table Extraction":
        print("Selected Choice: Table Extraction")  
        pdf_path = stored_file_name 
        table_html, list_of_tables = pdf_extract_table(pdf_path,output_folder)
        print("# of Tables found:", len(list_of_tables))

        response = {
            "response": table_html
        }

        return response   
       
    elif data['choices'] == "Table Summary":
        print("Selected Choice: Table Summary")
        pdf_path = stored_file_name 
        list_of_htmltable, list_of_tables = pdf_extract_table(pdf_path,output_folder)
        print("# of Tables found:", len(list_of_tables))
        
        each_table_summary = html_table_summary(list_of_htmltable)
            
        response = {
                    "response": each_table_summary
        }

        return response
    else:
        return None                            
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2024,debug=True)
