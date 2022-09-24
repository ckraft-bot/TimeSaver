import os #comes with python
from pathlib import Path #comes with python
import win32com.client  #pip install pywin32
import datetime

today = datetime.date.today()

def save_attachemnts(messages,today,path): 
    for message in messages:
        # Python checking for two conditions, mail read status and sent date, checks if either conditions are met
        if message.Unread or message.Senton.date() == today: 
            # defining attachments
            attachments = message.Attachments 
            # quantifying how many attachments are expected
            attachment = attachments.Item(1) # if i only get one excel attachement in the mail
            # a loop that says if an attachment is detected then save in the file path as defined later in the def main()
            for attachment in message.Attachments:
                attachment.SaveAsFile(os.path.join(path, str(attachment)))
                # Once the unread message is opened by Python then mark the message as READ.
                if message.Unread:
                    message.Unread = False # marked as "Read"
                break              


def main():
    path = r"\\path\Contact Center Reporting\Misc\Project Dump\Deploy Attachments"
    today = datetime.date.today()
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI") #GetNameSpace ("MAPI") returns the Outlook NameSpace object from the Application object.
    inbox = outlook.GetDefaultFolder(6)  
    # Docemendation on codes associated with Outlook folders: https://docs.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders
    subFolder = inbox.Folders("My Team")
    #"My team" is a sub folder in my main "Inbox" which contains all emails from team members.
    subFolderMessages = subFolder.Items 
    messages = subFolderMessages
    save_attachemnts(messages,today,path)
    print ("Attachemnts saved, yay you saved like 5 seconds!") 

    import shutil
    upzip_this = r"Some_File_path\File_name.XLS.zip"
    unzipped = r"C:\Users\Downloads\Folder_name"
    shutil.unpack_archive(upzip_this, unzipped)
    print("File unzipped.")

    # move unzipped file to final destination path
    # shutil.move() will override the old ready_file from yesterday
    unzipped_file = unzipped
    ready_file = r"C:\Users\Downloads\Folder_name\Subfolder_name\File_name.XLS"
    shutil.move(unzipped_file,ready_file)
    
if __name__=="__main__":
    main()
