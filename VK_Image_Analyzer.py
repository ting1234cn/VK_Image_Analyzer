import tkinter as tk
import traceback
import gray_profile
import Image_substract

class MainFrame:
    def __init__(self):
        # 目录相关
        self.root = tk.Tk()
        self.root.title("VK_Image_Analyzer")
        self.showMsgBox()
        self.root.mainloop()

    # 显示消息框
    def showMsgBox(self):
        root = self.root
        tk.Button(root, text='图像灰度profile', command=gray_profile.gray_profile,activebackground="BLUE",bd=10).grid(row=1, column=1,sticky="W")
        tk.Button(root, text='图像相加平均', command=Image_substract.average_img,activebackground="BLUE",bd=10).grid(row=1, column=2,sticky="W")
        tk.Button(root, text='图像相减', command=Image_substract.substract_img,activebackground="BLUE",bd=10).grid(row=1, column=3,sticky="W")
        tk.Button(root, text='图像gamma 变换', command=gray_profile.gray_profile,state="disabled",bd=10).grid(row=2, column=1,sticky="W")







if __name__  == "__main__":
    try:
        messageBox = MainFrame()
    except Exception:
        traceback.print_exc()