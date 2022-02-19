import pyshorteners
from tkinter import *
from tkinter.filedialog import *
from threading import *
ProductLink = ''


def startDownloadThread():
    print(urlField.get())
    
    ProductLink = urlField.get()

if '?' in ProductLink:
    index = ProductLink.find('?')
    ProductLink = ProductLink[0: index]


print('\n\n\nThe Main Product Link Is : ', ProductLink)

Link = ProductLink + \
    '?tracking=APvA30dTUiUIbOl0hhFQOnWOXP0R1o4dp6iTLjXbneYGDB5fzzTxREhinCfDIDVV'
print('\n\n\nThe Affiliate Link Is : ', Link)

shortener = pyshorteners.Shortener()
ShotLink = shortener.tinyurl.short(Link)

print('\n\n\nThe Short Link Is : ', ShotLink)








# strat GUI
main=Tk()
main.geometry('500x400')
main.title('Affiliate With LinkShortener')

urlField3 = Label(main,text=('Enter Product Url Below'), font=('verdana',10))
urlField3.pack(side=TOP,fill=X,pady=10)

urlField = Entry(main,bg='aqua',justify = RIGHT,font=('verdana',20))
urlField.pack(side=TOP,fill=X,padx=40,pady= 5 )

dBtn = Button(main,text = 'Start Downloard',font=('verdana',15),relief='ridge',bg='pink', command = startDownloadThread)# 
dBtn.pack(side=TOP,fill=X,padx=150,pady=15)

urlField4 = Label(main,text=('The Short Link Is'),font=('verdana',10))
urlField4.pack(side=TOP,fill=X,pady=10)

urlField2 = Label(main,text= ShotLink,bg='darkgoldenrod',font=('verdana',20))
urlField2.pack(side=TOP,fill=X,padx=40)




'''urlField5 = Label(main,text=('Video Size'),font=('verdana',10))
urlField5.pack(side=TOP,fill=X,pady=20)

urlField6 = Label(main,text='',bg='Brown',font=('verdana',20))
urlField6.pack(side=TOP,fill=X,padx=40)
'''
main.mainloop()

