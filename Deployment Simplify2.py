################################################# Summary #################################################
"""
This is the second piece to the SJS CM/Deployment ETL process. 

Just for context, the SJS CM data feeds one of our PowerBi reports.
The Contact Center has many departments and sub departments.
Most of the tiem, each department specializes in different areas of operations of the business.
The Deployment report only cares about one particular group of call agents and their tasks/performances.
So this reporting is tailored to the RM/Deployment of the business.
In the report there are metrics measuring the Deployment agents performances.

In the first step of the SJS CM/Deployment ETL process the SJS CM data is emailed to us in the form of a zipped excel file.
The first process sifts through my inbox, looking in a particular folder for the email containing the SJS CM data.
Based on two conditions: 
    Is the email unread? 
    Is the email sent today?
python will know which email message to open, download the attached file, save in the proper path, and unzip the file.
Once the staging is set up. The PowerBi is pointed to the unzipped file and the data cleaning takes place in the Bi.
That is inefficient. 

This script will reduce the staged (unzipped) attachemnt file to speed up the refresh rate thus speeding up the reporting all together.
To shrink the data we need to filter out irrelevant agents from irrelevant departents.


The outline broadly looks like this:
    1. Connect to Oracle on the backend.
    2. Query a mini roster from the master roster in the Oracle database.
    3. Bring in the unzipped version of the attachment file as downloaded in step 1 of this SJS CM/Deployment ETL process.
Once the data is cleaned up we'll export a new table that is a reduced version of the attachment file.
The data cleaning used to be done in Power Bi.
"""

import cx_Oracle #pip install cx_Oracle
import sqlalchemy #pip install sqlalchemy
import pandas as pd 
DATABASE = "DATABASENAME"
SCHEMA   = "CKRAFT-BOT"
PASSWORD = "its_a_secret"
connstr  = "oracle://{}:{}@{}".format(SCHEMA, PASSWORD, DATABASE)
conn     = sqlalchemy.create_engine(connstr)

### the full Oracle DB Client must be installed. They do not do this by default when they install Oacle SQL Developer. ### 
### An easy way to check this: windows key > type "sql plus" > if an app doesn't pop up, you don't have it. ###

query = """
    SELECT
    Upper(cr."First Last - CallMiner") AS "F,L Name"
    ,UPPER(cr."Last, First for Report") AS "L,F Name"
    ,cr."Site" 
    ,cr."Sup" 
    ,cr."Dept" 
    ,cr."Sub Dept" 
    ,cr."Term" 
    FROM OPS_REPORTING.CC_ROSTER cr 
    WHERE cr."Sub Dept" LIKE 'Deployment' OR cr."Sub Dept" LIKE 'Repair SRT'
    """
Mini_Roster = pd.read_sql(query, conn)
Mini_Roster.set_index('Agent Name')
#print(Mini_Roster.keys())
print('This is the SQL query:\n\n', (Mini_Roster.head()))

# Taking unzipped Deployment file and converting to pandas df
Deployment_Dash_Daily = r"\\path\Deployment_Dash_-_daily.xls"
Deploy_Unclean = pd.read_excel(Deployment_Dash_Daily)
# Deleting irrelevant rows like the first three rows, empty row, and the HS manufacure row
    # will need to delete some rows
    # then redefine the header row
Deploy_Cleaning = Deploy_Unclean.drop(labels = [0,1,3,4], axis = 0)
print('This is the relevant table:\n\n', (Deploy_Cleaning.head()))

Deploy_Cleaning.columns = Deploy_Cleaning.iloc[0]
new_header = Deploy_Cleaning.iloc[1:].reset_index(drop = True)
print('This is the sneak peak to the new header:\n\n', (new_header.head(2)))


# Reformatting the agent name column called 'Created By' to be uppercased
new_header['Created By'] = new_header['Created By'].str.upper()
# Displaying the indicies of the Deploy_Unclean df
#print(new_header.keys())
print('This is the Deploy table with new headers:\n\n', (new_header))
# Merging the SQL query mini roster to the Deploy_Unclean df
Deploy_Cleaner = pd.merge(Mini_Roster, new_header, how = 'left', left_on = 'Agent Name', right_on = 'Created By')
print('This is the Deploy Cleaner table:\n\n', (Deploy_Cleaner.head()))

# Dropping nulls is an option, for visibility i want to keep the N/As
#Deploy_Clean = Deploy_Cleaning.dropna()
#print('This is the Deploy Clean table\n', (Deploy_Clean))
Deploy_Cleaner.to_csv(r"C:\Users\path\Deploy_Cleaned.csv", index = False, encoding = 'utf-8') 
print("The Deploy Cleaned file is ready to go.")




