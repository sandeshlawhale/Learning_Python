# This file explains computer image fundamentals using Pillow.
# Topics covered:
# 1. Coordinates and box tuples
# 2. Working with Image data type
# 3. Cropping images
# 4. Copying image on another image
# 5. Resizing images
# 6. Rotating and flipping images
# 7. Changing individual pixels

from PIL import Image
import os

os.chdir('.\\17. manipulating images')

# Open image
image = Image.open('example.png')

# Print image size
print('Image Size:', image.size)

# Print width and height
print('Width:', image.width)
print('Height:', image.height)

# Coordinates:
# (0,0) -> top-left corner

# Box tuple:
# (left, top, right, bottom)

# Crop image
croppedImage = image.crop((300, 350, 600, 600))

croppedImage.save('cropped.png')

print('\nImage cropped successfully.')

# Copy image
copiedImage = image.copy()

# Resize image
resizedImage = image.resize((300, 300))

resizedImage.save('resized.png')

print('Image resized successfully.')

# Rotate image
rotatedImage = image.rotate(90)

rotatedImage.save('rotated.png')

print('Image rotated successfully.')

# Flip image horizontally
flippedImage = image.transpose(Image.FLIP_LEFT_RIGHT)

flippedImage.save('flipped.png')

print('Image flipped successfully.')

# Change individual pixel
image.putpixel((10, 10), (255, 0, 0))

image.save('pixelChanged.png')

print('Pixel modified successfully.')