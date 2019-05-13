import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import tkinter.filedialog
import tkinter.messagebox



def substract_img():
    image = tkinter.filedialog.askopenfilenames(title='选择两个文件',
                                            filetypes=[('image file', '.bmp .jpg .png'),
                                                           ('所有文件', '.*')])
    if len(image)!=2:
        tkinter.messagebox.showerror("incorrect file number","incorrect file number")
        return
    img1 = Image.open(image[0])
    img2= Image.open(image[1])
    if img1.size!=img2.size:
        tkinter.messagebox.showerror("image size different", "image size is different")
        return
    fig = plt.figure()
   # img=img.convert("L")
   # plt.subplot(221, title=image[0].rpartition("/")[2])
    plt.subplot(221, title="image1")
    plt.imshow(img1, plt.cm.gray)
    plt.subplot(222, title="image2")
    plt.imshow(img2, plt.cm.gray)
    plt.subplot(223, title="substract result")

    result_img = np.clip(np.array(img1)-np.array(img2),0,255)
    plt.imshow(result_img,plt.cm.gray)
    plt.tight_layout()

    plt.show()

def average_img():
    image = tkinter.filedialog.askopenfilenames(title='选择多个文件',
                                                filetypes=[('image file', '.bmp .jpg .png'),
                                                           ('所有文件', '.*')])
    if len(image)<1:
        return
    elif len(image) <2:
        tkinter.messagebox.showerror("incorrect file number", " file number must be more than 2")
        return
    img=[]
    j=0
    fig = plt.figure()
    for i in image:
        img.append(np.array(Image.open(i)))
        if j>0:
            if img[j].size != img[0].size:
                tkinter.messagebox.showerror("image size different", "image size is different,please choose same size image")
                return
        plt.subplot(2,len(image),j+1)
        plt.imshow(img[j], plt.cm.gray)
        j+=1




    plt.subplot(223, title="average result")
    result_img = np.average(img,0)
    plt.imshow(result_img, plt.cm.gray)

    plt.show()