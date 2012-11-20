#! /usr/bin/env python2.6
import Enrol

e = Enrol.enrol("data")
print "directory is ", e.directory

if( e.checkStudent('1124395','bw101') == 'bw101.1'):
	print "first test passed"
else:
	print "first test failed"

if(e.checkStudent('1125622') == ['bw101.1', 'bw330A']):
	print "second test passed"
else:
	print e.checkStudent('1125622')

print e.enrol('1124395','bw101.2')==1