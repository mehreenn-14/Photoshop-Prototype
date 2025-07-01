from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

# ------ Browse img from your computer --------
def browseImg():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Select image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    if file_path:
        entry.delete(0, END)
        entry.insert(0, file_path)
        browse_btn.pack_forget()
        display_btn.pack(pady=10)


def displayImg():
    global img
    img = Image.open(file_path)
    img = img.resize((200, 200))
    tk_img = ImageTk.PhotoImage(img)
    img_label.configure(image=tk_img)
    img_label.image = tk_img
    display_btn.pack_forget()
    filter_label.pack()
    filter_menu.pack()
    apply_btn.pack(pady=5)


# ------- Apply selected filter --------
def applyFilter():
    selected_filter = filter_var.get()
    filtered_img = img.copy()

    filter_map = {
        "BLUR": ImageFilter.BLUR,
        "CONTOUR": ImageFilter.CONTOUR,
        "DETAIL": ImageFilter.DETAIL,
        "SHARPEN": ImageFilter.SHARPEN,
        "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE
    }

    if selected_filter in filter_map:
        filtered_img = filtered_img.filter(filter_map[selected_filter])

    resized = filtered_img.resize((200, 200))
    tk_img = ImageTk.PhotoImage(resized)
    img_label.configure(image=tk_img)
    img_label.image = tk_img


# ------- Application setup -----------
win = Tk()
win.title("PhotoShop")
win.geometry('600x500')
win.iconbitmap(r"C:\Users\mehre\Downloads\application_photoshop_2442.ico")
win.configure(bg="#ffffff")

entry = Entry(win, width=50)
entry.pack(padx=5, pady=5)

browse_btn = Button(win, text="Browse", font=(20), command=browseImg)
browse_btn.pack()

display_btn = Button(win, text="Display", font=(20), command=displayImg)

# -------- Filter dropdown menu
filter_var = StringVar()
filter_var.set("BLUR")
filters = ["BLUR", "CONTOUR", "DETAIL", "SHARPEN", "EDGE_ENHANCE"]

filter_label = Label(win, text="Select Filter:", bg="#ffffff")
filter_menu = OptionMenu(win, filter_var, *filters)
apply_btn = Button(win, text="Apply Filter", command=applyFilter)


# Image display area
img_label = Label(win)
img_label.pack(pady=10)

win.mainloop()
