from PIL import Image, ImageDraw, ImageFont

# Create a blank image
img = Image.new('RGB', (600, 400), color='white')
d = ImageDraw.Draw(img)

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", 15)
except IOError:
    font = ImageFont.load_default()

# Draw the main rectangle for the use case diagram
d.rectangle([(50, 50), (550, 350)], outline='black', width=3)

# Draw ellipses for use cases with thicker lines and different colors
d.ellipse([(150, 100), (200, 150)], outline='blue', width=2)  # Start Pomodoro
d.ellipse([(150, 200), (200, 250)], outline='green', width=2)  # End Pomodoro
d.ellipse([(350, 100), (400, 150)], outline='red', width=2)  # View Stats

# Add labels with larger font
d.text((110, 40), "User", fill='black', font=font)
d.text((160, 120), "Start\nPomodoro", fill='black', font=font)
d.text((160, 220), "End\nPomodoro", fill='black', font=font)
d.text((360, 120), "View\nStats", fill='black', font=font)

# Draw arrows to indicate relationships
d.line([(100, 60), (175, 100)], fill='black', width=2)
d.polygon([(170, 95), (175, 100), (170, 105)], fill='black')  # Arrowhead

d.line([(100, 60), (175, 200)], fill='black', width=2)
d.polygon([(170, 195), (175, 200), (170, 205)], fill='black')  # Arrowhead

d.line([(100, 60), (375, 100)], fill='black', width=2)
d.polygon([(370, 95), (375, 100), (370, 105)], fill='black')  # Arrowhead

# Draw a border around the diagram
d.rectangle([(10, 10), (590, 390)], outline='black', width=2)

# Save the image in the current directory
img.save("use_case_diagram1.png")