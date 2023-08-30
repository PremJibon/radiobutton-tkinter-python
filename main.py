from tkinter import *

food = ["pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("You order pizza")
    elif (x.get()==1):
        print("You order burger")
    else:
        print("you order hotdog")
      
window = Tk()

pizzaImage = PhotoImage(file='pizza.png')
hotdogImage = PhotoImage(file='hotdog.png')
burgerImage = PhotoImage(file='burger.png')

# Reduce the size of the images by using the subsample method
pizzaImage = pizzaImage.subsample(2, 2)  # You can adjust the numbers to change the size
hotdogImage = hotdogImage.subsample(2, 2)
burgerImage = burgerImage.subsample(2, 2)

foodImages = [pizzaImage,burgerImage,hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,text=food[index],
                              variable=x,
                              value=index,padx_=25,
                              font=("Impact",50),
                              image=foodImages[index],
                              compound='left',
                              
                              width =375,command=order)
    
    radiobutton.pack(anchor=W)

window.mainloop()