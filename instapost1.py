from tkinter import *
import PIL.Image
from PIL import Image
from PIL import ImageFont, ImageDraw
from tkinter import ttk
# import requests
# import shutil # save img locally
root=Tk()
root.config(bg="purple")
root.geometry('600x300')
root.title("instagram post maker")

my_font="TIMESR.ttf"
font_size=50

def download():   
    # url= word_entry.get()
    # r = requests.get(url, stream=True)
    # if r.status_code == 200:
    #     with open("tara.jpg", 'wb') as f:
    #         r.raw.decode_content = True
    #         shutil.copyfileobj(r.raw, f)
    resize_photo()
    create_photo()

   


def Cancle():
     print("your welcome")
     exit()

                                 
def resize_photo(): #make instagram post size
    im = Image.open(r"tara.jpg")
    width, height = im.size
    if width != 1080:
        width =1080
    
    if height !=1080:
        height = 1080
        
    newsize = (width, height)
    im1 = im.resize(newsize)  
    im1.save("tara_instagram_siza.jpg")        


def fun1():
    global my_font
    option = comboExample.get()
    if option == "Times":
        my_font = "TIMESR.ttf"
    elif option == "Chilanka":
        my_font ="Chilanka-Regular.ttf"
    elif option == "sunbeam":
        my_font="Sunbeam.ttf" 
    elif option == "aAlleyGarden":
        my_font="aAlleyGarden.ttf"
    elif option == "dahot2.Filxgirl":
        my_font="dahot2.Filxgirl.ttf"
   
def fun2():
    global font_size
    font_size=font.get()

def place(): #place to write the text in photo
    place_name = text_place.get()
    if place_name == "Top Middle":
        weight , height =200,15
    elif place_name == "Top right":
        weight , height =500,15
    elif place_name == "Top left":
        weight , height =15,15
    elif place_name == "Center Middle":
        weight , height =200,400
    elif place_name == "Center right":
        weight , height =500,400
    elif place_name == "Center left":
        weight , height =15,400
    elif place_name == "Bottom middle":
        weight , height =200,950
    elif place_name == "Bottom right":
        weight , height =500,950
    elif place_name == "Bottom left":
        weight , height =15,950
        
    return weight , height
        
        


def create_photo():
    global my_font,font_size
    my_image = PIL.Image.open("tara_instagram_siza.jpg")
    title_font = ImageFont.truetype(my_font, int(font_size))
    title_text = "The Beauty of Nature"
    image_editable = ImageDraw.Draw(my_image)
    weight,height = place()
    image_editable.text((weight,height), title_text, (237, 230, 211), font=title_font, bg="red")
    my_image.save("result.jpg")

comboExample = ttk.Combobox(root,values=["Chilanka-Regular","aAlleyGarden","dahot2.Filxgirl","Sunbeam","Times" ],font=("courier",13))
comboExample.grid(row=1,column=1,sticky="NSWE")
font = ttk.Combobox(root,values=[100,90,80,70,60,50,40,30,20,10])
font.grid(row=2,column=1,sticky="NSWE")
text_place = ttk.Combobox(root,values=["Top Middle","Top right","Top left","Center Middle","Center right","Center left","Bottom middle","Bottom right","Bottom left" ],font=("courier",13))
text_place.grid(row=3,column=1,sticky="NSWE")




download_text=Label(root,text="Please enter your link!",fg="black",font=("courier",13))
download_text.grid(row=0,column=0,sticky="NSWE")
word_entry=Entry(root,bg="white",fg="black",font=("courier",13))
word_entry.grid(row=0,column=1,sticky="NSWE")


labelTop = Label(root, text = "Choose your favourite font!",fg="black",font=("courier",13))
labelTop.grid( row=1,column=0,sticky="NSWE")
sizetop = Label(root, text = "Choose your favourite size!",fg="black",font=("courier",13))
sizetop.grid( row=2,column=0,sticky="NSWE")
placetop= Label(root, text = "Choose your favourite place!",fg="black",font=("courier",13))
placetop.grid( row=3,column=0,sticky="NSWE")



btn_convert = Button(root, text = "convert", command=lambda: [fun1(), fun2(), download()])
btn_convert.grid(row=4,column=0,sticky="NSWE")
cancle_btn = Button(root,text="cancle" , command= Cancle)
cancle_btn.grid(column=1, row=4,sticky="NSWE")
root.mainloop()