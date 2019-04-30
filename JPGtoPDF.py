from PIL import Image
import os

def convert_JPEG_to_PDF(filename):
    im1 = Image.open(os.path.join(filename))
    im1.save(f.split('.')[0]+'.pdf', "PDF" ,resolution=100.0, save_all=True, append_images=[])

if __name__ == '__main__':
    filename=''
    convert_JPEG_to_PDF(filename)
