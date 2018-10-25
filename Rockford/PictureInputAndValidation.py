
# coding: utf-8

# In[5]:


from tkinter import messagebox, filedialog, Button, Tk
import imghdr

root = Tk()
root.withdraw()
file = filedialog.askopenfile(parent=root, mode='rb', title='Choose a file')

if imghdr.what(file) == 'png' or imghdr.what(file) == 'jpeg':
    data = file.read()
    file.close()
    print("File chosen matches requirement: .png or .jpeg")
    print("I got %d bytes from this file." % len(data))
    #print(data)
else:
    print("File chosen does not match requirement: .png or .jpeg")
root.destroy()

top = Tk()

def closeWindow():
    top.destroy()

B = Button(top, text ="Done", command = closeWindow)

B.pack()
top.mainloop()


# In[7]:


#This converts Notebook file into generic python file
#get_ipython().system('jupyter nbconvert --to script PictureInputAndValidation.ipynb')

