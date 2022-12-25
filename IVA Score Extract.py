import pandas as pd
import pdfplumber # extract texts and tables from pdf files
import re # find and match strings to patterns
#------------------ pip installs
#pip install pdfplumber
#------------------ load file
pdf=pdfplumber.open(r'C:\Users\path\Facebook_IVA_Profile.pdf')
page = pdf.pages[0]
text = page.extract_text()
print(text)


#------------------ set up function
def getNumbers(str):
    array = re.findall(r'\s\d.\d\s', str)
    return array


#------------------ extract text from MSCI's ESG IVA scores
# dummy df
df = pd.DataFrame()
# define the strings to look for
String = "ENVIRONMENTAL"
e_score=re.compile(String)
String = "SOCIAL"
s_score=re.compile(String)
String = "GOVERNANCE"
g_score=re.compile(String)
String_t = "TICKER"
ticker_data=re.compile(String_t)

# split texts into lines
for line in text.split('\n'):
    if e_score.search(line):
        array=getNumbers(line)
        e=array
        df['e']=e
    if s_score.search(line):
        array=getNumbers(line)
        s=array
        df['s']=s
    if g_score.search(line):
        array=getNumbers(line)
        g=array
        df['g']=g
    if ticker_data.search(line):
        ticker=line
        match1 = re.findall(r':\s[A-Z]{2}\s', ticker)
        tckr=match1
        df['ticker']=tckr
        
# cleaning data
df['ticker'] = df['ticker'].str.replace(r':', '')

print(df)

filename = r'C:\Users\path\IVA Scores.csv'
df.to_csv(filename, index = False, encoding = 'utf-8')