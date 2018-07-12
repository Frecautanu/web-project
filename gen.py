from datetime import datetime
 
 
def get_userName():
	n = raw_input("Whats your Name? ... ")  
	return n
	
def greet_user(name):
	print 'welcome {}'.format(name)

def get_dob():
	dob = raw_input("What's your date of birth in format m/d/y")  #ask user to input data and return the date
	return dob
def calculate_generation(year):
	gen = 'N/A'
	 #Logic
	 # if year is between 1966 - 1976  return  X
	 # if year is between 1977 - 1994  return  Y
	 # if year is between 1995 - 2012  return  Z

   	if year in range(1966,1976): 
   		return 'generation X'
   	if year in range(1977,1994):
   		return ' generation Y'
   	if year in range (1995,2012):
   		return 'generation Z'
   	return gen
user_name = get_userName() #to store the result from the fucntion  into user_name

greet_user(user_name)

user_dob = get_dob()

print user_dob
# Greet user
# call method get_dob to get user date of birth and store in a varabale user_dob
user_year = datetime.strptime(user_dob,'%m/%d/%Y').year
user_gen = calculate_generation(user_year)

# Pass year to the method calculate_generation to findout generation  same the retult in user_gen
print 'Your name :' + user_name
print 'Your DOB :' + user_dob
print 'Your Generation:' + user_gen
