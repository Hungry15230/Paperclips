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
    increase_sell_speed_label.config(text=f"Increase sell speed to: {sell_speed + 1}/sec")
    increase_sell_speed_button.config(text=f"Upgrade (${sell_speed_upgrade_cost})", command=upgrade_sell_speed)
    auto_clipper_label.config(text=f"Auto clippers: {auto_clipper_amount}")
    buy_auto_clipper_button.config(text=f"Buy auto clipper (${auto_clipper_cost})")


def buy_wire():
    global wire_cost, wire, money
    if money >= wire_cost:
        money -= wire_cost
        wire += 50
        update_display()


def buy_auto_clipper():
    global money, auto_clipper_cost, auto_clipper_amount
    if money >= auto_clipper_cost:
        money -= auto_clipper_cost
        auto_clipper_amount += 1
        auto_clipper_cost *= 1.5
        update_display()


def generate_wire_cost():
    global wire_cost
    wire_cost = random.randint(14, 30)
    update_display()
    root.after(10000, generate_wire_cost)


def sell_paperclips():
    global paperclips, money, sell_speed
    sold_per_sec = int(1000 / sell_speed)
    # 2 being sold every second
    # 1 sold every 0.5 sec
    # 1000 ms / num of clips = speed of clip selling
    print(f"1 paperclip being sold every {sold_per_sec/1000} sec")

    if paperclips > 0:
        money += 1
        paperclips -= 1
        update_display()

    root.after(sold_per_sec, sell_paperclips)


def upgrade_sell_speed():
    global money, sell_speed, sell_speed_upgrade_cost
    if money >= sell_speed_upgrade_cost:
        money -= sell_speed_upgrade_cost
        sell_speed += 1
        sell_speed_upgrade_cost *= 1.5


def auto_clip():
    global paperclips, total_clips, wire, auto_clipper_amount

    if auto_clipper_amount > 0 and wire > 0:
        for _ in range(auto_clipper_amount):
            total_clips += 1
            paperclips += 1
            wire -= 1
            update_display()

    root.after(1000, auto_clip)


money = 0
paperclips = 0
total_clips = 0
wire = 100
wire_cost = random.randint(14, 30)
sell_speed = 1
sell_speed_upgrade_cost = 100
auto_clipper_amount = 0
auto_clipper_cost = 50

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
# Display Total Clips
total_clips_label = tk.Label(main_screen, text=f"Total paperclips: {total_clips}")
total_clips_label.pack()
# Display money
money_label = tk.Label(main_screen, text=f"${money}")
money_label.pack()
# Display sell speed label/upgrades
increase_sell_speed_label = tk.Label(main_screen, text=f"Increase sell speed to: {sell_speed + 1}/sec")
increase_sell_speed_label.pack()
increase_sell_speed_button = tk.Button(main_screen, text=f"Upgrade (${sell_speed_upgrade_cost})",
                                       command=upgrade_sell_speed)
increase_sell_speed_button.pack()
# Display current paperclips/make clips button
paperclips_label = tk.Label(main_screen, text=f"Paperclips: {paperclips}")
paperclips_label.pack()
make_paperclips_button = tk.Button(main_screen, text="Make paperclip (1 Wire)", command=make_paperclip)
make_paperclips_button.pack()
# Display current wire amt/upgrades
wire_label = tk.Label(main_screen, text=f"Wire: {wire}")
wire_label.pack()
buy_wire_button = tk.Button(main_screen, text=f"Buy 50 wire (${wire_cost})", command=buy_wire)
buy_wire_button.pack()
# Display auto clippers/upgrades
auto_clipper_label = tk.Label(main_screen, text=f"Auto clippers: {auto_clipper_amount}")
auto_clipper_label.pack()
buy_auto_clipper_button = tk.Button(main_screen, text=f"Buy auto clipper (${auto_clipper_cost})",
                                    command=buy_auto_clipper)
buy_auto_clipper_button.pack()

# Main loop
generate_wire_cost()
sell_paperclips()
update_display()
auto_clip()
root.mainloop()
