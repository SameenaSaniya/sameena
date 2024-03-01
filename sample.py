import webbrowser as web
print("1.youtube")
print("2.google")
print("3.chrome")
print("4.firefox")     
a=int(input("select one webbrowser")) 
def e():
    web.open("www.youtube.com")
def b():
    web.open("www.google.com")
def c():          
    web.open("www.chrome.com")
def d():
    web.open("www.firefox.com")   
a=int(input("enter your choice"))
if(a==1):
    e()
elif(a==2):
    b()
elif(a==3):
    c()
elif(a==4):
    d()
else:
    print("Invalid choice")     
       