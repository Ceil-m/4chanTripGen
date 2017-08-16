#!/usr/bin/env python
import os, sys, re, string, crypt

def mktripcode(pw):
    pw = pw.decode('utf_8', 'ignore') \
        .encode('shift_jis', 'ignore')    \
        .replace('"', '&quot;')      \
        .replace("'", '')           \
        .replace('<', '&lt;')        \
        .replace('>', '&gt;')        \
        .replace(',', ',')
    salt = (pw + '...')[1:3]
    salt = re.compile('[^\.-z]').sub('.', salt)
    salt = salt.translate(string.maketrans(':;<=>?@[\\]^_`', 'ABCDEFGabcdef'))
    trip = crypt.crypt(pw, salt)[-10:]
    return trip

x=0
y=0
try:
	os.system('clear')
	print "Use after generating: in the 'name' field, type '(NAME)#(CODE)'\n\nIf it pauses, it is searching\n\n4-5 characters max recommended\n"
	code = raw_input('Input the trip to search for: ').lower()
	if len(code) >= 11:
		print 'Max 10 characters'
		exit()
	print '\nsearching...'
except(KeyboardInterrupt):
	os.system('clear')
	exit()

while 1==1:
	try:
		if re.search(str(code),string.lower(mktripcode(str(x))))>-1:
			print '\nCODE:  ',x
			print 'TRIP:   '+mktripcode(str(x))
			file = open('code-dump.txt','a')
			print >> file, '\nCODE:', x, '\nTRIP:', mktripcode(str(x))
			file.close()
		elif x==y:
			#print x
			y=y+100000
		x=x+1
	except(KeyboardInterrupt):
		exit()
	except(TypeError):
		print("TypeError")
		exit()