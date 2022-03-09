from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class Linkshoter:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Link Management System")

        upper_frem = Frame(self.root, width=1500, height=100, bd=20, relief=RIDGE)
        upper_frem.place(x=0, y=0, width=1500, height=100)
        upper_frem_lavel = Label(upper_frem, text="LINK  MANAGEMENT  SYSTEM", font=("times new roman",50, "bold"),fg="red")
        upper_frem_lavel.place(x=100, y=0, width=1300, height=60)

        main_frem = Frame(self.root, width=1495, height=410, bd=15, relief=RIDGE)
        main_frem.place(x=1, y=105, width=1500, height=410)


        main_left_frame = LabelFrame(main_frem, width=800, height=350, bd=7, relief=RIDGE,text="Input box",font=("arial",11,"bold"))
        main_left_frame.place(x=10, y=10, width=800, height=350)

        product_name = Label(main_left_frame, text="Product Name:", font=("arial", 16, "bold"), padx=10, pady=6)
        product_name.grid(row=1, column=0, sticky=W)
        product_name = ttk.Entry(main_left_frame, font=("arial",16, "bold"), width=35)
        product_name.grid(row=1, column=1)

        product_link_label = Label(main_left_frame, text="Product Link :", font=("arial", 16, "bold"), padx=10, pady=6)
        product_link_label.grid(row=2, column=0, sticky=W)
        product_link_entry = ttk.Entry(main_left_frame, font=("arial", 16, "bold"), width=35)
        product_link_entry.grid(row=2, column=1)

        custom_link_lavel = Label(main_left_frame, text="Custom Link:", font=("arial", 16, "bold"), padx=10, pady=6)
        custom_link_lavel.grid(row=3, column=0, sticky=W)
        custom_link_entry = ttk.Entry(main_left_frame, font=("arial", 16, "bold"), width=35)
        custom_link_entry.grid(row=3, column=1)

        btn_farme = Frame(main_left_frame, width=320, height=50, bd=10, relief=RIDGE)
        btn_farme.place(x=200, y=260, width=320, height=50)

        customize_link_btn = Button(btn_farme, text="Genaret Shot Link  ", font=("times new roman", 11, "bold"), width=200, bg="green", fg="white")
        customize_link_btn.place(x=0, y=0, width=300)







        main_right_frem = LabelFrame(main_frem, width=600, height=350, bd=7, relief=RIDGE, text="Customize link",font=("arial", 11, "bold"))
        main_right_frem.place(x=850, y=10, width=600, height=350)

        main_left_text=Text(main_right_frem,font=("arial",12,"bold"), width=62, height=16)
        main_left_text.place(x=10,y=10)

        right_btn_farme = Frame(main_right_frem, width=800, height=50, bd=15, relief=RIDGE)
        right_btn_farme.place(x=0, y=280, width=580, height=50)

        copy_link_btn = Button(right_btn_farme, text="Copy", font=("times new roman", 11, "bold"),width=200, bg="green", fg="white")
        copy_link_btn.place(x=0, y=0, width=550)










if __name__=="__main__":
    root=Tk()
    app=Linkshoter(root)
    root.mainloop()