############################################################# Summary #############################################################
# The purpose of this script is to dynamically move the Raw data spit out by Alteryx to the public folder.
    #Alteryx spits out here: \\path\Previous Month Raw Data
    #Public folder: \\another_path
# As of right now this process is done with PowerShell. The issue is every month the script needs to be changed.
# The year and month have to be changed with ctrl + H. Python datetime will eliminate this manual change.
############################################################# I like to move it, move it  ######################################################################
# To keep the terminal to a minimalist, ignore warnigns
from copy import copy
import os
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    
print("Task: Raw data move")
# datetiem set up
import datetime
from datetime import date, timedelta
now = datetime.datetime.now()
import datetime
today = datetime.date.today()
first = today.replace(day=1)
last_month = first - datetime.timedelta(days=1)
Day_of_reporting =  today.strftime("%Y-%m-%d")
#import datetime
from datetime import date, timedelta
last_day_prev_month = (date.today().replace(day=1) - timedelta(days=1))
#print(last_day_prev_month)
convert_to_str = last_day_prev_month.strftime("%Y-%m-%d")
print(convert_to_str)

# From files
Calls_From = r"\\path\Previous Month Raw Data\Previous Month Calls Raw Data.csv"
Bonus_From = r"\\path\Previous Month Raw Data\Previous Month Bonus Raw Data.csv"
Saves_From= r"\\path\Previous Month Raw Data\Previous Month Saves Raw Data.csv"

# To files
#To = rb"\\path\ " + today.strftime("%Y-%m")
This_month = today.strftime("%Y-%m")
print(This_month)
To = r"\\another_path\2022-06"
print("Moving raw data files for Prelim.")

import shutil
shutil.copy(Calls_From, To)
print("Calls file moved.")
import shutil
shutil.copy(Bonus_From, To)
print("Bonus file moved.")
import shutil
shutil.copy(Saves_From, To)
print("Saves file moved.")

# Renaming the newly copied file
os.rename(r"\\another_path\2022-06\Previous Month Calls Raw Data.csv", 
          r"\\another_path\2022-06\Calls Data " + convert_to_str + " Prelim.csv") #yyyy-mm-dd)
print("Calls renamed")
os.rename(r"\\another_path\2022-06\Previous Month Bonus Raw Data.csv", 
          r"\\another_path\2022-06\Bonus Data " + convert_to_str + " Prelim.csv") #yyyy-mm-dd)
print("Bonus renamed")
os.rename(r"\\another_path\2022-06\Previous Month Saves Raw Data.csv", 
          r"\\another_path\2022-06\Saves Data " + convert_to_str + " Prelim.csv") #yyyy-mm-dd
print("Saves renamed")
