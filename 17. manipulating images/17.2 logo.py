# Project: Adding a Logo to Images
# This program:
# 1. Loads logo image
# 2. Loops through all JPG images in directory
# 3. Resizes images if width or height is greater than 300
# 4. Adds logo to bottom-right corner
# 5. Saves modified images

from PIL import Image
import os

os.chdir('.\\17. manipulating images')

# Logo filename
logoFilename = 'catlogo.png'

# Open logo image
logoImage = Image.open(logoFilename)

# Get logo width and height
logoWidth, logoHeight = logoImage.size

# Create output folder
os.makedirs('withLogo', exist_ok=True)

# Loop through all files in current directory
for filename in os.listdir('.'):

    # Process only JPG files
    if filename.endswith('.jpg') or filename.endswith('.png'):

        print('Adding logo to:', filename)

        # Open image
        image = Image.open(filename)

        # Get image size
        width, height = image.size

        # Resize image if needed
        if width > 300 or height > 300:

            # Resize proportionally
            if width > height:

                height = int((300 / width) * height)

                width = 300

            else:

                width = int((300 / height) * width)

                height = 300

            image = image.resize((width, height))

        # Skip image if too small for logo
        if width < logoWidth * 2 or height < logoHeight * 2:

            print('Image too small for logo.')

            continue

        # Calculate logo position
        position = (
            width - logoWidth,
            height - logoHeight
        )

        # Paste logo
        image.paste(logoImage, position, logoImage)

        # Save modified image
        image.save(
            os.path.join(
                'withLogo',
                filename
            )
        )

print('Logo added to all images.')