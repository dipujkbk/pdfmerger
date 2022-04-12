from tkinter import *
from tkinter import filedialog,messagebox
import PyPDF2
import os

from PyPDF2.pdf import PdfFileReader

root = Tk()
root.title("Pdf Merger")
root.geometry('400x400')

mylabel = Label(root,text="Select pdf files to merge",borderwidth=2, relief="sunken",padx=10,pady=10)
mylabel.grid(row=0,column=0,sticky=EW,padx=10,pady=10,columnspan=2)


input_filenames =[]
myformats = [("Pdf filess","*.pdf"),("jpg files","*.png")]
def merge_pdfs():
    merger_obj = PyPDF2.PdfFileMerger()
    print(input_filenames)
    for pdf in input_filenames:
        merger_obj.append(PyPDF2.PdfFileReader(pdf,'rb'))

    output_path = filedialog.asksaveasfilename(title="Save pdf in",filetypes=myformats)
    if output_path:
        merger_obj.write(output_path +".pdf")
        messagebox.showinfo("File Saved!",f"Your Merged File saved in {os.path.split(output_path)[0]}")



def open():
    global input_filenames,btn1
    input_filenames = filedialog.askopenfilenames(title="select pdf files",filetypes=myformats)
    clean_name =[]
    for item in input_filenames:
        clean_name.append(os.path.split(item)[1])

    # mylabel = Label(root,text=clean_name)
    mylabel.grid(row=2,column=0)

    btn1 = Button(root,text="Merge Pdfs",command=merge_pdfs,bd=4,bg='yellow',fg='blue')
    btn1.grid(row=1,column=1,padx=10,pady=10,sticky=EW,ipadx=20)

   



  

btn = Button(root,text='Select Files',command=open,bd=4,bg='yellow',fg='blue')
btn.grid(row=1,column=0,padx=10,pady=10,sticky=EW)

btn1 = Button(root,text="Merge Pdfs",state=DISABLED,bd=4,bg='yellow',fg='blue')
btn1.grid(row=1,column=1,padx=10,pady=10,sticky=EW,ipadx=20)  
    
root.mainloop()