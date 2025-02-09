import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents

def wiki_extract(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    wikiTable=soup.findAll('table',{'class':"wikitable"})
    list_table_html = []
    list_of_tables = []  
    if len(wikiTable)>0:
        dfs = pd.read_html(str(wikiTable))
        
        for each_df in dfs:
            each_df = pd.DataFrame(each_df) # convert list to dataframe
            each_df = each_df.fillna('')
            list_of_tables.append(each_df)
            list_table_html.append(each_df.to_html(header="true", table_id="table"))
    return list_table_html, list_of_tables
    
def url_extract_table(url):
    """This function scrapes the content and finds all the tables from the given url using Beautiful soup. 
    The found html tables are then converted to a DataFrame using pandas

    Args:
        url (str): a web url such as https://en.wikipedia.org/wiki/Vitamin_C

    Returns:
        list: returns a list of tables 
    """
    if "en.wikipedia.org/wiki" in url:
        table_html, list_of_tables = wiki_extract(url)
        return table_html, list_of_tables
    else:
        response=requests.get(url,timeout = 10) 
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            table_html = soup.find_all('table')   
            list_table_html = []
            list_of_tables = []  
            if len(table_html)>0:
                dfs = pd.read_html(str(table_html))
                
                for each_df in dfs:
                    each_df = pd.DataFrame(each_df) # convert list to dataframe
                    each_df = each_df.fillna('')
                    list_of_tables.append(each_df)
                    list_table_html.append(each_df.to_html(header="true", table_id="table"))
            return list_table_html, list_of_tables
        else:
            return ["Link Error Response Code:"+str(response.status_code)],["Link Error Response Code:"+str(response.status_code)]

def test():
    """
    This function is for testing the Table scraping function
    """
    # List of URLS to test
    # url= "https://en.wikipedia.org/wiki/Vitamin_C" # has 4 tables
    # url = "https://en.wikipedia.org/wiki/Metabolic_pathway" # has no tables
    # url = "https://en.wikipedia.org/wiki/PAW_Patrol" # has 3 tables
    # url = "https://wiki.q-researchsoftware.com/wiki/Marketing_-_Brand_Health_Table" #has image not table
    # url = "https://www.timeshighereducation.com/world-university-rankings/2023/world-ranking" #complex tables
    url = "https://www.studysmarter.de/schule/mathe/analysis/" # has one table
    
    html_table_list, table_list = url_extract_table(url)
    for i in table_list:
        print(i)
        print("=="*20)
    # print(list_of_tables)
    
# test()

"""if en.wikipedia.org in url: use wiki table extractor
"""

