import smtplib
carriers = {
	'att':	  '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':	'@vtext.com',
	'sprint':	'@page.nextel.com',
	'test': '@thesmsworks.net'
}

def send(text,to,subject = None):
	auth = ('twophoton.lab@gmail.com', 'info69000')
	
	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login(auth[0], auth[1])
	message = 'To:{}\r\nSubject: {}\r\n{}'.format(to,subject, text)
	print('the mess is:' , message)
	# Send text message through SMS gateway of destination number
	server.sendmail( auth[0], to, message)
'''	
subject = 'Experiment is done, maafaka!'
text = 'No, just kidding ;)'

#to = '07448281517.senderID{}'.format(carriers['test'])
to = 'keivan.razban@gmail.com'
#send(text,to,subject)
'''