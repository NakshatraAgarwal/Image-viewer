from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Image Viewer")
root.geometry("500x500")

l_img = Label(root, bg = "black", highlightthickness = 5, borderwidth = 1, relief = SOLID)
l_img.place(relx = 0.5, rely = 0.5, anchor = CENTER)

img_path = ""

def open_file():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Image File", filetypes = [("Image Files", "*.jpg;*.gif;*.png;*.jpeg;")])
    img = Image.open(img_path)
    img1 = ImageTk.PhotoImage(img)
    l_img["image"] = img1
    img1.close()
    
    
    
    
def rotate_img():
    global img_path
    img = Image.open(img_path)
    rotated_img = img.rotate(180)
    igm = ImageTk.PhotoImage(rotated_img)
    l_img["image"] = igm
    igm.close()
    
    
b_open = Button(root, text = "Open Image", font = ("calibri", 18, "bold"), relief = SOLID, padx = 10, pady = 10, command = open_file)
b_open.place(relx = 0.5, rely = 0.2, anchor = CENTER)

b_rotate = Button(root, text = "Rotate Image", font = ("calibri", 18, "bold"), relief = SOLID, padx = 10, pady = 10, command = rotate_img)
b_rotate.place(relx = 0.5, rely= 0.8, anchor = CENTER)




root.mainloop()

