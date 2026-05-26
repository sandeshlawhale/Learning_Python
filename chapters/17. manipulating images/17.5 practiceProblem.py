# Practice Project: Extending and Fixing the Chapter Project Programs
# This program:
# 1. Supports JPG, PNG, GIF, and BMP images
# 2. Handles uppercase and lowercase extensions
# 3. Adds logo only if image is large enough

from PIL import Image
import os

os.chdir('.\\17. manipulating images')

# Logo filename
logoFilename = 'logo.png'

# Open logo image
logoImage = Image.open(logoFilename)

# Logo size
logoWidth, logoHeight = logoImage.size

# Create output folder
os.makedirs('updatedImages', exist_ok=True)

# Supported extensions
extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

# Loop through files
for filename in os.listdir('.'):

    # Check file extension
    if filename.lower().endswith(extensions):

        print('Processing:', filename)

        # Open image
        image = Image.open(filename)

        width, height = image.size

        # Resize image if needed
        if width > 300 or height > 300:

            if width > height:

                height = int((300 / width) * height)

                width = 300

            else:

                width = int((300 / height) * width)

                height = 300

            image = image.resize((width, height))

        # Skip small images
        if width < logoWidth * 2 or height < logoHeight * 2:

            print('Skipped small image.')

            continue

        # Logo position
        position = (
            width - logoWidth,
            height - logoHeight
        )

        # Paste logo
        image.paste(logoImage, position, logoImage)

        # Save updated image
        image.save(
            os.path.join(
                'updatedImages',
                filename
            )
        )

print('All images processed successfully.')