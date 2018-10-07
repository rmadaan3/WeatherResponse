#Name: Rahul Madaan
#Roll No.2017179

#function to get weather response

def weather_response(location, API_key):
	import urllib.request                                                                                #Importing urllib.request module
	url='http://api.openweathermap.org/data/2.5/forecast?q=' +location+'&APPID='+API_key                 #Defining the url of the weather query using user input of location and json string 
	cont=urllib.request.urlopen(url)                                                                     #Storing the content (json string) in cont
	json=cont.read()																					 #Reading and decoding the json string and storing it as a normal string in json
	json=json.decode()	
	return json                                                                                          #The function is returning json(normal string)

# function to check for valid response 
def has_error(location,json):
	location=location.title()																			 #To correct the format of location in order to exactly match it from the json string
	if json.find(location)==-1:																			 #When location is not found, return True (it has error) and false if location is found
		error=True
	else:
		error=False	
	return error                                                                                         #Function is returning error
	
# function to get attributes on nth day
def get_temperature (json,n=0,t='3:00:00'):
	import datetime                                                                                      #Importing datetime module
	cdate=datetime.date.today()																			 #Finding out the current data
	fdate=cdate + datetime.timedelta(days=n)															 #Adding no of days entered by user to the current date to find the date requested by user
	dt=str(fdate)+' '+t                                                                                  #Making dt in the format in which the string (if present) will be found in the json string
	if (json.find(dt)==-1):																				 #Return null if date is not present
		return null
	else:
		q1=json[:json.find(dt)]																			 #slicing the string upto the index where the date has been found
		x=q1.rfind('temp":')																			 #Then finding the location of temp from reverse
		y=q1.find(',',x)																				 #finding the comma next to temp
		z=q1[x+6:y]																						 #slicing the exact value of temperature from the string
		z=round(float(z),2)																				 #rounding off the exact float value with decimal values upto 2 points
		return z																						 #return the value of temp
		
def get_humidity(json, n=0, t='3:00:00'):																 #Similar functions are defined below to get different parameters regarding the weather
	import datetime
	cdate=datetime.date.today()
	fdate=cdate + datetime.timedelta(days=n)
	dt=str(fdate)+' '+t
	if (json.find(dt)==-1):
		return null
	else:
		q1=json[:json.find(dt)]
		x=q1.rfind('humidity":')
		y=q1.find(',',x)
		z=q1[x+10:y]
		z=int(z)																						 
		return z																						  

def get_pressure(json, n=0, t='3:00:00'):
	import datetime
	cdate=datetime.date.today()
	fdate=cdate + datetime.timedelta(days=n)
	dt=str(fdate)+' '+t
	if (json.find(dt)==-1):
		return null
	else:
		q1=json[:json.find(dt)]
		x=q1.rfind('pressure":')
		y=q1.find(',',x)
		z=q1[x+10:y]
		z=float(z)
		return z 
	
def get_wind(json, n=0, t='3:00:00'):
	import datetime
	cdate=datetime.date.today()
	fdate=cdate + datetime.timedelta(days=n)
	dt=str(fdate)+' '+t
	if (json.find(dt)==-1):
		return null
	else:
		q1=json[:json.find(dt)]
		x=q1.rfind('speed":')
		y=q1.find(',',x)
		z=q1[x+7:y]
		z=float(z)
		return z 
	
def get_sealevel(json, n=0, t='3:00:00'):
	import datetime
	cdate=datetime.date.today()
	fdate=cdate + datetime.timedelta(days=n)
	dt=str(fdate)+' '+t
	if (json.find(dt)==-1):
		return null
	else:
		q1=json[:json.find(dt)]
		x=q1.rfind('sea_level":')
		y=q1.find(',',x)
		z=q1[x+11:y]
		z=float(z)
		return z