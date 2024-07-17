from PIL import Image, ImageDraw, ImageFont

# Create a blank image
img = Image.new('RGB', (600, 400), color='white')
d = ImageDraw.Draw(img)

# Define font
font = ImageFont.truetype("arial.ttf", 15)

# Draw Deployment Diagram
d.rectangle([(100, 50), (500, 150)], outline='black')  # Docker Container
d.rectangle([(150, 100), (250, 140)], outline='black')  # CLI
d.rectangle([(350, 100), (450, 140)], outline='black')  # Web App

d.text((250, 40), "Docker Container", fill='black', font=font)
d.text((170, 110), "CLI", fill='black', font=font)
d.text((370, 110), "Web App", fill='black', font=font)

img.save("deployment_diagram1.png")
