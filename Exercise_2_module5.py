import random # import random library
class film: # define class film with parameters and methods
   def __init__(self,title, release_date, category, broadcast_num):
       self.title = title
       self.release_date = release_date
       self.category = category
       self.broadcast_num= broadcast_num
       
   def play_film(self): # definition of play method for film only
         a = int(self.broadcast_num) # use a temporary variable to store the broadcast number in integer format
         a = a+1 # increament the variable by 1
         self.broadcast_num = str(a) # convert a new value in string format to store it in a broadcast number
         print(self.title,self.release_date)

 
   def play(self): # definition of play method
       a = int(self.broadcast_num)# use a temporary variable to store the broadcast number in integer format
       a = a+1 # increament the variable by 1
       self.broadcast_num = str(a)# convert a new value in string format to store it in a broadcast number
       
class serie(film): # inherit from the class film
     def _init_(self,serie_num, season_num, *args, **kwargs):
      super(serie, self).__init__(*args, **kwargs)# using function super for inheritence
#(class can use the methods and parameters from film)
     
     def play_serie(self): # definition of play method for serie only
         a = int(self.broadcast_num)
         a = a+1
         self.broadcast_num = str(a)
         print(self.title,"S",self.season_num,"E",self.serie_num)
         
library = []   # creation of an empty list for a library

#--------------------------------------------------------------------------------
def get_movies(): # the aim of this function is to collect all film from the library list
# and sort the titles in alphabetical order
  Get_movies =[] # empty list for temporary storage of films only
  for i in range(len(library)): # loop to go trough the library list
    if type(library[i]) == film: # use the function type to return variable data type,
#it helps to differentiate between film and serie
        Get_movies.append(library[i].title)#  adding the films titles to the list Get_movies
    
  print(Get_movies)# print the list of films
  print()
  Get_movies.sort() # sort films titles in alphabetical order
  print(Get_movies) # display the sorted titles
#------------------------------------------------------------------------------------------------  
def get_series(): # the aim of this function is to collect all series from the library list 
#and sort the titles in alphabetical order
  Get_series =[] # empty list for temporary storage of series only
  for i in range(len(library)): # loop to go trough the library list
    if type(library[i]) != film: # use the function type to return variable data type, 
  #it helps to differentiate between serie and films
        Get_series.append(library[i].title)#  adding the series titles to the list Get_series
  print(Get_series)# print the list of series
  print()
  Get_series.sort() # sort films titles in alphabetical order
  print(Get_series) # display the sorted titles
 #--------------------------------------------------------------
def generate_views(): # define function generate_views to display the elements 
# randomly a value between 1 and 100 
  r1 = random.randint(1,100)
  W = library[random.randint(0,len(library)-1)] # randomly check the element from the list libarary
  # print(W.broadcast_num)
  W.broadcast_num = str(r1 +int(W.broadcast_num))
  # print(r1)
  # print(W.broadcast_num)
#-------------------------------------------------------------------------------------

def generate_views_10times():# define function generate_views_10times
   for i in range(9): # loop to go trough the list 10 times 
       generate_views()
#---------------------------------------------------------------------------------------------
def top_titles(): # define a function to dispaly the title of film or serie broadcasted the most number of times
   Titles = [] # empty list to add the titles of films and series
   Broadcast = [] # empty list to add the number of broadcast
   
   for i in range(len(library)-1):
       Titles.append(library[i].title) # add titles of films or series to the list Titles
       Broadcast.append(int(library[i].broadcast_num)) # add the number of broadcast of films or series to the list Broadcast
   
   list_x =dict(zip(Titles, Broadcast))  # create dictionnary to add 2 elements of the lists Titles and Broadcast
   print(list_x)
   list_x_sorted = dict(sorted(list_x.items(), key=lambda item: item[1])) # sort the dictionary to display the title of film or series broadcasted the most of times
   print(list_x_sorted)
   print()
   print("The top title is: ", list(list_x_sorted.keys())[-1]) # print the last element of the dictionary
   print()
   f = list(list_x_sorted.keys())[-1] # copy the last element of the dictionary list_x_sorted in the variable f
   #the last element in dictionary list_x_sorted is the last title broadcasted the most number of times
   for i in range(len(library)-1):  #use loop function to go trough the titles of films and series in the library list
          if library[i].title == f: # compare titles in library with the variable f
             content_type = type(library[i])# copy the type of element from the library in the variable content_type if f is in the library
   if content_type == film: #if the content_type is a film, we print the following message: "The top title is a film"
     print("The top title is a film")
   else: # if the content_type is not a film, we print the message: "The top title is a serie")
     print("The top title is a serie")
   
#------------------------------------------                               
def search(text):  # using the seearch function
    Search = [] # empty list for temporary storage of films and series titles
    flag = 0    # define a variable with 0 value
    for i in range(len(library)): # loop to go trough the library list
      if library[i].title == text: # use the function type to return variable data type- title
          Search.append(library[i].title)# adding the titles of films and series to the list Search
          flag = 1 # define a variable (title of film or serie) that is in the library
    if flag != 1: # define a variable that is not in the library
        print("error - the title is not in the library") # display error message
        return # end the executon of the function
    print(Search) #display the result of the search function
#---------------------------------------------------------------------  
#----------------------------------------------------------------------

film1 = film("Pride and Prejudice","1995","romance", "70") # creation of the database of the film
library.append(film1) # adding the title of the film to the library
#film1.play_film()# increament number of broadcast
film3 = film("Red Notice", "2021","action","66")
library.append(film3)
film4 = film("Hater","2020", "thriller", "15")
library.append(film4)
film5 = film("The War Below","2021","drama","40")
library.append(film5)
    
         
film2 = serie("Succession","2018", "comedy-drama","90")# creation of database of the series
library.append(film2) # adding the series to the library
film6 = serie("The Fall", "2013", "thriller", "20")
library.append(film6)
film7 = serie("Traitors", "2019", "drama", "30")
library.append(film7)
film8 = serie("Marcela", "2016", "mystery", "50")
library.append(film8)

film2.serie_num = "01"
film2.season_num = "02"

# get_series()
#print (type(film8))
# search("The War Below")# test
#generate_views()
generate_views_10times()
top_titles()