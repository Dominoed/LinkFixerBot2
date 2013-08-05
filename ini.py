import configparser

def write(ifile,isec,ikey,ival):
	'Write to ini file'
	config = configparser.ConfigParser()
	config[isec] = {ikey:ival}
	with open(ifile,'w') as configfile:
		config.write(configfile)
def writemp(ifile,isec,ikey):
	'Write to ini file'
	config = configparser.ConfigParser()
	config[isec] = {ikey}
	with open(ifile,'w') as configfile:
		config.write(configfile)
def read(ifile,isec,ikey):
	'Read from ini file'
	config = configparser.ConfigParser()
	config.read(ifile)
	return config[isec][ikey]
def secexists(ifile,isec):
	config = configparser.ConfigParser()
	config.read(ifile)
	return isec in config
def keyexists(ifile,isec,ikey):
	config = configparser.ConfigParser()
	config.read(ifile)
	return ikey in isec in config
