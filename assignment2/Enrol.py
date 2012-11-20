#Assignement for s3222417, please forgive my liberal use of lambdas, maps and filters 
import os

class enrol(object):
	"""Enrolment Class which contains functions necessary to enrol, and retrieve data from basketweaving department"""
	def __init__(self,directory):
		"""Constructor for enrolment class takes the directory where data files are stored as an argument"""
		self.directory = os.path.abspath(directory)+os.sep
		self.students =[]

	def subjects(self): 
		"""Returns list of the subject codes in SUBJECTS file"""		
		return[line[0]for line in  readtable(self.directory+"SUBJECTS")]
	
	def subjectName(self,subj):
		""""""
		subs = readlines(self.directory+"SUBJECTS")
		#Lambda function to match substring, filter to iterate through subject list
		cmp = lambda a : a.find(subj)!= -1
		results = filter(cmp, subs)		
		if len(results)==0:
			raise KeyError("Subject does not exist in file")
		return results[0].split(":")[1]		

	def classes(self,subj):
		"""Accepts the argument of the subject code and returns all classes using that subject code"""
		allclasses = readlines(self.directory+"CLASSES")
		#lambda function which matches
		qualifier = lambda a: a.find(subj)!=-1
		#filter for matches
		allclasses = filter(qualifier, allclasses)
		#further pull classnames
		allclasses = [derp.split(":")[0] for derp in allclasses]		
		return allclasses

	def classInfo(self,subj):
		"""Accepts Class code and returns tuble in the form of (subjectcode, time, venue, tutor, students)"""		
		thefilename = self.directory+subj+".roll"		
		theclass=filter(lambda a: a.find(subj)!=-1,readlines(self.directory+"CLASSES"))	
		if len(theclass)>0:			
			temp = theclass[0].split(":")[1:]		
			if len(filter(lambda a: a==thefilename,[self.directory+i for i in os.listdir(self.directory)]))>0:			
				return (temp[0],temp[1],temp[2],temp[3],readlines(thefilename))
		else:
			raise KeyError("Class does not exist in file")


	def checkStudent(self,studentID,subjcode=None):
		"""Accepts 2 arguments the Student ID(required) and subject code(optional) If the subject code is passed it returns the class code the 
student is enrolled in. If no subject code is specified returns a list of classcodes student is enrolled in, if the student is 
not enrolled in any classes, the list will be empty """
		if subjcode == None:
			
			#find all the files with .roll at the end. 
			allclasses=filter(lambda a: a.find(".roll")!=-1,os.listdir(self.directory))
			#trawl through all the roll for where the student is, if yes, pop it into the list
			studentlist=[line[0] for line in filter(lambda a: a[1]==True ,map(lambda a:(a,studentID in readlines(self.directory+a)) ,allclasses))]
			#strip .roll from the end
			return map(lambda a:a[:a.rfind(".roll")],studentlist)
		else:
			#grab all class files with subjcode 
			allclasses=filter(lambda a: a.find(subjcode)!=-1,os.listdir(self.directory))
			#find the class with the student inside
			studentlist = map(lambda a: (a,studentID in readlines(self.directory+a)), allclasses)
			#print studentlist
			#return first occurence of class that student is enrolled in, also strip roll from the end
			classEnrolled=[ thing[0][:thing[0].rfind(".roll")] for thing in filter(lambda a: a[1]==True, studentlist)]
			
			if len(classEnrolled)==0:
				return None
			else:
				return classEnrolled[0]
			
	def enrol(self,	studentID,	classcode):
		"""Accepts student ID and Class code, Enrols student in class checking for capacity, removes student from any other classes in that subject if they are enrolled in 
that class"""
		#check class capacity
		rollname = classcode+".roll"
		#check class exists		
		if rollname not  in os.listdir(self.directory):
			raise KeyError("specified class code does not exist")
		theclass = filter(lambda a:a[0]==classcode, readtable(self.directory+"CLASSES"))[0]	
		venue = theclass[3]	
		subject =classcode[:classcode.rfind(".")]		
		
		#check venue capacity		
		if int(len(self.classInfo(theclass[0])[4])) <int( filter(lambda a:a[0]==venue, readtable(self.directory+"VENUES"))[0][1] ):
			if self.checkStudent(studentID,subject )==None:				
				newlist = _readAllLines(rollname)
				newlist.append(studentID)				
				writelines(rollname,newlist)
			else:
				#search through all rolls of subject and remove the student
				
				for rollfile in filter(lambda thing: thing.startswith(subject) and thing.endswith(".roll") , os.listdir(self.directory)):
					temp =_readAllLines(self.directory+rollfile)
					if studentID in temp:
						temp.remove(studentID)
						writelines(rollfile,temp) 
				temp = _readAllLines(self.directory+rollname)
				temp.append(studentID)
				writelines(self.directory+rollname,temp)
			
		else:
			return None		
"""Accepts the filename and returns all the lines without hash prefix """
def	readlines(filename):
	FILE=open(filename,'r')
	FileLines =FILE.readlines()
	#Lambda filters hashes
	qualifier = lambda a: a.find("#")!=0
	#Lamda strips newlines
	clean = lambda a:  a.strip() 
	#filter out comments and then apply the strip newline lambda to them
	FileLines=map(clean, filter(qualifier,FileLines))	
	FILE.close()
	return FileLines
"""Accepts the filename and returns list of lists splitting tokens on the : delimiter """	
def readtable(filename):
	return [line.split(":")for line in readlines(filename)]	
"""Accepts the filename and list of strings, writes file to string"""	
def writelines(filename, lines):
	FILE = open(filename,"w")
	for line in lines:
		FILE.write(line.strip()+"\n")		
	FILE.close()
"""Accepts the filename and returns a list of lines in the file, this one returns them with the lines that have hashes infront of them"""
def _readAllLines(filename):
	FILE=open(filename,'r')
	return [line.strip() for line in FILE.readlines()]