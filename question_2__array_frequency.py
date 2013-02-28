################################################################################
# Question 2: Given an array of integers, write some code to find all the 
# integers that appear more than once in the array, sorted by which appears 
# most often to least often (once) 
#
# Solution Approach : Used Counter function of the collection class 
# A Counter is a dict subclass for counting hashable objects. 
# It is an unordered collection where elements are stored as dictionary keys
# and their counts are stored as dictionary values. 
#
#################################################################################

# Importing Counter function from collection class

from collections import Counter
import sys


# Function to calculate the frequency of elements and print them in sorted order 

def calculate_frequency_of_elements(array):
 frequency_of_elements = Counter ()			   # Initializing a variable of type counter

# Scanning the array to calculate frequency of each unique element and storing it in the variable

 for element in array:
  if not isinstance(element,basestring):       # To check if any element is a string
   frequency_of_elements[element] +=1
  else:
   print "The array contains string objects"
   sys.exit()									# If there is a string element the program will stop and throws an error message
     
 print "The list of elements with frequencies highest to lowest are:",list(frequency_of_elements.keys())
 
 
 
# Main function to take input and intial type and empty set checks
def main():
  
 input_array_of_integers= []                                                                  # Define an empty list 
 try:
   input_array_of_integers = input("Please enter an array of integers :")					  # Ask input from the user
   
   if isinstance(input_array_of_integers,list) and len(input_array_of_integers)!= 0:  		  # Check whether the input is empty or non list 
       calculate_frequency_of_elements(input_array_of_integers)								  # If input is non empty list function to calculate the frequency is called
   else:
	    print "empty list or type non an array "											  # If the input is empty or non list error message
		
 except :
   print "error ! Try Again"                                                                  # Exception message if the entry is errorneous 
   
# Main function called
if __name__ == "__main__":
    main()