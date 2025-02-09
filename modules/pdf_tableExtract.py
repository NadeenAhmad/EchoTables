import os
import pandas as pd
from img2table.document import PDF
from img2table.ocr import TesseractOCR


def pdf_extract_table(pdf_path, pdf_output_dir, ocr_lang="eng"):
    # Instantiate the OCR engine
    ocr = TesseractOCR(lang=ocr_lang)

    if pdf_path.endswith(".pdf"):
        pdf_path_base=os.path.basename(pdf_path)
        base_name =  os.path.splitext(pdf_path_base)[0]
        # Instantiate the PDF document
        pdf = PDF(src=pdf_path)

        # Extract tables
        pdf_tables = pdf.extract_tables(ocr=ocr)

        print("==>",os.path.join(pdf_output_dir, f"{base_name}.xlsx"))
        print("===Base:",base_name)
        print("===outputdir",pdf_output_dir)
        # Save the extracted tables to an XLSX file
        xlsx_path = os.path.join(pdf_output_dir, f"{base_name}.xlsx")
        pdf.to_xlsx(xlsx_path, ocr=ocr)
        print(f"Saved tables to {xlsx_path}")

        # Convert the XLSX file to CSV
        table_html, list_of_tables = xlsx_to_csv(xlsx_path, pdf_output_dir, base_name)

        return table_html, list_of_tables

def xlsx_to_csv(xlsx_path, pdf_output_dir, base_name):
    # Load the XLSX file
    xlsx = pd.ExcelFile(xlsx_path)

    list_of_tables = []
    list_of_htmltable = []
    
    # Convert each sheet in the XLSX file to a CSV file
    for sheet_name in xlsx.sheet_names:
        df = pd.read_excel(xlsx, sheet_name=sheet_name)
        list_of_tables.append(df)
        list_of_htmltable.append(df.to_html(header="true", table_id="table"))
    return list_of_htmltable, list_of_tables

        
# Example usage
# output_folder = "/Volumes/MacPema/HIWI2/tablesummary/pdf_output"  
# pdf_path = "/Volumes/MacPema/HIWI2/tablesummary/Documents/Doc1/Exercise_10.pdf"  # Replace with the path to your PDF folder
# table_html, list_of_tables = pdf_extract_table(pdf_path,output_folder)
