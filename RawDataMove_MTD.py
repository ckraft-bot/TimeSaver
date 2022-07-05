############################################################# Summary #############################################################
# The purpose of this script is to dynamically move the Raw data spit out by Alteryx to the public folder.
    #Alteryx spits out here: \\usfl04fsx04v.hsus.hsa.int\data\Contact Center Reporting\Data Sources\APR\Current Day Raw Data
    #Public folder: \\usfl04fsx04v.hsus.hsa.int\data\Ops Reporting\Management\Raw Data
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
now = datetime.datetime.now()
today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
#print(lastMonth.strftime("%y-%m")) #yy-mm
#print(today.strftime("%Y-%m-%d")) #yyyy-mm-dd
#print(today.strftime("%Y-%m")) #yyyy-mm
#print(today.strftime("%d-%b-%y")) #dd-month in short abbreviation-yy

# From files
Calls_From = r"\\path\Current Day Call Raw Data.csv"
Bonus_From = r"\\path\Current Day Bonus Raw Data.csv"
Saves_From = r"\\path\Current Day Saves Raw Data.csv"

# To files
#To = rb"\\usfl04fsx04v.hsus.hsa.int\\data\\Ops Reporting\Management\Raw Data\ " + today.strftime("%Y-%m")
This_month = today.strftime("%Y-%m")
print(This_month)
To = r"\\path\2022-07"
#RawDataFolder = r"\\usfl04fsx04v.hsus.hsa.int\data\Ops Reporting\Management\Raw Data\{This_month}\*.csv"
#import glob 
#print(glob.glob(RawDataFolder))
print("Moving raw data files for MTD.")


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
os.rename(r"\\another_path\2022-07\Current Day Call Raw Data.csv", 
          r"\\another_path\2022-07\Calls Data " + today.strftime("%Y-%m-%d") + ".csv") #yyyy-mm-dd)
print("Calls renamed")
os.rename(r"\\another_path\Current Day Bonus Raw Data.csv", 
          r"\\another_path\Raw Data\2022-07\Bonus Data " + today.strftime("%Y-%m-%d") + ".csv") #yyyy-mm-dd)
print("Bonus renamed")
os.rename(r"\\another_path\2022-07\Current Day Saves Raw Data.csv", 
          r"\\another_path\2022-07\Saves Data " + today.strftime("%Y-%m-%d") + ".csv") #yyyy-mm-dd
print("Saves renamed")