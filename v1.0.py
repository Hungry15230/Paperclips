import tkinter as tk
import random


def start_game():
    start_screen.pack_forget()
    main_screen.pack()


def center_window():
    # Function to center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = screen_width
    window_height = screen_height
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}')


def make_paperclip():
    global paperclips, wire, total_clips
    if wire > 0:
        wire -= 1
        paperclips += 1
        total_clips += 1
        update_display()


def update_display():
    total_clips_label.config(text=f"Total paperclips: {total_clips}")
    money_label.config(text=f"${money}")
    paperclips_label.config(text=f"Paperclips: {paperclips}")
    wire_label.config(text=f"Wire: {wire}")
    make_paperclips_button.config(text="Make paperclip (1 Wire)", command=make_paperclip)
    buy_wire_button.config(text=f"Buy 50 wire (${wire_cost})", command=buy_wire)


def buy_wire():
    global wire_cost, wire, money
    if money >= wire_cost:
        money -= wire_cost
        wire += 50
        update_display()


def generate_wire_cost():
    global wire_cost
    wire_cost = random.randint(14, 30)
    update_display()
    root.after(10000, generate_wire_cost)


def sell_paperclips():
    global paperclips, money
    rate = 1  # Rate at which clips are being sold
    if paperclips >= 1:
        paperclips -= 1
        money += 1
        update_display()

    root.after(rate*1000, sell_paperclips)


money = 0
paperclips = 0
total_clips = 0
wire = 100
wire_cost = random.randint(14, 30)

root = tk.Tk()
root.title("Worldly Paperclips")
center_window()

# Create the start screen
start_screen = tk.Frame(root)
start_screen.pack(expand=True)
# Creates a title with custom font
custom_font = ("Roboto", 14, "bold")
title = tk.Label(start_screen, text="Worldly Paperclips", font=custom_font)
title.pack()
# Center the button both horizontally and vertically
start_button = tk.Button(start_screen, text="Start Game", command=start_game)
start_button.pack(pady=20)  # Add vertical space around the button
exit_button = tk.Button(start_screen, text="Exit", command=exit)
exit_button.pack(pady=20)

disclaimer_label = tk.Label(start_screen, text="DISCLAIMER: This game is not mine, it is just a python remake of "
                                               "Universal Paperclips.", font="bold")
disclaimer_label.pack()


# Create the main screen
main_screen = tk.Frame(root)
total_clips_label = tk.Label(main_screen, text=f"Total paperclips: {total_clips}")
total_clips_label.pack()

money_label = tk.Label(main_screen, text=f"${money}")
money_label.pack()

paperclips_label = tk.Label(main_screen, text=f"Paperclips: {paperclips}")
paperclips_label.pack()
make_paperclips_button = tk.Button(main_screen, text="Make paperclip (1 Wire)", command=make_paperclip)
make_paperclips_button.pack()

wire_label = tk.Label(main_screen, text=f"Wire: {wire}")
wire_label.pack()
buy_wire_button = tk.Button(main_screen, text=f"Buy 50 wire (${wire_cost})", command=buy_wire)
buy_wire_button.pack()


# Main loop
generate_wire_cost()
sell_paperclips()
update_display()
root.mainloop()
