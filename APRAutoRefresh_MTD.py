############################################################# Summary #############################################################
# The purpose of this script is two auto refrsh the APR so that by the time you get to the desk you just have to do quality checks.
# Chris programed to have the model (from the APR folder) create a copy with the day of reporting timestamp to the Daily reports folder.
    # Model - path\APR\APR Current Model.xlsx
    # Daily Reports - path\APR\Daily Reports
# This script will Open up The Current Model, refresh, save, and rename with date of report tiemstamp.
############################################################# APR Auto Refresh ######################################################################

from calendar import month
from email.mime import base
from posixpath import basename
import sys
import os
import pandas 

# To keep the terminal to a minimalist, ignore warnigns
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    
# pip install pypiwin32
from distutils.command.config import config
from fileinput import filename
import glob
import os

# datetiem set up
import datetime
today = datetime.date.today()
first = today.replace(day=1)
last_month = first - datetime.timedelta(days=1)
Day_of_reporting =  today.strftime("%Y-%m-%d")

# Identify today's APR
Day_of_reporting =  today.strftime("%Y-%m-%d")
MTD_APR = r"path\APR\APR Current Model.xlsx"



import win32com.client

# Start an instance of Excel
xlapp = win32com.client.DispatchEx("Excel.Application")

# Anticipoating pop ups that ask if you want the open fiel as read only.
xlapp.DisplayAlerts = False

# Open latest Site Details file and refresh
wb = xlapp.workbooks.open(MTD_APR)

# To suprress the pop up window that asks "do you want to save?"
xlapp.DisplayAlerts = False 

# Optional: this line is if you want to watch excel do it's task. "= 0" will keep the excel hidden as this script runs its task. "= 1" will display the excel application so enjoy the show.
xlapp.Visible = 0

# Refresh all data connections.
wb.RefreshAll()
wb.Save() # For some reason the APR is downloadedd and auto refreshed and saved in your documents

# To suprress the pop up window that asks "do you want to save?"
xlapp.DisplayAlerts = False 

# Quit
xlapp.Quit()

# Optional: notification for you.
print("Today's APR is refreshed and saved.")


############################################################# APR moves for rewview ######################################################################
# For some reason the APR model is downloaded, auto refreshed, saved in your documents.
# Copy the newly refreshed file in your docuemtns into the Daily Reports folder.
# First remove the existing APR yyyy-mm-dd file in daily reports.
import os
Yesterday_File = r"path\APR\Daily Reports\APR " + today.strftime("%Y-%m-%d") + ".xlsx"
if os.path.exists(Yesterday_File):
    os.remove(Yesterday_File)
else:
    print("This file doesn't exist")
  
# Now copy over the refreshed file in the docutments into the Daily Reports folder.
import shutil
From = r"C:\Users\ckraft\Documents\APR Current Model.xlsx"
To = r"path\APR\Daily Reports\APR " + today.strftime("%Y-%m-%d") + ".xlsx"
shutil.copy(From, To)
print("APR is saved in the Daily Reports from your Documents folder.")
