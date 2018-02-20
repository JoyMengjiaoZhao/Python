from PIL import Image,ImageFilter
import os

#image1.show()
#image1.save('Photo.png')
size_300=(300,300)
for f in os.listdir('.'):  #
    if f.endswith('.jpg'): #the extension is '.jpg'
        i=Image.open(f)
        fn,fext=os.path.splitext(f) #split the filename into single name and extension
        i.thumbnail(size_300) #set the size for 300*300
        i.save('300/{}_300.{}'.format(fn,fext))
#Rotate 90
image1=Image.open('Photo.jpg')
image1.rotate(90).save('rotata_photo.jpg')

#color black and white
image1=Image.open('Photo.jpg')
image1.convert(mode='L').save('color_photo.jpg')

#photo blur
image1=Image.open('Photo.jpg')
image1.filter(ImageFilter.GaussianBlur(15)).save('blur_photo.jpg') #default number is 2


