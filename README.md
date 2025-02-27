# IKILeUS - EchoTables
[![Identifier](https://img.shields.io/badge/doi-10.18419%2Fdarus--4774-d45815.svg)](https://doi.org/10.18419/darus-4774)
[![Identifier](https://img.shields.io/badge/doi-10.18419%2Fdarus--4774-d45815.svg)](https://doi.org/10.18419/darus-4775)
[![Identifier](https://img.shields.io/badge/doi-10.18419%2Fdarus--4774-d45815.svg)](https://doi.org/10.18419/darus-4776)
#### [IMPORTANT INFORMATION] while using the webapp, after every API call(button submit) click on HOME button to call the other APIs.

### Install the packages
``` pip install -r requirements.txt ```

### To run the webapp locally:
``` python3 api.py ``` <br>
Note: Open the given link <br>
Test URL: https://en.wikipedia.org/wiki/Vitamin_C

### To Run the webapp in Colab
Open these 3 to get the proj running
- Colab: https://colab.research.google.com/drive/12rdPr2I76FtxWZUQzkpAQz9wmUsumJ-k#scrollTo=nS7mQuJ4Inbn
- Ngrok: https://dashboard.ngrok.com/tunnels/agents (delete the running session)
- SSH: https://github.com/settings/keys (update the ssh keys from colab)

And follow the instructions given in the notebook ->[Notebook Link](https://colab.research.google.com/drive/12rdPr2I76FtxWZUQzkpAQz9wmUsumJ-k?usp=sharing)

### Folder Information:
- modules folder: Contains all the .py files
  - pdf_tableExtract.py : module to extract tables from pdf
  - url_tableExtract.py : module to extract tables through scraping for the given url
  - table_summary.py : modules to generate table summary
- static folder: Contains the css, images, js for the front end
- templates folder: Contains the webpages
  - index.html: Page to choose the input type: url or pdf <br>
    ![image](https://github.com/user-attachments/assets/46cc0c21-49f7-432d-8784-33871d95f18a)

  - upload.html: Page to upload the File<br>
  ![image](https://github.com/user-attachments/assets/142c915c-3579-45e6-9347-6eff2727f2e5)

  - fileindex.html: Once the file is uploaded, this is the page to choose the api(table extraction or table summary) <br>
  ![image](https://github.com/user-attachments/assets/69d6ed99-caa6-4123-b13b-ef9abd4c67c8)

  - urlIndex.html: Page to choose the api(table extraction or table summary) for the Url <br>
  ![image](https://github.com/user-attachments/assets/65898cff-bf46-4354-aeb6-95adfeea2de8)

- notebooks folder: Contains the python notebooks for models
<br>
Note: The web template was taken from Colorlib (https://colorlib.com)

### Module Information:
1. URL Table Extraction

   Input(URL): https://en.wikipedia.org/wiki/Vitamin_C <br>
   Process: Scrape table from URL <br>
   <b>Sample Result:</b> <br>
   <b>[INFO]</b>Web Page to enter the URL and choose the API "Table Extraction" <br>
   ![image](https://github.com/user-attachments/assets/3055601a-34f9-4026-b5e4-6f8e270d68a5) <br>
   <b>[INFO]</b>Result is displayed on the same page at the bottom <br>
   ![image](https://github.com/user-attachments/assets/78ce2fba-9db0-4e41-911b-9fe5393eb9cd)


3. URL Table Summary

   Input(URL): https://en.wikipedia.org/wiki/Vitamin_C <br>
   Process: Scrape table from the given URL > table summary<br>
   <b>Sample Result: </b><br>
    <b>[INFO]</b> Web Page to enter the URL and choose the API "Table Summary" <br>
   ![image](https://github.com/user-attachments/assets/0dc20ae0-9c3c-4833-b7bb-21a98a0b5cbf) <br>
   <b>[INFO]</b>Result is displayed on the same page at the bottom <br>
   ![image](https://github.com/user-attachments/assets/5ebc47ff-120f-473e-a613-87bf05d9858b)

   
5. PDF Table Extraction
   
   Input: PDF file<br>
   Process: Table extraction from pdf<br>
   <b>Sample Result: </b><br>
    <b>[INFO]</b>Web Page to choose a file<br>
   ![image](https://github.com/user-attachments/assets/5a68f672-ad5b-4a6a-8d5a-e4c27e408a55)
   <br> <b>[INFO]</b>Web Page to call the API "Table Table Extraction" for the uploaded pdf file <br>
   ![image](https://github.com/user-attachments/assets/0d0b2120-66e5-40c2-a4ef-52fecc9afbab)
   <br> <b>[INFO]</b>Result is displayed on the same page at the bottom <br>
   ![image](https://github.com/user-attachments/assets/c5518f1e-20ce-4717-ac2d-927b05e415b0)

  
   
7. PDF Table Summary
   
   Input: PDF file<br>
   Process: Table extraction from pdf > table summary<br>
    <b>Sample Result: </b><br>
    <b>[INFO]</b>Web Page to choose a file<br>
   ![image](https://github.com/user-attachments/assets/5a68f672-ad5b-4a6a-8d5a-e4c27e408a55)
   <br><b>[INFO]</b>Web Page to call the API "Table Table Extraction" for the uploaded pdf file <br>
   ![image](https://github.com/user-attachments/assets/45ea7573-05ce-4f21-856a-52e21031ad09)
   <br> <b>[INFO]</b>Result is displayed on the same page at the bottom <br>
   ![image](https://github.com/user-attachments/assets/63dab8a5-43cc-45e2-a51a-ee2c2813f9a7)

   

