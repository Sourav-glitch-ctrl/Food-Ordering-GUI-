import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()

root.title("TTC - Binary Restaurant")

# Initialize order list and total
order_list = []
total_amount = 0

# ------------------------------------FUNCTIONS--------------------------------------------- #
def update_display(image, dish_name, price):
    displayLabel.configure(image=image)
    displayLabel.image = image  # To prevent garbage collection of the image
    displayLabel.dish_name = dish_name  # Store the dish name
    displayLabel.price = price  # Store the price


def add_to_order():
    global total_amount
    if hasattr(displayLabel, 'dish_name'):
        order_list.append((displayLabel.dish_name, displayLabel.price))
        total_amount += displayLabel.price
        update_order_display()
    else:
        print("No dish selected to add.")


def remove_from_order():
    global total_amount
    if order_list:
        last_item = order_list.pop()
        total_amount -= last_item[1]
        update_order_display()
    else:
        print("No items in the order to remove.")


def update_order_display():
    orderTransaction.configure(text="\n".join(f"{name} - ₹{price}" for name, price in order_list))
    orderTotalLabel.configure(text=f"TOTAL: ₹{total_amount}")


def confirm_order():
    global total_amount
    if not order_list:
        messagebox.showinfo("Order Confirmation", "No items in the order.")
        return

    order_details = "\n".join(f"{name} - ₹{price}" for name, price in order_list)
    messagebox.showinfo("Order Confirmation", f"Your order:\n{order_details}\n\nTotal: ₹{total_amount}")

    order_list.clear()
    total_amount = 0
    update_order_display()


# ---------------------------------- STYLING AND IMAGES ------------------------------------ #

#region Style configurations
s = ttk.Style()

# Set the theme to 'clam' to allow more styling options
s.theme_use('clam')

# Main frame background: dark with subtle contrast for a sleek, modern look
s.configure('MainFrame.TFrame', background="#222831")

# Menu frame: slightly lighter with modern gray tones
s.configure('MenuFrame.TFrame', background="#393E46")
s.configure('DishFrame.TFrame', background="#393E46")  # Consistent background for dish frames

# Image display frame: clean, bright background for showcasing food images
s.configure('DisplayFrame.TFrame', background="#EEEEEE")

# Order frame: dark gray with bright accents
s.configure('OrderFrame.TFrame', background="#2E2E2E")

# Labels styling
s.configure('MenuLabel.TLabel',
            background="#393E46",
            font=("Verdana", 12, "bold"),
            foreground="#EEEEEE",
            padding=(10, 10, 10, 10))

s.configure('OrderTitle.TLabel',
            background="#2E2E2E",
            font=("Verdana", 14, "bold"),
            foreground="#FFD369",
            padding=(10, 10, 10, 10))

s.configure('OrderID.TLabel',
            background="#2E2E2E",
            font=("Helvetica", 11, "italic"),
            foreground="#EEEEEE",
            padding=(5, 5, 5, 5))

s.configure('orderTotalLabel.TLabel',
            background="#2E2E2E",
            font=("Helvetica", 12, "bold"),
            foreground="#FFD369",
            padding=(10, 10, 10, 10),
            anchor="w")

s.configure('orderTransaction.TLabel',
            background="#2E2E2E",
            font=('Helvetica', 11),
            foreground="white",
            wraplength=170,
            anchor="nw",
            padding=(5, 5, 5, 5))

# Buttons styling
s.configure('AccentButton.TButton',
            background="#FFD369",
            foreground='#222831',
            font=('Helvetica', 11, 'bold'),
            padding=(5, 5, 5, 5),
            borderwidth=0,
            focuscolor='none')

s.map('AccentButton.TButton',
      background=[('active', '#E0C565'), ('disabled', '#AFAFAF')])


s.map('GreenButton.TButton',
      background=[('active', '#45A049'), ('disabled', '#AFAFAF')])

# Adjust the default TButton style to remove borders and focus ring
s.configure('TButton',
            borderwidth=0,
            focuscolor='none')
# Green button for "Add to Order"
s.configure('GreenButton.TButton',
            background="#45A049",  # Green color
            foreground='#FFFFFF',  # White text
            font=('Helvetica', 11, 'bold'),
            padding=(5, 5, 5, 5),
            borderwidth=0,
            focuscolor='none')

s.map('GreenButton.TButton',
      background=[('active', '#3E8E41'), ('disabled', '#AFAFAF')])  # Darker green on active

# Red button for "Remove"
s.configure('RedButton.TButton',
            background="#D9534F",  # Red color
            foreground='#FFFFFF',  # White text
            font=('Helvetica', 11, 'bold'),
            padding=(5, 5, 5, 5),
            borderwidth=0,
            focuscolor='none')

s.map('RedButton.TButton',
      background=[('active', '#C9302C'), ('disabled', '#AFAFAF')])  # Darker red on active



#endregion

Image.MAX_IMAGE_PIXELS = None

# region Images
# Update these paths to the correct locations of your images
LogoImageObject = Image.open("C:\\Users\\ayush\\Downloads\\1728659797202vxpncnwn.jpg").resize((130, 130))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("C:\\Users\\ayush\\Downloads\\TransistorWOK.png").resize((800, 130))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

# Menu images
displayDefaultImageObject = Image.open("C:\\Users\\ayush\\Downloads\\display - Default.png").resize((350, 360))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

paneerTikkaImageObject = Image.open("C:\\Users\\ayush\\Downloads\\Paneer-Tikka.jpg").resize((350, 334))
paneerTikkaImage = ImageTk.PhotoImage(paneerTikkaImageObject)

paneerButterMasalaImageObject = Image.open("C:\\Users\\ayush\\Downloads\\restaurant-style-paneer-butter-masala-2-500x500.jpg").resize((350, 334))
paneerButterMasalaImage = ImageTk.PhotoImage(paneerButterMasalaImageObject)

chickenGravyImageObject = Image.open("C:\\Users\\ayush\\Downloads\\Chicken Gravy.jpg").resize((350, 334))
chickenGravyImage = ImageTk.PhotoImage(chickenGravyImageObject)

malaiPrawnCurryImageObject = Image.open("C:\\Users\\ayush\\Downloads\\Malai Prawn Curry.jpg").resize((350, 334))
malaiPrawnCurryImage = ImageTk.PhotoImage(malaiPrawnCurryImageObject)

hyderabadiBiryaniImageObject = Image.open("C:\\Users\\ayush\\Downloads\\Hyderabadi Biryani.jpg").resize((350, 334))
hyderabadiBiryaniImage = ImageTk.PhotoImage(hyderabadiBiryaniImageObject)

butterChickenImageObject = Image.open("C:\\Users\\ayush\\Downloads\\butter-chicken-.jpg").resize((350, 334))
butterChickenImage = ImageTk.PhotoImage(butterChickenImageObject)

#endregion

#----------------------------------- WIDGETS ----------------------------------------------- #

# region Frames

# Section Frames
mainFrame = ttk.Frame(root, width=800, height=580, style='MainFrame.TFrame')
mainFrame.grid(row=0, column=0, sticky="NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row=0, column=0, sticky="NSEW", columnspan=3)

menuFrame = ttk.Frame(mainFrame, style='MenuFrame.TFrame')
menuFrame.grid(row=1, column=0, padx=3, pady=3, sticky="NSEW")

displayFrame = ttk.Frame(mainFrame, style="DisplayFrame.TFrame")
displayFrame.grid(row=1, column=1, padx=3, pady=3, sticky="NSEW")

orderFrame = ttk.Frame(mainFrame, style="OrderFrame.TFrame")
orderFrame.grid(row=1, column=2, padx=3, pady=3, sticky="NSEW")

# Dish Frames
paneerTikkaDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
paneerTikkaDishFrame.grid(row=1, column=0, sticky="NSEW")

paneerButterMasalaDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
paneerButterMasalaDishFrame.grid(row=2, column=0, sticky="NSEW")

chickenGravyDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
chickenGravyDishFrame.grid(row=3, column=0, sticky="NSEW")

malaiPrawnCurryDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
malaiPrawnCurryDishFrame.grid(row=4, column=0, sticky="NSEW")

hyderabadiBiryaniDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
hyderabadiBiryaniDishFrame.grid(row=5, column=0, sticky="NSEW")

butterChickenDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
butterChickenDishFrame.grid(row=6, column=0, sticky="NSEW")

#endregion

# region Top Banner Section

LogoLabel = ttk.Label(topBannerFrame, image=LogoImage, background="#222831")
LogoLabel.grid(row=0, column=0, sticky="W")

RestaurantBannerLabel = ttk.Label(topBannerFrame, image=TopBannerImage, background="#222831")
RestaurantBannerLabel.grid(row=0, column=1, sticky="NSEW")

# endregion

#region Menu Section
MainMenuLabel = ttk.Label(menuFrame, text="MENU", style="MenuLabel.TLabel")
MainMenuLabel.grid(row=0, column=0, sticky="WE")
MainMenuLabel.configure(anchor="center", font=("Helvetica", 16, "bold"))

PaneerTikkaDishLabel = ttk.Label(paneerTikkaDishFrame, text="Paneer Tikka ..... ₹350", style="MenuLabel.TLabel")
PaneerTikkaDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

PaneerButterMasalaDishLabel = ttk.Label(paneerButterMasalaDishFrame, text="Paneer Butter Masala ..... ₹400", style="MenuLabel.TLabel")
PaneerButterMasalaDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

ChickenGravyDishLabel = ttk.Label(chickenGravyDishFrame, text="Chicken Gravy ..... ₹450", style="MenuLabel.TLabel")
ChickenGravyDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

MalaiPrawnCurryDishLabel = ttk.Label(malaiPrawnCurryDishFrame, text="Malai Prawn Curry ..... ₹550", style="MenuLabel.TLabel")
MalaiPrawnCurryDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

HyderabadiBiryaniDishLabel = ttk.Label(hyderabadiBiryaniDishFrame, text="Hyderabadi Biryani ..... ₹500", style="MenuLabel.TLabel")
HyderabadiBiryaniDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

ButterChickenDishLabel = ttk.Label(butterChickenDishFrame, text="Butter Chicken ..... ₹425", style="MenuLabel.TLabel")
ButterChickenDishLabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

# Display buttons
PaneerTikkaDisplayButton = ttk.Button(paneerTikkaDishFrame, text="Display", command=lambda: update_display(paneerTikkaImage, "Paneer Tikka", 350), style='AccentButton.TButton')
PaneerTikkaDisplayButton.grid(row=0, column=1, padx=10, pady=5)

PaneerButterMasalaDisplayButton = ttk.Button(paneerButterMasalaDishFrame, text="Display", command=lambda: update_display(paneerButterMasalaImage, "Paneer Butter Masala", 400), style='AccentButton.TButton')
PaneerButterMasalaDisplayButton.grid(row=0, column=1, padx=10, pady=5)

ChickenGravyDisplayButton = ttk.Button(chickenGravyDishFrame, text="Display", command=lambda: update_display(chickenGravyImage, "Chicken Gravy", 450), style='AccentButton.TButton')
ChickenGravyDisplayButton.grid(row=0, column=1, padx=10, pady=5)

MalaiPrawnCurryDisplayButton = ttk.Button(malaiPrawnCurryDishFrame, text="Display", command=lambda: update_display(malaiPrawnCurryImage, "Malai Prawn Curry", 550), style='AccentButton.TButton')
MalaiPrawnCurryDisplayButton.grid(row=0, column=1, padx=10, pady=5)

HyderabadiBiryaniDisplayButton = ttk.Button(hyderabadiBiryaniDishFrame, text="Display", command=lambda: update_display(hyderabadiBiryaniImage, "Hyderabadi Biryani", 500), style='AccentButton.TButton')
HyderabadiBiryaniDisplayButton.grid(row=0, column=1, padx=10, pady=5)

ButterChickenDisplayButton = ttk.Button(butterChickenDishFrame, text="Display", command=lambda: update_display(butterChickenImage, "Butter Chicken", 425), style='AccentButton.TButton')
ButterChickenDisplayButton.grid(row=0, column=1, padx=10, pady=5)

# endregion

#region Display Section

displayLabel = ttk.Label(displayFrame, image=displayDefaultImage)
displayLabel.grid(row=0, column=0, padx=5, pady=5)

# endregion

#region Order Section

orderLabel = ttk.Label(orderFrame, text="ORDER", style="OrderTitle.TLabel")
orderLabel.grid(row=0, column=0, columnspan=2, pady=5, sticky="WE")

orderTransaction = ttk.Label(orderFrame, style="orderTransaction.TLabel")
orderTransaction.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

orderTotalLabel = ttk.Label(orderFrame, text="TOTAL: ₹0", style="orderTotalLabel.TLabel")
orderTotalLabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")

addButton = ttk.Button(orderFrame, text="Add to Order", command=add_to_order, style='GreenButton.TButton')  # Green button
addButton.grid(row=3, column=0, padx=10, pady=5)

removeButton = ttk.Button(orderFrame, text="Remove", command=remove_from_order, style='RedButton.TButton')  # Red button
removeButton.grid(row=3, column=1, padx=10, pady=5)

confirmButton = ttk.Button(orderFrame, text="Confirm Order", command=confirm_order, style='AccentButton.TButton')
confirmButton.grid(row=4, column=0, columnspan=2, padx=10, pady=5)



#endregion

root.mainloop()
