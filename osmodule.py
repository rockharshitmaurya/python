import os
print(os.getcwd())
print(os.chdir(r'C:\Users\LENOVO\Documents'))
if(os.path.exists('new')):
	print('Already exists')
else:
	os.mkdir('new')
open('new.txt','a').close()
print(os.listdir())
print([os.path.join(os.getcwd(),item) for item in os.listdir()])