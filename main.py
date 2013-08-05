import praw
import time
from console import *
import ini
from __main__ import *

r = praw.Reddit('Link Fixer Bot v2.3.1 - by /u/Dominoed')
r.login('LinkFixerBot2','TheBotPassword')
cprint('Link Fixer Bot v2.3.1 Initiated!')
already_done = set()
bannedsubs = set()
bannedsubs.add('pics')
bannedsubs.add('funny')
bannedsubs.add('DebateAChristian')
bannedsubs.add('answers')
bannedsubs.add('aww')
bannedsubs.add('science')
bannedsubs.add('news')
bannedsubs.add('gifs')
bannedsubs.add('GirlGamers')
bannedsubs.add('IAmA')
bannedsubs.add('gaming')
bannedsubs.add('AdviceAnimals')
errorlog = 0
def hasend(string):
  'Check if link is the end of comment.'
	string.replace(' ', '?')
	if (string.count('*')+string.count(':')+string.count('-')+string.count('.')+string.count('!')+string.count("'")+string.count('/')+string.count('?')+string.count(',')+string.count('|')+string.count('+')+string.count(')')+string.count('(')+string.count(']')+string.count('[')) > 0:
		return True
	else:
		return False
def getspace(s):
	s = s.replace(' ','?')
	s = s.replace('.','?')
	s = s.replace(',','?')
	s = s.replace('|','?')
	s = s.replace('+','?')
	s = s.replace('(','?')
	s = s.replace(')','?')
	s = s.replace('!','?')
	s = s.replace("'",'?')
	s = s.replace('/','?')
	s = s.replace('[','?')
	s = s.replace(']','?')
	s = s.replace(':','?')
	s = s.replace('-','?')
	s = s.replace('*','?')
	return s.find('?')
def makecom(comment,types):
	'Reply to the comment.'
	if types == 'user/':
		comment.body = comment.body.replace('user/','u/',1)
		types = 'u/'
	link_start = comment.body[comment.body.find(types)+2:]
	islinkfull = comment.body[comment.body.find(types)+2].isalnum()
	if not islinkfull and link_start == '_':
		islinkfull = True
	if islinkfull:
		if hasend(link_start):
			time.sleep(0.1)
			link_after = getspace(link_start)+2+comment.body.find(types)
			link_before = comment.body.find(types)
			link_full = '/'+comment.body[link_before:link_after]
			if link_full[3:] != comment.subreddit.display_name:
				comment.reply(bcomment(link_full))
				return link_full
			elif link_full[:3] == '/r/':
				cprint('Broken link just links to the subreddit it is in.')
				print(comment.permalink)
				return 'False'
			else:
				comment.reply(bcomment(link_full))
				return link_full
		else:
			time.sleep(0.1)
			link_after = leng(comment.body)+1
			link_before = comment.body.find(types)
			if link_start.count(' ') > 0:
				cprint('Weird exception. Adding Comment.')
				link_after = getspace(link_start)+2+comment.body.find(types)
				link_full = '/'+comment.body[link_before:link_after]
			link_full = '/'+comment.body[link_before:link_after]
			if link_full[3:] != comment.subreddit.display_name:
				comment.reply(bcomment(link_full))
				return link_full
			elif link_full[:3] == '/r/':
				cprint('Broken link just links to the subreddit it is in.')
				print(comment.permalink)
				return 'False'
			else:
				comment.reply(bcomment(link_full))
				return link_full
	else:
		cprint('Broken link is empty.')
		return 'False'
def checkcom(comment,types):
	'Check through different reddit links.'
	if comment.body.count(types) > 0:
		if comment.body.find(types) == 0:
			return True
		else:
			if comment.body[(comment.body.find(types)-1):(comment.body.find(types))].isspace():
				return True
	else:
		return False
def getcom():
	'Get comment from reddit.com/comments'
	global errorlog
	allc = r.get_comments('all')
	cprint('Searching for comments')
	try:
		for comment in allc:
			if comment.id not in already_done:
				already_done.add(comment.id)
				if (comment.body.count('u/')+comment.body.count('r/'))+comment.body.count('user/') > 0:
					cprint('Potential comment found. Checking if comment is valid.')
					time.sleep(0.1)
					if comment.body.count('u/')+comment.body.count('r/')+comment.body.count('user/') > comment.body.count('/u/')+comment.body.count('[u/')+comment.body.count('/r/')+comment.body.count('[r/')+comment.body.count('/user/')+comment.body.count('[user/'):
						if comment.subreddit.display_name not in bannedsubs:
							if checkcom(comment, 'r/'):
								cprint('Broken /r/ link found! Fixing link.')
								comty = makecom(comment, 'r/')
								if comty != 'False':
									cprint(comty+' comment added!')
									time.sleep(1)
								else:
									cprint('Ignoring and checking comments again.')
							elif checkcom(comment, 'u/'):
								cprint('Broken /u/ link found! Fixing link.')
								comty = makecom(comment, 'u/')
								if comty != 'False':
									cprint(comty+' comment added!')
									time.sleep(1)
								else:
									cprint('Ignoring and checking comments again.')
							elif checkcom(comment, 'user/'):
								cprint('Broken /user/ link found! Fixing link.')
								comty = makecom(comment, 'user/')
								if comty != 'False':
									cprint(comty+' comment added!')
									time.sleep(1)
								else:
									cprint('Ignoring and checking comments again.')
							else:
								cprint('Invalid comment.')
								time.sleep(0.5)
						else:
							cprint('Comment is in a banned subreddit (/r/'+comment.subreddit.display_name+'). Checking again.')
					else:
						cprint('Invalid comment.')
						time.sleep(0.3)
	except Exception as error:
		cprint('There was an un-encountered-before-error.')
		cprint('Logging error now.')
		errorlog = logerror(error, errorlog)
		time.sleep(3)
		cprint('Error logged as #'+str(errorlog))
	time.sleep(2)
while True:
	getcom()
