from PIL import Image, ImageDraw

# Create a blank image
img = Image.new('RGB', (600, 400), color='white')
d = ImageDraw.Draw(img)

# Draw Class Diagram
d.rectangle([(100, 50), (500, 150)], outline='black')  # Pomodoro Class
d.line([(300, 150), (300, 350)], fill='black')         # Divider

d.text((200, 60), "Pomodoro", fill='black')
d.text((110, 100), "+ start(): void", fill='black')
d.text((110, 130), "+ end(): void", fill='black')
d.text((310, 160), "+ duration: int", fill='black')
d.text((310, 190), "+ task: str", fill='black')
d.text((310, 220), "+ start_time: datetime", fill='black')
d.text((310, 250), "+ end_time: datetime", fill='black')

img.save("class_diagram.png")
