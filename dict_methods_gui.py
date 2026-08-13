import tkinter as tk
from dict_methods import add_item, sort_entries
#Tkinter GUI Below:
window = tk.Tk()

window.title("Mecha Munch Shopping Cart")
window.geometry("500x600")

cart = {}

#Functions
def add_item_to_cart():
    iteminput = item_entry.get()

    add_item(cart, [iteminput])

    cart_list.delete(0, tk.END)

    for item, quantity in cart.items():
        cart_list.insert(
            tk.END,
            f"{item}: {quantity}"
        )
        
def sort_cart():
    sorted_cart = sort_entries(cart)

    cart_list.delete(0, tk.END)

    for item, quantity in sorted_cart.items():
        cart_list.insert(
            tk.END,
            f"{item}: {quantity}"
        )
        
def combined_button():
    add_item_to_cart()
    sort_cart()
#---
        
        
# GUI Elements
# Title Label
title_label = tk.Label(
    window,
    text="Mecha Munch Shopping Cart",
    font=("Arial", 20)
)
title_label.pack(pady=20)

# Input Fields
item_label = tk.Label(
    window,
    text="Item Name:",
    font=("Arial", 14)
)
item_label.pack()
item_entry = tk.Entry(window)
item_entry.pack()

#Add Items
add_button = tk.Button(
    window,
    text="Add Item",
    command=combined_button
)

add_button.pack(pady=10)
#---



#Cart Listbox
cart_list = tk.Listbox(window)
cart_list.pack(pady=20)
#---



window.mainloop()
