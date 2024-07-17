from PIL import Image, ImageDraw, ImageFont

# Create a blank image
img = Image.new('RGB', (600, 400), color='white')
d = ImageDraw.Draw(img)

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", 15)
except IOError:
    font = ImageFont.load_default()

# Draw lifelines with thicker lines and different colors
d.line([(50, 50), (50, 350)], fill='blue', width=3)
d.line([(150, 50), (150, 350)], fill='green', width=3)
d.line([(250, 50), (250, 350)], fill='red', width=3)
d.line([(350, 50), (350, 350)], fill='purple', width=3)

# Add labels with larger font
d.text((40, 30), "User", fill='black', font=font)
d.text((140, 30), "CLI", fill='black', font=font)
d.text((240, 30), "App", fill='black', font=font)
d.text((340, 30), "DB", fill='black', font=font)

# Draw arrows for messages
d.line([(50, 100), (150, 100)], fill='black', width=2)
d.polygon([(145, 95), (150, 100), (145, 105)], fill='black')  # Arrowhead

d.line([(150, 120), (250, 120)], fill='black', width=2)
d.polygon([(245, 115), (250, 120), (245, 125)], fill='black')  # Arrowhead

d.line([(250, 140), (350, 140)], fill='black', width=2)
d.polygon([(345, 135), (350, 140), (345, 145)], fill='black')  # Arrowhead

d.line([(50, 200), (150, 200)], fill='black', width=2)
d.polygon([(145, 195), (150, 200), (145, 205)], fill='black')  # Arrowhead

d.line([(150, 220), (250, 220)], fill='black', width=2)
d.polygon([(245, 215), (250, 220), (245, 225)], fill='black')  # Arrowhead

d.line([(250, 240), (350, 240)], fill='black', width=2)
d.polygon([(345, 235), (350, 240), (345, 245)], fill='black')  # Arrowhead

# Draw a border around the diagram
d.rectangle([(10, 10), (590, 390)], outline='black', width=2)

# Save the image in the current directory
img.save("sequence_diagram.png")