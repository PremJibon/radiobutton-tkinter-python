from tkinter import *

root = Tk()

def order():
    if(x.get()==0):print("you order pizza")
    

food = ["pizza","burger","hotdog"]

pizzaImage= PhotoImage(file='pizza.png')
hotdogImage= PhotoImage(file='hotdog.png')
burgerImage= PhotoImage(file='burger.png')

pizzaImage = pizzaImage.subsample(2, 2)  # You can adjust the numbers to change the size
hotdogImage = hotdogImage.subsample(2, 2)
burgerImage = burgerImage.subsample(2, 2)

x = IntVar()

foodImages = [pizzaImage,burgerImage,hotdogImage]
for i in range(len(food)):
    radiobutton = Radiobutton(root,text=food[i],
                              variable=x,
                              value=i,padx_=25,
                              font=("Impact",50),
                              image=foodImages[i],
                              compound='left',
                              indicatoron=0,
                              width =375,command=order)
    
    radiobutton.pack(anchor=W)
root.mainloop()