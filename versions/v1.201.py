import tkinter as tk
import random

def create_start_screen():
    def start_game():
        start_screen.destroy()
        main_screen.place(x=0, y=0)
    # Create the start screen
    start_screen = tk.Frame(root, width=screen_width, height=screen_height)
    start_screen.place(x=0, y=0)  # Place the frame in the top-left corner
    # Creates a title with custom font
    custom_font = ("Roboto", 14, "bold")
    title = tk.Label(start_screen, text="Worldly Paperclips", font=custom_font)
    title.place(x=(screen_width / 2) - title.winfo_reqwidth() / 2, y=screen_height / 4)
    # Display Start button
    start_button = tk.Button(start_screen, text="Start Game", command=start_game)
    start_button.place(x=(screen_width / 2) - start_button.winfo_reqwidth() / 2, y=screen_height / 2)
    # Display Exit button
    exit_button = tk.Button(start_screen, text="Exit", command=root.destroy)
    exit_button.place(x=(screen_width / 2) - exit_button.winfo_reqwidth() / 2, y=(screen_height / 4) * 3)
    # Display Disclaimer
    disclaimer = tk.Label(start_screen, text="DISCLAIMER: This game is not mine, it is just a python remake of Universal Paperclips.", font="bold")
    disclaimer.place(x=(screen_width / 2) - disclaimer.winfo_reqwidth() / 2, y=screen_height)
    # Display Changelog
    changelog = tk.Label(start_screen, text="Changelog:\nAdded: \nFixed: Exit button size in-game")
    changelog.place(x=0, y=screen_height - changelog.winfo_reqheight())


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


def sell_paperclips():
    global paperclips, money, sell_speed
    sold_per_sec = int(1000 / sell_speed)
    # 2 being sold every second
    # 1 sold every 0.5 sec
    # 1000 ms / num of clips = speed of clip selling
    print(f"1 paperclip being sold every {sold_per_sec / 1000} sec")

    if paperclips > 0:
        money += 1
        paperclips -= 1
        update_display()

    root.after(sold_per_sec, sell_paperclips)


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


def generate_wire_cost():
    global wire_cost
    wire_cost = random.randint(14, 30)
    update_display()
    root.after(10000, generate_wire_cost)


def update_display():
    total_clips_label.config(text=f"Total paperclips: {total_clips}", font=("Roboto", 50, "bold"))
    money_label.config(text=f"Available funds: {money}", font=label_font)
    paperclips_label.config(text=f"Paperclips: {paperclips}", font=label_font)
    wire_label.config(text=f"Wire: {wire}", font=label_font)
    increase_sell_speed_label.config(text=f"Increase sell speed to: {sell_speed + 1}/sec", font=label_font)
    auto_clipper_label.config(text=f"Auto clippers: {auto_clipper_amount}", font=label_font)
    make_paperclips_button.config(text="Make paperclip (1 Wire)", command=make_paperclip)
    buy_wire_button.config(text=f"Buy 50 wire (${wire_cost})", command=buy_wire)
    increase_sell_speed_button.config(text=f"Upgrade (${sell_speed_upgrade_cost})", command=upgrade_sell_speed)
    buy_auto_clipper_button.config(text=f"Buy auto clipper (${auto_clipper_cost})")


def get_next_y_coord(last_widget):
    root.update_idletasks()
    return last_widget.winfo_y() + last_widget.winfo_reqheight()

root = tk.Tk()
root.title("Worldly Paperclips")
root.attributes('-fullscreen', True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
money = 0
paperclips = 0
total_clips = 0
wire = 100
wire_cost = random.randint(14, 30)
sell_speed = 1
sell_speed_upgrade_cost = 100
auto_clipper_amount = 0
auto_clipper_cost = 50
label_font = ("Roboto", 20)

create_start_screen()

main_screen = tk.Frame(root, width=screen_width, height=screen_height)

total_clips_label = tk.Label(main_screen, text=f"Total paperclips: {total_clips}", font=("Roboto", 50, "bold"))
total_clips_label.place(x=0, y=0)
y_coord = get_next_y_coord(total_clips_label)

money_label = tk.Label(main_screen, text=f"Available funds: {money}", font=label_font)
money_label.place(x=5, y=y_coord+5)
y_coord = get_next_y_coord(money_label)

increase_sell_speed_label = tk.Label(main_screen, text=f"Increase sell speed to: {sell_speed + 1}/sec", font=label_font)
increase_sell_speed_label.place(x=5, y=y_coord)
y_coord = get_next_y_coord(increase_sell_speed_label)

increase_sell_speed_button = tk.Button(main_screen, text=f"Upgrade (${sell_speed_upgrade_cost})", command=upgrade_sell_speed)
increase_sell_speed_button.place(x=5, y=y_coord)
y_coord = get_next_y_coord(increase_sell_speed_button)

paperclips_label = tk.Label(main_screen, text=f"Paperclips: {paperclips}", font=label_font)
paperclips_label.place(x=5, y=y_coord)
y_coord = get_next_y_coord(paperclips_label)

make_paperclips_button = tk.Button(main_screen, text="Make paperclip (1 Wire)", command=make_paperclip)
make_paperclips_button.place(x=5, y=y_coord)
y_coord = get_next_y_coord(make_paperclips_button)

wire_label = tk.Label(main_screen, text=f"Wire: {wire}", font=label_font)
wire_label.place(x=5, y=y_coord)
y_coord = get_next_y_coord(wire_label)

buy_wire_button = tk.Button(main_screen, text=f"Buy 50 wire (${wire_cost})", command=buy_wire)
buy_wire_button.place(x=5, y=y_coord)
y_coord = get_next_y_coord(buy_wire_button)

auto_clipper_label = tk.Label(main_screen, text=f"Auto clippers: {auto_clipper_amount}", font=label_font)
auto_clipper_label.place(x=5, y=y_coord)
y_coord = get_next_y_coord(auto_clipper_label)

buy_auto_clipper_button = tk.Button(main_screen, text=f"Buy auto clipper (${auto_clipper_cost})", command=buy_auto_clipper)
buy_auto_clipper_button.place(x=5, y=y_coord)

exit_button = tk.Button(main_screen, text="EXIT", command=root.destroy, font=20)
exit_button.place(x=screen_width - exit_button.winfo_reqwidth(), y=0)

# Main loop
generate_wire_cost()
sell_paperclips()
update_display()
auto_clip()
root.mainloop()
