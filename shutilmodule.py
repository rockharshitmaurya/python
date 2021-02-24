import os
import shutil
print(os.getcwd())
#os.mkdir("new")
#os.makedirs("new3/new4/new4")
#shutil.rmtree('new3')
print([dirs for paths ,dirs,files in os.walk('new3')])
#shutil.copy('first.py','new/first.py')
#shutil.copytree('new3','new/new')
#shutil.move('new','new2/new1')