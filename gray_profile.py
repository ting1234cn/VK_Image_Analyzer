import argparse
import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


import tkinter.filedialog

img_data=[]

def on_press(event):
    #print("my position:" ,event.button,event.xdata, event.ydata)
    global img_data
    line=img_data[int(event.ydata),:]
    y_line = img_data[:,int(event.xdata)]
    plt.figure("profile")
    plt.clf()
    plt.subplot(121,title="horizon"+str(int(event.ydata)))
    l1,=plt.plot(line)
    plt.subplot(122,title="vertical"+str(int(event.xdata)))
    l2,=plt.plot(y_line)
    #plt.legend(handles=[l1, l2], labels=['horizon','vertical'],loc='best')
    plt.pause(0.1)#这一步是必须的，图片在pause中更新
    plt.show()

def on_close(event):
    plt.close("all")
def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, help='image file to be profile')
    return parser.parse_args(argv)

def gray_profile():
    image = tkinter.filedialog.askopenfilename(title='选择一个文件',
                                            filetypes=[('image file', '.bmp .jpg .png'),
                                                           ('所有文件', '.*')])
    if len(image)<1:
        return
    img = Image.open(image)
    fig = plt.figure()
    img=img.convert("L")
    global img_data
    img_data = np.array(img)
    plt.imshow(img,plt.cm.gray)
    fig.canvas.mpl_connect('button_press_event', on_press)
    fig.canvas.mpl_connect('close_event', on_close)
    plt.show()

def main(args):

    # try:
    #     messageBox = MainFrame()
    # except Exception:
    #     traceback.print_exc()

    if args.image==None:
        args.image = tkinter.filedialog.askopenfilename(title='选择一个文件', filetypes=[('bmp','.bmp'),('jpg','.jpg'),('png','.png')])
        if len(args.image)<1:
            return
    img = Image.open(args.image)
    fig = plt.figure()
    img=img.convert("L")
    global img_data
    img_data = np.array(img)
    plt.imshow(img,plt.cm.gray)
    fig.canvas.mpl_connect('button_press_event', on_press)
    fig.canvas.mpl_connect('close_event', on_close)
    plt.show()

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))