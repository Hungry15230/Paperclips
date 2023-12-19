import tkinter as tk


def gold_upgrade():
    global gold, gold_per_second, gold_upgrade_cost
    if gold >= gold_upgrade_cost:
        gold -= gold_upgrade_cost
        gold_per_second += 2  # Increase gold per second by a certain amount
        gold_upgrade_cost += 10  # Increase upgrade cost
        update_display()


def wood_upgrade():
    global gold, wood_per_second, wood_upgrade_cost
    if gold >= wood_upgrade_cost:
        gold -= gold_upgrade_cost
        wood_per_second += 1
        wood_upgrade_cost += 10
        update_display()


def increase_gold():
    global gold
    gold += gold_per_second
    update_display()
    root.after(1000, increase_gold)  # Call itself after 1000 milliseconds (1 second)


def increase_wood():
    global wood
    wood += wood_per_second
    update_display()
    root.after(1000, increase_wood)  # Call itself after 1000 milliseconds (1 second)


def update_display():
    gold_label.config(text=f"Gold: {gold} (Earns {gold_per_second} per second)")
    gold_upgrade_button.config(text=f"Upgrade ({gold_upgrade_cost} Gold)")

    wood_label.config(text=f"Wood: {wood} (Earns {wood_per_second} per second)")
    wood_upgrade_button.config(text=f"Upgrade ({wood_upgrade_cost} Gold)")


wood = 0
wood_per_second = 0
wood_upgrade_cost = 100
gold = 0
gold_per_second = 1
gold_upgrade_cost = 10

root = tk.Tk()
root.title("Upgrade Game")

gold_label = tk.Label(root, text=f"Gold: {gold} (Earns {gold_per_second} per second)")
gold_label.place(x=20, y=20)
gold_upgrade_button = tk.Button(root, text=f"Upgrade ({gold_upgrade_cost} Gold)", command=gold_upgrade)
gold_upgrade_button.place(x=20, y=50)

wood_label = tk.Label(root, text=f"Wood: {wood} (Earns {wood_per_second} per second)")
wood_label.place(x=20, y=100)
wood_upgrade_button = tk.Button(root, text=f"Upgrade ({wood_upgrade_cost} Gold)", command=wood_upgrade)
wood_upgrade_button.place(x=20, y=130)

increase_gold()
increase_wood()
update_display()

root.mainloop()
