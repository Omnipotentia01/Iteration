#N factorial.
#Tommy Cakebread

n = int(input("Please enter a number: "))
for count in range(1,n):
    product = (count)*(count+1)
    #print (product)
    
print ("The n factorial (n!) is equal to {0}".format(product))
    
