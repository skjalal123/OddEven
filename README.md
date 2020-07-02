# OddEven
In this program I write code for oddEven Function. of a no. sequence. In this code I use polynomial equation to print the calculate the Odd Even. So that it reduce the process time to find Odd Even no. of sequence.

Lets Consider
I want Even no. from 1 to 100
so I have to run a loop for 100 times to print the Even no. with following code

for i in range(1,100+1):
  if (i%2==0):
    print(i)
    
same for Odd no.

for i in range(1,100):
  if(i%2==1):
    print(i)
    
 In these code loop run 100x time to check odd or Even.
 
 So i use polynomial equation to reduce loop time
 
 instead of if statement write 
 #2*i for Even no and 2 * i + 1 for Odd no.
 
 so that if I want calculation from 1 to 100
 so I will divide the no. by two mean 100 / 2 = 50
 and I pass 50 inside the loop so that loop will run for 50x times but 
 It return result for 100
 
 
 
 Thank U
