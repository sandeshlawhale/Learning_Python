# This file explains how to retrieve and delete emails using IMAP in Python.
# Topics covered:
# 1. Connecting to IMAP server
# 2. Logging into IMAP server
# 3. Selecting folders
# 4. Searching for emails
# 5. Fetching email
# 6. Marking email as read
# 7. Getting email body
# 8. Deleting email
# 9. Disconnecting from IMAP server


# IMAP - used to manage email

# pip install pyzmail36
# pip install imapclient

import imapclient
import pyzmail

# Connect to IMAP server
imapObj = imapclient.IMAPClient(
    'imap.gmail.com',
    ssl=True
)

# Login to account
imapObj.login(
    'your_name@gmail.com',
    'Your_secure_password'
)

# Select inbox folder
imapObj.select_folder('INBOX', readonly=False)

# Search for all emails
UIDs = imapObj.search(['ALL'])

print('Email UIDs:')
print(UIDs)

# Fetch latest email
rawMessage = imapObj.fetch([UIDs[-1]], ['BODY[]', 'FLAGS'])

# Get raw email data
message = pyzmail.PyzMessage.factory(
    rawMessage[UIDs[-1]][b'BODY[]']
)

# Get sender email
print('\nFrom:')
print(message.get_addresses('from'))

# Get subject
print('\nSubject:')
print(message.get_subject())

# Get email body
if message.text_part != None:

    print('\nBody:')
    
    print(
        message.text_part.get_payload().decode(
            message.text_part.charset
        )
    )

# Mark email as read
imapObj.add_flags(UIDs[-1], [b'\\Seen'])

# Delete email
# imapObj.delete_messages([UIDs[-1']])

# Permanently remove deleted emails
# imapObj.expunge()

# Logout and disconnect
imapObj.logout()