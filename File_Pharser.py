import tkinter as tk
from tkinter import filedialog
from file_pharser_main import *
class file_hider_main:
	def __init__(self):
		self.EXTENSION=["py","c","cpp","mp4","mp3","exe","txt","docx","zip","xml","html"]
		self.root=tk.Tk()
		l=tk.Label(self.root,text="Welcome to File Parser",font="none 15 bold ")
		l.grid(row=0,column=0)
		b=tk.Button(text="Parse",command=self.hide)
		b.grid(row=1,column=0)
		b2=tk.Button(text="Unparse",command=self.unhide)
		b2.grid(row=1,column=1)



		self.root.mainloop()
	def hide(self):
		self.hide_frame=tk.Frame(self.root)
		self.hide_frame.grid(row=2,column=1)
		b=tk.Button(self.hide_frame,text="Select the file",command=self.hide_select)
		b.grid(row=0,column=0)



	def hide_select(self):
		self.file_path=filedialog.askopenfilename(initialdir="/",title="Select the file You want to hide")
		if len(self.file_path)>=1:
			print(self.file_path)
			l=tk.Label(self.hide_frame,text=self.file_path,bg="#ff0000")
			l.grid(row=0,column=1)
			l=tk.Label(self.hide_frame,text="Eneter the filename with any extention")
			l.grid(row=0,column=2)
			self.e=tk.Entry(self.hide_frame)
			self.e.grid(row=0,column=3)
			b=tk.Button(self.hide_frame,text="continue",command=self.hide_check)
			b.grid(row=0,column=4)
	def hide_check(self):
		self.hidden_file_name=self.e.get()
		print(self.hidden_file_name)
		exetension=self.hidden_file_name.split(".")
		exetension=exetension[-1]
		if "."in self.hidden_file_name and not exetension in self.EXTENSION:
			dump(self.file_path,self.hidden_file_name)
			pass
		else:
			self.e.insert(0,"Extension s node there")


	def unhide(self):
		self.hide_frame=tk.Frame(self.root)
		self.hide_frame.grid(row=2,column=1)
		b=tk.Button(self.hide_frame,text="Select the file",command=self.unhide_select)
		b.grid(row=0,column=0)
	def unhide_select(self):
		self.file_path=filedialog.askopenfilename(initialdir="/",title="Select the file You want to hide")
		if len(self.file_path)>=1:
			print(self.file_path)
			l=tk.Label(self.hide_frame,text=self.file_path,bg="#ff0000")
			l.grid(row=0,column=1)
			l=tk.Label(self.hide_frame,text="Eneter the filename with any extention")
			l.grid(row=0,column=2)
			self.e=tk.Entry(self.hide_frame)
			self.e.grid(row=0,column=3)
			b=tk.Button(self.hide_frame,text="continue",command=self.unhide_check)
			b.grid(row=0,column=4)
	def unhide_check(self):
		self.hidden_file_name=self.e.get()
		print(self.hidden_file_name)
		exetension=self.hidden_file_name.split(".")
		exetension=exetension[-1]
		if "."in self.hidden_file_name and  exetension in self.EXTENSION:
			load(self.file_path,self.hidden_file_name)
		else:
			self.e.insert(0,"Extension s node there")



file_hider_main()