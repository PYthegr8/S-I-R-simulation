''' Papa Yaw Owusu Nti
    September 14th, 2023
    CS152 B 
    Project 01
    This program prints the sum and avg of 3 numbers
'''  

print('version1')
print ('sum', 41+21+5)
print ('avg', (41+21+5)/3) #floating point division 



print('version2')
print ('sum', 41+21+5)
print ('avg', (41+21+5)//3) #tells python that the division should be integer division



print('version3')
print ('sum', 41+21+5.0)
print ('avg', (41+21+5)//3.0) 


print('version4')
a=42
b=21
c= 5
print ('sum', a+b+c)
print ('avg', (a+b+c)//3.0) 



print('version5')
S0= 99
I0= 1
R0= 0
print("Population size: ", S0+I0+R0)




print('version6')
S0= 99
I0= 1
R0= 0

def compute_population_size(S0, I0, R0):
    '''This function  computes the total population size of the simulation by summing the S0,R0 and I0'''
    print("Population size: ", S0+I0+R0)

compute_population_size(S0, I0, R0)
compute_population_size( 20, 20, 10 )
compute_population_size( 8, 16, 1 )




print('version7')
S0= int(input('Enter the SO for this simulation: '))
I0= int(input('Enter the IO for this simulation: '))
R0= int(input('Enter the RO for this simulation: '))

def compute_population_size(S0, I0, R0):
    '''This function  computes the total population size of the simulation by summing the S0,R0 and I0'''
    print("Population size: ", S0+I0+R0)

compute_population_size(S0, I0, R0)





print('version8')
S0= int(input('Enter the SO for this simulation: '))
I0= int(input('Enter the IO for this simulation: '))
R0= int(input('Enter the RO for this simulation: '))

def compute_population_size(S0, I0, R0):
    '''This function  computes the total population size of the simulation by summing the S0,R0 and I0'''
    return S0+I0+R0

population_size= compute_population_size(S0, I0, R0)

print('Population size:', population_size)




