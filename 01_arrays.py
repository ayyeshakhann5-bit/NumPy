import numpy as np

# my_list=[1,2,3,4]
# my_list=my_list*2
# print(my_list)

# array=np.array([1,2,3,4])*10

# print(array)

# array=np.array([[['A','B','C'],['D','E','F' ],['G','H','I']],
#                 [['J','K','L'],['M','N','O'],['P','Q','R']],
#                 [['S','T','U'], ['V','W','X'],['Y','Z',' ']]])
# word=array[0,0,0]+array[1,1,1]+array[2,2,0]
# print(word)

#array[start:end:step]

# array=np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12]])
#ROW SELECTION
#print(array[start:end:step])

#print(array[0])
#print(array[0:3])
#print(array[1:2])
#print(array[1:])
#print(array[0:4:2])
#print(array[::2])
#print(array[2])
#print(array[::-2])
#print(array[::-1])

#COLUMN SELECTION

#print(array[:,0])
#print(array[:,-1])
#print(array[:,-1])
#print(array[:,0:3])
#print(array[:,:3])

#print(array[:,::2])

#print(array[:,1::1])

#print(array[:,::-1])

#SELECTION IN QUADRANTS

#print(array[0:2] [0:2])

#print(array[1:,0:2])

#SCALAR Arithmetic

# array=np.array([1,2,3])
# # print(array+1)
# print(array ** 5)

#Vectorized math func

#array=np.array([1,2,3])

#print(np.sqrt(array))

#Excercise
# radii=np.array([1,2,3])

# print(np.pi * radii ** 2)

#Element-Wise arithmetic

# array1=np.array([1,2,3])
# array2=np.array([5,6,7])
# print(array1+array2)

#Comparison operators

# scores=np.array([100,20,700])

# print(scores==100)

# scores[scores<60]=0

# print(scores)

#Excercise

#Where was your favorite place for vacation

fav=np.array(["aus","sydny"])

print(fav[0])








