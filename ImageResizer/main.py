from PIL import Image

# Open an image file
#image_path =Image.open("bg_1.jpg.jpg")
with Image.open("bg_1.jpg") as img:
    # Print original size
    print(f"Original size: {img.size}")

    # Set the desired size
    new_width = 200
    new_height = 200

    # Resize the image
    img_resized = img.resize((new_width, new_height))

    # Save the resized image
    img_resized.save("resized_image.jpg")

    # Print new size
    print(f"Resized size: {img_resized.size}")