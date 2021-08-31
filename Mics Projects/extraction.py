import datetime
import os
import win32com.client


path = os.path.expanduser(r"C:\Users\evsairn\Desktop\Finance")
today = datetime.date.today()

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
mailbox = outlook.Folders[1]
inbox = outlook.GetDefaultFolder(6)
emails = inbox.Items
emails.sort("[ReceivedTime]", True)


def saveattachemnts(subject):
    for message in emails:
        print(message.Subject)
        if message.Subject == subject and message.Senton.date() == today:
            # body_content = message.body
            attachments = message.Attachments
            attachment = attachments.Item(1)
            for attachment in message.Attachments:
                attachment.SaveAsFile(os.path.join(path, str(attachment)))
                if message.Subject == subject and message.Unread:
                    message.Unread = False
                exit()

saveattachemnts("Demo")