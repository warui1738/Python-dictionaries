# my_profile = {"name":"Godson","gender":"male","status":"single"}
# my_profile["status"]="married"
# del my_profile["gender"]
# print(my_profile)
# elements ={
#    1:"Hydrogen",2:"Helium",3:"Lithium",4:"Berrylium",
#   5:"Boron",6:"Carbon",7:"Nitrogen",8:"Oxygen",
#    9:"Flourine",10:"Neon",11:"Sodium",12:"magnesium",
#   13:"Alumininum",14:"Silicon",15:"Phosphorus",16:"Sulphur",17:"Chlorine",18:"Argon",19:"Potassium",20:"Calcium"
#  }
# while True:
#   element_position = int(input("Enter the elements position(1-20):"))
#   if element_position ==None:
#      break
#   else:
#     print(element_position,":",elements[element_position])


# my_result ={
#   "Bible":45,
#   "Acct":24,
#   "Bmgt":67,
#   "coms":54,
#   "comps":79,
#   "math 100":15
# }
# for courses in my_result:
#   print(courses,":",my_result[courses])


Phonebook={}
while True:
  Phonename = str(input("Please enter the name: to the phonebook:"))
  Phonenumber = int(input("Please enter the name to the Phonebook:"))
  if Phonename and Phonenumber == None:
    break
  else:
    Phonebook[Phonename] = Phonenumber
    print(Phonebook)