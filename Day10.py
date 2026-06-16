from tkinter import *
import random

# Create window
root = Tk()
root.title("Car Racing Game")
root.geometry("400x600")
root.resizable(False, False)

# Canvas
canvas = Canvas(root, width=400, height=600, bg="gray")
canvas.pack()

# Road lines
for i in range(0, 600, 100):
    canvas.create_line(200, i, 200, i + 50, fill="white", width=5)

# Player car
player = canvas.create_rectangle(180, 500, 220, 550, fill="blue")

# Enemy car
enemy = canvas.create_rectangle(180, 50, 220, 100, fill="red")

score = 0
score_text = canvas.create_text(
    50, 20,
    text="Score: 0",
    fill="white",
    font=("Arial", 16)
)

enemy_speed = 5


# Move player
def move_left(event):
    x1, y1, x2, y2 = canvas.coords(player)
    if x1 > 0:
        canvas.move(player, -20, 0)


def move_right(event):
    x1, y1, x2, y2 = canvas.coords(player)
    if x2 < 400:
        canvas.move(player, 20, 0)


# Move enemy car
def move_enemy():
    global score

    canvas.move(enemy, 0, enemy_speed)

    ex1, ey1, ex2, ey2 = canvas.coords(enemy)
    px1, py1, px2, py2 = canvas.coords(player)

    # Collision detection
    if ex2 > px1 and ex1 < px2 and ey2 > py1 and ey1 < py2:
        canvas.create_text(
            200, 300,
            text="GAME OVER",
            fill="yellow",
            font=("Arial", 25, "bold")
        )
        return

    # Reset enemy and increase score
    if ey2 > 600:
        score += 1
        canvas.itemconfig(score_text, text=f"Score: {score}")

        new_x = random.randint(50, 350)
        canvas.coords(enemy, new_x, 0, new_x + 40, 50)

    root.after(50, move_enemy)


# Keyboard controls
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

move_enemy()

root.mainloop()