import time
import ini

def leng(stri):
  'Get length of a string easier.'
	return stri.__len__()
def cprint(msg):
	'Print a console message.'
	print(bprint()+msg)
def bprint():
	'Return a "console" prefix.'
	c_time = time.strftime('%H:%M:%S', time.localtime())
	cp = '['+c_time+']'+'<Console> '
	return cp
def bcomment(msg):
	'Add pre-made suffix to the comment.'
	return (msg+'''

***

^I ^am ^an [^automatic ^bot](http://reddit.com/r/LinkFixerBot2/)^. ^If ^I ^have ^made ^a ^mistake ^or ^you ^see ^a ^bug, ^**please** ^contact ^my [^author](http://www.reddit.com/message/compose/?to=Dominoed&subject=LinkFixerBot2&message=Hello!%20%3CInsert%20comment%20about%20bug%20here%3E)^.''')
def logerror(error,errorlog):
	'Log an encountered error. error is the error, errorlog is the error number.'
	#Because why not Military time?
	errortime = time.strftime('%H'+'%M and %S seconds', time.localtime())
	errorlog += 1
	errorname = 'Error #'+str(errorlog)
	errorfile = 'errors.ini'
	ini.write(errorfile,errorname,'Time of Error',errortime)
	ini.write(errorfile,errorname,'Error Name',error)
	return errorlog
