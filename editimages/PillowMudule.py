# installation of pillow library 
# change the image extension 
# resize image files
# resize multiple images using for loop  
# Sharpness 
# Brightess 
# Color
# Contrast 
# Image blur , GaussianBlur
from PIL import Image,ImageEnhance,ImageFilter
import os
obj=Image.open('imagee.jpg')
#obj.show() #toChangeExtenstion 
#obj.save('kp.pdf')
# MAX_SIZE=(250,250)
# obj.thumbnail(MAX_SIZE)
# obj.save('resize.png')
# for item in os.listdir():
#     if item.endswith('.png'):
#         obj=Image.open(item)
#         filename,extenstion=os.path.splitext(item)
#         obj.save(f'{filename}.jpg')
#-------sharpness---------------
# inhencer=ImageEnhance.Sharpness(obj)
# inhencer.enhance(2).save('enhenced.png')

#-------color--------------
# inhencer=ImageEnhance.Color(obj)
# inhencer.enhance(2).save('enhenced.png')

#-----------brightness------------

# inhencer=ImageEnhance.Brightness(obj)
# inhencer.enhance(1).save('enhenced.png')

#-----------contrass------------

# inhencer=ImageEnhance.Contrast(obj)
# inhencer.enhance(1).save('enhenced.png')

#----------------->blur<-----------

obj.filter(ImageFilter.GaussianBlur()).save('enhenced.png')