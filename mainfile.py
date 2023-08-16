import imaplib
import email, getpass, sys, time, re
from bs4 import BeautifulSoup
def animated_please_wait():
    animation = "|/-\\"
    i = 0
    while True:
        sys.stdout.write("\rPlease wait..." + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.15)
        i += 1

        if i == 10:
        	break

def load_animate():
	try:
		animated_please_wait()
	finally:
		sys.stdout.write('\rDone...')
		sys.stdout.write('\r')

def mail_type():
	m_no = None
	try:
	    print("Select type of Mail:\n1.Gmail\n2.YahooMail\n3.Outlook\n4.Fastmail\n5.Apple_Icloud")
	    m_no = int(input("Choose number: "))
	except:
		print("Wrong Input, Try again..")
		mail_type()
	else:
		return m_no

def get_user_pass():
	name = None; pwd = None
	try:
		name = str(input("Your email: "))
		pwd = getpass.getpass("Your password: ")
	except:
		print("Wrong_Input")
		get_user_pass()
	return name, pwd

def read_no_of_emails(length):
	n = None
	try:
		n = int(input("Enter number of mails to read: "))
	except:
		print("Wrong Input, Try again")
		read_no_of_emails()
	
	if n > length:
		read_no_of_emails(length)
	else:
		return n
def spec_mail_to_read():
	name = None
	try:
		name = str(input("Insert name of mail to be read: "))
	except:
		spec_mail_to_read()
	return name


def find_tag(html_content, name_of_tag):
	soup = BeautifulSoup(html_content, 'html.parser')
	soup.findall(name_of_tag)

def load_mail():
	m = None
	try:
		mail = imaplib.IMAP4_SSL(mail_imap.get(select_mail))
		m = mail
		confirm_login(mail)
	except imaplib.IMAP4.error:
		print(sys.exc_info()[1])
		load_mail()
	else:
		mail.select('INBOX')
		return m

def confirm_login(mail):
	name, pwd = get_user_pass()
	mail.login(name, pwd)

mail_imap = {1:'imap.gmail.com', 2:'imap.mail.yahoo.com', 
3:'outlook.office365.com',
4:'imap.fastmail.com',
5:'imap.mail.me.com'}


BODY = []
select_mail = mail_type()
load_animate()

mail = load_mail()
status, email_ids = mail.search(None, f'ALL FROM {spec_mail_to_read()}')
email_id_list = email_ids[0].split()

i = 0; l = len(email_id_list)
print("TOTAL MAILS:", l)
val = read_no_of_emails(l)

for email_id in email_id_list:
	status, msg_body = mail.fetch(email_id, '(RFC822)')
	msg = email.message_from_bytes(msg_body[0][1])

	subject = msg['subject']; from_address = msg['from']; date = msg['date']

	#print(f"Subject: {subject}")
	#print(f"From: {from_address}")
	#print(f"Date: {date}")

	if msg.is_multipart():
		for part in msg.walk():
			if part.get_content_type() == "text/plain":
				body = part.get_payload(decode=True).decode("utf-8")
				BODY.append(body)
				#print("Body:", body)
	else:
		body = msg.get_payload(decode=True).decode("utf-8")
		BODY.append(body)
		#print("Body:", body)

	#print("=====")
	i += 1
	if i == val:
		break






