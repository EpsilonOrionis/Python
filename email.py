# Import modules
import getpass
import imaplib

# Set server address in the server variable
server = 'imap.googlemail.com'

# Set server port in the port variable
port = '993'

# Prompt the following message
print('enter the email address you wish to read the emails from please!')

# Get email address in the username variable
username = input('email address:')

# Create session
mailbox = imaplib.IMAP4_SSL(server,port)

# Get account password in the password variable
password = input('enter your password: ')

# Login
mailbox.login(username,password)
status,count = mailbox.select('Inbox')
status,data= mailbox.fetch(count[0],'(UID BODY[TEXT])')

# Print data
print(data[0][1])

# End
