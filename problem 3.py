#preparing function to calculate pi
def calcullate_pi (n):
     #putting the variables
     pi_overfour =0
     sign=1
     #lopping over the n terms to calculate pi/4
     for i in range (n):
         #calculate one term and this mathematical relationship (2i+1) to make sure that tha denominator is an odd number
         term= sign * (1/(2*i+1))
         # adding the ture we calculated to pi_overfour
         pi_overfour += term
         #switching the sign to calculate the next term
         sign = - sign
     #Multiply by 4 both sides to get the value of pi
     pi=pi_overfour*4
     #returning the value of pi
     return pi
#user input choosing the numbers of terms (n)
n = int(input("Enter a number to calculate pi :"))
#calling the function
the_value_of_pi =calcullate_pi(n)
#print the output to the user recording to n terms
print (f"The value of pi recording to {n} terms is : {the_value_of_pi}")
