# Sure! Here's the code breakdown with comments and explanations:

# ```python
print("Welcome to our online shoe shop")

def brands():
    print("Available brands are: ")
    brand = ['nike','adidas','sparks']
    print(brand)

def sizes():
    print("Available sizes are: ")
    size = [8,9,10]
    print(size)

def prices():
    print("Shoes are available between price range 999 to 5000")

def colors():
    print("Available colors are: ")
    color = ["Red","Black","White"]
    print(color)

database = [(2000,'Nike','Black',9),(3000,'Adidas','Red',10)]

def check(mn,mx,brnd,clr,sz):
    for tup in database:
        if (tup[0] >= mn and tup[0] <= mx) and tup[1] == brnd and tup[2] == clr and tup[3] == sz:
            return True
    return False

while True:
    print("Enter 1 to see brands: ")
    print("Enter 2 to see sizes available: ")
    print("Enter 3 to see price range: ")
    print("Enter 4 to see colors available: ")
    
    print("Enter 5 to check for a particular shoe: ")
    print("Enter 6 to exit: ")
    inputt = int(input())
    if inputt == 1:
        print(brands())
    if inputt == 2:
        print(sizes())
    if inputt == 3:
        print(prices())
    if inputt == 4:
        print(colors())

    if inputt == 5:
        print(("Enter price range(min and max price): "))
        mn,mx = map(int,input().split())
        brnd = input("Enter brand you are looking for: ")
        clr = input("Enter color: ")
        sz = int(input("Enter size: "))
        if check(mn,mx,brnd,clr,sz):
            print("Required shoe is available at the store")
        else:
            print('Required shoe is not available')
'''
The code represents a simplified version of an online shoe shop. Here's an explanation of each section:

1. The initial print statement welcomes the user to the online shoe shop.

2. `brands()` function prints the available brands, which are Nike, Adidas, and Sparks.

3. `sizes()` function prints the available sizes, which are 8, 9, and 10.

4. `prices()` function informs the user that shoes are available in the price range of 999 to 5000. However, this function does not print any values explicitly.

5. `colors()` function prints the available colors, which are Red, Black, and White.

6. `database` is a list of tuples representing the shoe inventory in the shop. Each tuple contains the price, brand, color, and size of a shoe.

7. `check()` function takes minimum price (`mn`), maximum price (`mx`), brand (`brnd`), color (`clr`), and size (`sz`) as input. It iterates through the `database` and checks if there is a shoe that matches the given criteria. If a matching shoe is found, it returns `True`; otherwise, it returns `False`.

8. The `while` loop allows the user to interact with the program until they choose to exit.

9. The user is presented with a menu of options, and their input is stored in the variable `inputt` as an integer.

10. Depending on the user's input, different functions are called to display the available brands, sizes,
'''



'''
from tkinter import *
import pyttsx3
import keyboard

root = Tk() 
root.title("Chatbot")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160 )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def send():
    send = "\nYou-> "+e.get()
    txt.insert(END, send)
    user = e.get().lower()
    if(user== "hello"):
        speak("Hi")
        txt.insert(END, "\n" + "Bot -> Hi")
    elif(user == "hi" or user == "hii" or user == "hii"):
        speak("Hello")
        txt.insert(END, "\n" + "Bot -> Hello")
    elif(e.get()== "how are you"):
        speak("fine! and you")
        txt.insert(END, "\n" + "Bot-> fine! and you")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        speak("Great! how can I help you?")
        txt.insert(END, "\n" +"Bot-> Great! how can I help you?")
    else:
        speak("Sorry! I dind't got you")
        txt.insert(END, "\n"+ "Bot-> Sorry! I dind't got you")
    e.delete(0, END)

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e= Entry(root, width=100)
e.grid(row=1, column=0) 
send = Button(root, text="Send", command=send)
send.grid(row=1, column=1)
root.bind('<Return>', lambda e: send(e))
root.mainloop()
#first give --> !pip install tkinter if error occured in tkinter
# another step -->  !pip install pyttsx3
# last install --> !pip install keyboard
'''

'''
#ChatBot for Order delivery app
def greet():
    print("~ Hello, this is Helper Bot at your Service.")
    print("~ I was invented in 2023 by Rakhi Patil.")
    
def intro():
    print("~ Please type 'Y' to start the conversation.")
    name = input()
    print("~ Can you please remind me your name?".format(name))
    name = input()
    print("~ {0}, Please wait, You'll be assigned a Helper bot assistant shortly.".format(name))
     
def order_id():
    print("~ What is Your Order_id?.")
    name = input()
    print("~ Your Order id is {0}, let me check your order and I'll get back to you asap.".format(name))
    name = input()
    print("~ Your order details are ab...z".format(name))
    
def confirm():
    print("~ Please Type 'K' for confirming your order details, so we can proceed with your problem.")
    name = input()
    print("~ Thank you for the confirmation.".format(name))
    
def problem():
    print("~ Can I get the details of the Problem you are facing?")
    name = input()
    print("~ Sorry for {0} problem, let me check the details and I will get back to you asap.".format(name))
    name = input()
        
def solution():
    print("~ Your Order has been arrived at the nearest Helper Bot delivery center.")
    name = input()
    print("~ Your order will be delivered to you within Tommorrow.".format(name))
    name = input()
    
def end():
     print("~ Is your problem solved?.")
     name = input()
     print("~ We have marked your issue as resolved. You can contact us again in case you have any queries.".format(name))   
     print("~ Thank you for connecting with us, Have a nice Day!".format(name))
     name = input()   
     print("This chat ended here, you cannot reply to this conversation anymore.".format(name))
    
greet()
intro()
order_id()
confirm()
problem()
solution()
end()
'''