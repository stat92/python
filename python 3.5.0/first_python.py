# Nesting loops
res = [(x,y,z) 	for x in range(5) 
					if x%2==0 
						for y in range(5) 
							if y%2!=0 
								for z in range(5) if z%2==0 ]
print (res)


# Generates list and dictionary from list
L1 = [1,2,3,4,5,6,7,8]
L2 = [5,6,7,8,9,10,11,12]

list_from_gnrtr = [ x for x in L1 if x%2==0 ]
dict_from_gnrtr = { x: y for (x,y) in zip(L1,L2)if x%2!=0 }

print(list_from_gnrtr)
print(dict_from_gnrtr)


# List from the text
s = list(map((lambda line: line.rstrip()), open(r'files\numpy_io.txt','r')))
print(s)


# Nesting function
def out(s):
	state = s
	def inner(n):
		nonlocal state
		print(state,n)
		state += 1
	return inner

f = out(1)

f(2)
f(3)
f(4)


		# PICKLE
import pickle

Dict = {'a': 1, 'b': 45, 'c': 878, 52: 'FT'}

P = open(r'files\pickled.pkl','wb')
pickle.dump(Dict,P)
P.close()

P = open(r'files\pickled.pkl','rb')
R = pickle.load(P)
print(R)
		# PICKLE