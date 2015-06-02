__author__ = 'kennedy klunwebale@gmail.com'


class Pesapi:


  def __init__(self):

    return;
    #    This method returns the balance of the mpesa account at the specified point in time.
	#	 If there are not transactions later than the specified time, then we can not gurantee 100%
	#	 that is is the exact balance - since there might be a transaction prior to the specified time
	#	 which we have not yet been informed about.
	#    The specified time is represented in a unix timestamp.

  def availablebalance(self,time,identifier=""):
      amount =0


      return amount;

      #Locate a particular transaction using the unique reciept number
      #that is send to the mobile user.
      #It is expected that this method will be the primary method used
      #for e-commerce shops
      #For extra security you might consider confirming that the phonenumber
      #of the returned transaction match the users phonenumber.

  def locateByReceipt(self,receipt, identifier = ""):
       transactions =[]
       return transactions;

       #This method locates all payments performed by a given phonenumber
       #within a given time-period (all payments from a particular phone).
       #If at all possible try not to use an until value all the way up
       #until now since that will greatly enhance performance.
def locateByPhone(self,phone, identifier = "",dfrom=0,until=0):
       transactions =[]
       return transactions;

     #this method locates all the payments by a specific client name
	 #within a given time-period. The name is the name that Mpesa
	 #has in its database.
	 #Be alert that mobile users might have there records changed i.e.
	 #if Safaricom mistyped there name.

def locateByName(self,name, identifier="", dfrom=0, until=0):
      transactions =[]
      return transactions;

   # The method locates all payments within a particular time interval
   # plain and simple.

def locateByTimeInterval(self,dfrom,until, type):
	transactions =[]
  	return transactions;

   # This method determines the different names that have been registered
   # using a given phone number

def  locateName(self,phone):
    names =[]
    return names;

#This method determines the different phone numbers that have been
#used by a person with a given name.
#This might be extended to include someone with a similar name.
def  locatePhone(self,name):
    phones=[]
    return phones;

 # This method performs a syncronisation between the safaricom database
 # and the local database.

def forcesyncronisation():
   return True;

def getErrorCode():
   return 0;

def getErrorMessage():
   return "";


def getAccount(identifier=''):
    accounts =[]
    return accounts;
