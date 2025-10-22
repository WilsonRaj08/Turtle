import turtle

# --- Setup Turtle ---
t = turtle.Turtle()

# --- User Inputs ---
print("🎨 Welcome to Turtle Spiral Art!")
speed = int(input("Enter the turtle speed (1–10, higher = faster): "))
color1 = input("Enter the first color: ")
color2 = input("Enter the second color: ")
bg = input("Enter the background color: ")

# --- Apply Settings ---
t.speed(speed)
turtle.bgcolor(bg)

# --- Drawing Magic ---
for i in range(300):
    # Alternate between the two colors
    t.color(color1 if i % 2 == 0 else color2)
    t.circle(i)
    t.right(7)

# --- End ---
turtle.done()
