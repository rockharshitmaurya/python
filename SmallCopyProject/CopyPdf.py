import os,shutil
for path,k,files in os.walk(os.getcwd()):
   for filename in files:
    if filename.endswith('.pdf'):
        #os.mkdir('pdffiles')
        if(os.path.exists('pdffiles')):
	        print('Already exists')
        else:
	        os.mkdir('pdffiles')
        item_new_path=os.path.join(os.getcwd(),'pdffiles')
        shutil.move(os.path.join(path,filename),item_new_path)