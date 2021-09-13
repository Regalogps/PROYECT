from tkinter import *

root = Tk()
root.title('Codemy.com - Auto Select/Search')
root.geometry("500x300")


def update(data):     # LISTBOX
	# Clear the listbox
	my_list.delete(0, END)

	# Add toppings to listbox
	for item in data:
		my_list.insert(END, item)


def fillout(e):      # LISTBOX ENTRY
	
	my_entry.delete(0, END)

	# Add clicked list item to entry box
	my_entry.insert(0, my_list.get(ANCHOR))
 
def check(e):        # LISTBOX

	typed = my_entry.get()

	if typed == '':
		data = toppings
	else:
		data = []
		for item in toppings:
			if typed.lower() in item.lower():
				data.append(item)
	update(data)				


my_label = Label(root, text="Start Typing...",
	font=("Helvetica", 14), fg="grey")
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

my_list = Listbox(root, width=50)
my_list.pack(pady=40)

toppings = ["Pepperoni", "Peppers", "Mushrooms", "Cheese", "Onions", "Ham", "Taco"]

# Add the toppings to our list
update(toppings)

my_list.bind("<<ListboxSelect>>", fillout)
my_entry.bind("<KeyRelease>", check)

root.mainloop()