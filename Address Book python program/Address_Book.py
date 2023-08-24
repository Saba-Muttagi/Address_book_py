
'''
@Author: Saba Muttagi
@Date: 2023-08-23
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-24
@Title : Address Book Assignment
----------------------------------
  1) Create address book which consists of first name, last name, address, 
  city, state, mobile, email
  (number of address books and the address book name will be taken from 
  user command line)

  2) Edit address book:
    i]Check whether the address book is present or not which you want 
    to edit
    ii]Take 3 choices, like choice=1 is for editing mobile number and 
    choice=2 is for editing email and choice=3 for editing all details in 
    the address book
    
  3)  Delete the address book
  4) & 5) --below--
  6) Display the address book. (in dictionary form or tabular form'''


import re
import json


#--------------1] Creating Address Book------------
address_book={ }
n=int(input("Enter the no of address books to be added:"))

def TheAddress_book():
  def Create_AddressBook():
    for i in range(n):
      name=input("\nEnter book {}'s  name :".format(i+1))
      book={ }
        
      fname=input("Enter your First name: ")  
      book["First name"]=fname

      Lname=input("Enter your Last name :")
      book["Last name"]=Lname

      address=input("Enter your Address :")
      book["Address"]=address

      city=input("Enter City name: ")
      book["City"]=city

      state=input("Enter State name:")
      book["State"]=state


      #------------Pin Code validation--------------
      regex_pin="^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
      while True:
       pincode=input("Enter Pin-code :")
       if (re.fullmatch(regex_pin,pincode)):
        break
       else:
         print("Invalid pin code, Please enter valid pin code")
      book["Pin code"]=pincode


      #------------mobile number validation--------------
      def Mobile():
        pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        while True:
          mobile=input("Enter mobile number :")
          if (re.fullmatch(pattern,mobile)):
           break
          else:
           print("Invalid number, Please enter a valid phone number ")
        book["Mobile"]=mobile
      Mobile()
      
      #---------------------Email validity----------------
      def Email():
        regex_email=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        while True:
          email=input("Enter Email :")
          if (re.fullmatch(regex_email,email)):
            #print(email)
            break
          else:
            print("Invalid email. Please enter a valid email")
        book["Email"]=email
      Email()
      address_book[name]=book
    print("Address book created successfully....!!!!")
    print("_______________________________________________")


   #---------Display Address book-----
    def Display_AddressBook():
      #print(book)
      print("Address book is :\n",address_book)
    Display_AddressBook()



   #---------------Edit address book--------------
    def Edit_AddressBook():
      b=input("Enter book name to edit:")
      print("\nFor Editing address book select your choice from below:")
      print("1:Edit mobile number \n 2:Edit email \n 3:Edit all the details :")
      print("_______________________________________________")
      if b in address_book:
        while True:
          choice=input("Enter your choice :")
          if choice=='':
              break
          elif (choice=='1'):
                Mobile()
                break
          elif (choice=='2'):
                Email()
                break
          elif (choice=='3'):     
                TheAddress_book()
                break
          else:
                print("Incorrect choice...")
        print("__________________________________________")
        print("Edited address book is :")#,address_book)
      else:
        print("Address book not present")
    Edit_AddressBook()
  Create_AddressBook()
TheAddress_book()



#-------Write to JSON file – write the address book details to JSON---------
def Write_tojson():
  json_object=json.dumps(address_book,indent=4)

  with open("sample.json","w") as outfile:
    outfile.write(json_object)
Write_tojson()



  #-------- Read from JSON - Read from the JSON file-----------
def Read_fromjson():
  with open('sample.json','r') as thefile:
   thedata=json.load(thefile)
  print(thedata)
  thefile.close()
Read_fromjson()


#------------Deleting Address book------
def Delete_AddressBook():
  delet_addBook=input("Enter name of address book to delete :")
  if delet_addBook in address_book:
    del(address_book[delet_addBook])
    print("Address book deleted successfully.")
    print("Address book  after changes made is \n:",address_book)  
  else:
    #break
    print("Address book not present..")
Delete_AddressBook()