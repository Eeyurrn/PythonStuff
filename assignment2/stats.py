#! /usr/bin/env python
import sys
import Enrol
import os
"""Called when Invalid arguments are passed, prints error message and exits gracefully"""
def badArgument():
	print "Invalid Arguments, please enter no arguments OR --student <studentnumber>.  Exiting" 
	sys.exit(0)
"""Stats script gets all classes or queries a students enrolment"""
arguments = sys.argv[1:]
#print os.environ

ENROLDIR_key = "ENROLDIR"

if ENROLDIR_key in os.environ:
	print "ENROLDIR Variable is set"
else:
	os.environ["ENROLDIR"]="data"
	
ENROLDIR =os.environ["ENROLDIR"]
en = Enrol.enrol(ENROLDIR)

#No arguments
if len (arguments) <1:
	allsubjects = [ i[0] for i in Enrol.readtable(en.directory+os.sep+"SUBJECTS")]
	#print allsubjects

	subInfo=[]

	for sub in allsubjects:
		temp = [sub]
		temp.append(filter(lambda a:a[0]==sub,Enrol.readtable(en.directory+os.sep+"SUBJECTS"))[0][1])
		allrolls =  filter(lambda a: a.startswith(sub) and a.endswith(".roll"),os.listdir(en.directory))
		temp.append(len(allrolls))
		if len(allrolls) <1:
			temp.append(0)		
			subInfo.append(temp)
			continue 
		allclassInfo=[]
		for i in allrolls:
			hurr =  en.classInfo(i[:i.rfind(".roll")])
			
			allclassInfo.append(hurr)
		#adds up the total student population for each subject	
		totalstudents = reduce(lambda a,b: len(a)+len(b), map(lambda a: a[4], allclassInfo))
		#bit of hacky code, reduce function will return a list if there is only one class of the subject type, thus detect whether it is a list and then take the length
		if type(totalstudents) == type([]):
			totalstudents = len(totalstudents)
		temp.append(totalstudents)
		subInfo.append(temp)

		
	print "Subjects are:"
	for line in subInfo:
		print"{0:>6}  {1:<35} classes: {2:>3} students: {3:>3}".format(line[0], line[1],line[2],line[3])
		
elif arguments[0] == "--student":
	try:
	
		thestudent = arguments[1]
	except IndexError:
		badArgument()
	#go through subjects to get relevant rolls
	allsubjects = [ i[0] for i in Enrol.readtable(en.directory+"SUBJECTS")]
	#for each subject check if roll exists
	allrolls = []
	for subj in allsubjects:		
		allrolls.extend(filter(lambda a: a.startswith(subj) and a.endswith(".roll"), os.listdir(en.directory)))
	
	classesenrolled = [ hurr  for hurr in filter(lambda a:thestudent in Enrol.readlines(en.directory+a),allrolls)]
	
	classoutput=[]
	for i in classesenrolled:
		try:
			temp=[]
			i = i[:i.rfind(".roll")]
			temp.append( i.split(".")[0])
			#grab the class name from classfile
			temp.append(filter(lambda a: temp[0] in a,Enrol.readlines(en.directory+"SUBJECTS"))[0].split(":")[1])
			#get the time and venue from CLASSES file
			temp.extend(filter(lambda a: a.startswith(i)  ,Enrol.readlines(en.directory+"CLASSES"))[0].split(":")[2:-1])
			#get class info
			classoutput.append(temp)
		except Exception:
			pass
	
	for line in classoutput:
		print"{0:>6}  {1:<35}  {2:<10} @ {3:>3}".format(line[0], line[1],line[2],line[3])
	
else:
	badArgument()
	
