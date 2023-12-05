import imaplib


host = 'imap.gmail.com'
user = 'josephbenno2547@gmail.com'
password = 'password'

# connect to host using SSL
imap = imaplib.IMAP4_SSL(host)

## login to server
imap.login(user, password)

imap.select('Inbox')

tmp, data = imap.search(None, 'ALL')
print(data)
print(tmp)
for num in data[0].split():
    tmp, data = imap.fetch(num, '(RFC822)')
    print('Message: {0}\n'.format(num))
    print(data[0][1])
    break


imap.close()
imap.logout()