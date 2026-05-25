# This file explains drawing on images using Pillow.
# Topics covered:
# 1. Drawing shapes
# 2. Points
# 3. Lines
# 4. Rectangles
# 5. Ellipses
# 6. Polygons
# 7. Drawing text

from PIL import Image, ImageDraw
import os

os.chdir('.\\17. manipulating images')

# Create blank image
image = Image.new('RGBA', (400, 400), 'white')

# Create drawing object
draw = ImageDraw.Draw(image)

# Draw point
draw.point((50, 50), fill='red')

# Draw line
draw.line((60, 60, 200, 60), fill='blue', width=3)

# Draw rectangle
draw.rectangle((50, 100, 200, 200), outline='black', fill='yellow')

# Draw ellipse
draw.ellipse((220, 100, 350, 200), outline='green', fill='pink')

# Draw polygon
draw.polygon(
    ((100, 250), (200, 300), (150, 350)),
    outline='purple',
    fill='orange'
)

# Draw text
draw.text((50, 20), 'Hello Pillow!', fill='black')

# Save image
image.save('drawingExample.png')

print('Drawing created successfully.')