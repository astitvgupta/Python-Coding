from PIL import Image

# Load the image
image_path = r'C:\Users\hp\Documents\Code PlayGround\Python Coding\Python Projects\Image Reader Project\Capture.PNG'
image = Image.open(image_path)

# Get image size
width, height = image.size

# Convert the image to RGB and load pixel data
pixels = image.convert("RGB").load()

# Count the number of green pixels and the total number of pixels in the progress bar
green_pixel_count = 0
total_pixel_count = 0

# Define what we consider as "green"
green_range = ((0, 128, 0), (128, 255, 128))  # Approx range of green

# Loop through the image and count pixels
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        if green_range[0][0] <= r <= green_range[1][0] and green_range[0][1] <= g <= green_range[1][1] and green_range[0][2] <= b <= green_range[1][2]:
            green_pixel_count += 1
        total_pixel_count += 1

# Calculate the percentage of green pixels
completion_percentage = (green_pixel_count / total_pixel_count) * 100
print(f"{round(completion_percentage, 2)} % completed!")
