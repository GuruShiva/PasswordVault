__author__ = 'guru-main-linux'

from passdb import Db  #Import from passdb Class Db


def main ():

    pwd_db = Db() #Initialization of Class
    pwd_db.delete_all()   #To Clear DB. For Testing Purposes. Use only when necessary

    username = raw_input("Enter THe Username To Record: ")
    password = raw_input("Enter the Password To Record: ")
    service = raw_input("Enter The Service To Record: ")
    pwd_db.record_insert(username=username,service=service,password=password) #Insert to DB
    finduser = raw_input("Enter The Username To Find: ") #User search on DB
    pwd_db.lookup(finduser)  #Searching ufor user in DB based in input
    servicename = raw_input("Enter the Services To Find:")
    pwd_db.lookup(servicename)

if __name__=='__main__':
	   main()


#INSERT PICK PROJECT HERE FOR THE MENU. WRITE BETTER CODE!!!!!!