from tkinter import*
import pyshorteners

root = Tk()
root.geometry('500x400')
root.title('Affiliate With LinkShortener')


def ClickMe():
    ProductLink = entry1.get()
    # print(ProductLink)

    if '?' in ProductLink:
        index = ProductLink.find('?')
        ProductLink = ProductLink[0: index]


    Link = ProductLink + \
    '?tracking=APvA30dTUiUIbOl0hhFQOnWOXP0R1o4dp6iTLjXbneYGDB5fzzTxREhinCfDIDVV'


    shortener = pyshorteners.Shortener()
    ShotLink = shortener.tinyurl.short(Link)



    OutpuLink = Label(root, text=ShotLink, font=('verdana', 10))
    OutpuLink.pack()


name = Label(root, text='Enter Product Url Below', font=('verdana', 10))
entry1 = Entry(root)
button = Button(root, text='Click Me', command=ClickMe)


name.pack()
entry1.pack()
button.pack()

root.mainloop()
