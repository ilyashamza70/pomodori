from PIL import Image, ImageDraw, ImageFont

# Create a blank image
img = Image.new('RGB', (600, 400), color='white')
d = ImageDraw.Draw(img)

# Define font
font = ImageFont.truetype("arial.ttf", 15)

# Draw System Diagram
d.rectangle([(100, 50), (500, 150)], outline='black')  # System
d.rectangle([(150, 100), (250, 140)], outline='black')  # CLI
d.rectangle([(350, 100), (450, 140)], outline='black')  # Web App
d.rectangle([(250, 200), (350, 240)], outline='black')  # Database

d.text((270, 40), "System", fill='black', font=font)
d.text((170, 110), "CLI", fill='black', font=font)
d.text((370, 110), "Web App", fill='black', font=font)
d.text((280, 210), "Database", fill='black', font=font)

img.save("system_diagram.png")
