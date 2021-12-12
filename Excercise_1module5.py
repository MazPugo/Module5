from faker import Faker  # import faker library
fake = Faker()
fake.first_name()
fake.last_name()
fake.email()
fake.phone_number()
fake.company()
fake.job()

class card:
   def __init__(self, visit_card, first_name, last_name, company_name, job_title, email_address):
       self.visit_card = visit_card
       self.first_name = first_name
       self.last_name = last_name
       self.company_name = company_name
       self.job_title = job_title
       self.email_address = email_address
       
       
   def contact(self): # displaying the contact information
        print("The person to contact is ",self.first_name, " ", self.last_name)
        print("The job title is " , self.job_title)
        print("The email address is ", self.email_address)
        
        
   def __repr__(self): # using _repr_ method to display the code in interpreter
            return '({}, {}, {}, {}, {}, {})'.format(self.visit_card, self.first_name, self.last_name, self.company_name, self.job_title, self.email_address)

   def length_Name(self):# using the function len to display the number of letters in first and in last name
       #return self.length_Name
       print(len(self.first_name)," ",len(self.last_name) )
      


card1 = card("A", "Beth R", "Gambrell","Plan Smart Partner","Employee welfare manager","BethRGambrell@dayrep.com")
card2 = card("B", "Tomáš","Hronek", "Micro Design", "Chemical plant and system operator","TomasHronek@armyspy.com")
card3 = card("C", "Charles","Regeer", "Nan Duskin", "Data entry keyer", "CharlesRegeer@rhyta.com")
card4 = card("D","Basia",  "Zielinska", "First Choice Garden Maintenance", "HIV/AIDS nurse","BasiaZielinska@teleworm.us")


class Basecontact(card): # inherit from the class card
     def _init_(self,personal_number, *args, **kwargs):
      super(Basecontact, self).__init__(*args, **kwargs)
      
     def contact(self):
        print("I dial the number ", self.personal_number, "I call ",self.first_name, " ", self.last_name)
        
class Businesscontact(Basecontact): # inherit from the Basecontact card
     def _init_(self, company_number, *args, **kwargs):
      super(Businesscontact, self).__init__(*args, **kwargs)
      
     def contact(self):
        print("I dial the number ", self.company_number, "I call ",self.first_name, " ", self.last_name)

Card6 = Basecontact("E", "Baptiste","Paquette", "Komerci", "Job estimator", "BaptistePaquette@armyspy.com")
Card6.personal_number="+48 123456789"
Card7 = Businesscontact("E", "Baptiste","Paquette", "Komerci", "Job estimator", "BaptistePaquette@armyspy.com")
Card7.company_number="+48 453456777"
Card6.contact() 

print()
Card7.contact()  # "Contact method" is defined in the class card
print()
Card7.length_Name()   
newcard = [] # empty list will be used to save newly created cards
def create_card(card_type, num):
 # if card_type == "Basecontact" or card_type == "Businesscontact":
      for a in range(num):
       new = card_type(a,fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.email())
       newcard.append(new) # adding the information from "new" to the newcard list
create_card(Basecontact, 5)# create a function to generate random visit cards and quantity of cards using the data from faker
