1#SyedaRameenZahra
#Intern at Prodigy Info Tech
#Task 2
# Pixel Maniulation for image Encryption
 


from PIL import Image

# Function to swap pixels at given coordinates (x1, y1) and (x2, y2)
def swapPix(image, x1, y1, x2, y2):
    # Get the width and height of the image
    wd, hg = image.size

    # Check if the coordinates are within the bounds of the image
    if x1 >= 0 and x1 < wd and y1 >= 0 and y1 < hg and x2 >= 0 and x2 < wd and y2 >= 0 and y2 < hg:
        # Get the pixel values at the given coordinates
        pix1 = image.getpixel((x1, y1))
        pix2 = image.getpixel((x2, y2))
        # Swap the pixel values
        image.putpixel((x1, y1), pix2)
        image.putpixel((x2, y2), pix1)

# Function to encrypt the image using a given key
def encryptImg(input_image_path, output_image_path, key):
    # Open the input image
    with Image.open(input_image_path) as img:
        # Get the width and height of the image
        width, height = img.size
        # Iterate through each pixel in the image
        for x in range(width):
            for y in range(height):
                # Get the RGB values of the pixel
                r, g, b = img.getpixel((x, y))
                # Add the encryption key to each RGB value
                img.putpixel((x, y), (r + key, g + key, b + key))
        # Save the encrypted image
        img.save(output_image_path)

# Function to decrypt the image using a given key
def decryptImg(input_image_path, output_image_path, key):
    # Open the input image
    with Image.open(input_image_path) as img:
        # Get the width and height of the image
        width, height = img.size
        # Iterate through each pixel in the image
        for x in range(width):
            for y in range(height):
                # Get the RGB values of the pixel
                r, g, b = img.getpixel((x, y))
                # Subtract the decryption key from each RGB value
                img.putpixel((x, y), (r - key, g - key, b - key))
        # Save the decrypted image
        img.save(output_image_path)

# Main function to provide user interaction
def main():
    while True:
        print("\n1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Swap Pixels")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            input_image = input("Enter the path of the input image: ")
            output_image = input("Enter the path for the encrypted image: ")
            key = int(input("Enter the encryption key (integer value): "))
            encryptImg(input_image, output_image, key)
            print("Image encrypted successfully!")

        elif choice == '2':
            input_image = input("Enter the path of the encrypted image: ")
            output_image = input("Enter the path for the decrypted image: ")
            key = int(input("Enter the decryption key (integer value): "))
            decryptImg(input_image, output_image, key)
            print("Image decrypted successfully!")

        elif choice == '3':
            input_image = input("Enter the path of the image for swapping: ")
            output_image = input("Enter the path for the image after swapping: ")
            x1, y1 = map(int, input("Enter the x and y coordinates of the first pixel separated by a comma: ").split(','))
            x2, y2 = map(int, input("Enter the x and y coordinates of the second pixel separated by a comma: ").split(','))
            with Image.open(input_image) as img:
                swapPix(img, x1, y1, x2, y2)
                img.save(output_image)
                print("Pixels swapped successfully!")
        elif choice == '4':
            print("Program has been Exited!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


       
if __name__ == "__main__":
    main()
