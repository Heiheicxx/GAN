from PIL import Image
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def convert(dir,width,height):
    file_list = os.listdir(dir)
    print(file_list)
    for filename in file_list:
        path=''
        path=dir+filename
        im=Image.open(path)
        out=im.resize((256,256),Image.ANTIALIAS)
        print ("%s has been resized!"%filename)
        out.save(path)
        print("success")

if __name__ == '__main__':
   convert("/home/cxx/deep/GAN/pytorch-CycleGAN-and-pix2pix/datasets/num/testA/",256,256)