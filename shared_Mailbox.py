from datetime import date, timedelta
import os
import win32com.client


path = os.path.expanduser(r"\\eapac.ericsson.se\EINGRDFS01\COE_ANALYTICS\HRGO_COE_ANALYTICS\100 SQL SERVER\ITM")
today = date.today()

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.Folders("GFPL Reporting and Analytics").Folders.Item("Inbox")
messages = inbox.Items
subject = "Task_Learning_New_Values"
subject1 = "Task_Learning_SET2WIN"
messages.sort("[ReceivedTime]", True)
sub = False
sub1 = False

max = 2500
for count, message in enumerate(messages):
    if count > max:
        break
    if subject in message.subject or subject1 in message.subject:
        attachments = message.Attachments
        num_attach = len([x for x in attachments])
        for x in range(1, num_attach+1):
            attachment = attachments.Item(x)
            attachment.SaveASFile(path + '\\' + str(attachment))
        if subject in message.subject:
            sub = True
        elif subject1 in message.subject:
            sub1 = True

if sub is False or sub1 is False:
    new_email = win32com.client.Dispatch("Outlook.Application")
    email = new_email.CreateItem(0)
    email.To = "ravjyot.singh.duggal@ericsson.com"
    email.Subject = "Files not found - Python Script"
    if sub is False and sub1 is True:
        email.Body = "Hello,\n\n We are not able to find the Task_Learning_New_Values in Inbox, Please check.\n\n" \
                     "Regards,\nPython Script"
    elif sub1 is False and sub is True:
        email.Body = "Hello,\n\n We are not able to find the Task_Learning_SET2WIN in Inbox, Please check.\n\n" \
                     "Regards,\nPython Script"
    elif sub is False and sub1 is False:
        email.Body = "Hello,\n\n We are not able to find the Task_Learning_New_Values and Task_Learning_SET2WIN" \
                     " in Inbox, Please check.\n\n Regards,\nPython Script"
    email.Display()
