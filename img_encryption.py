from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Encrypt the image by adding the key to each pixel value
    encrypted_image_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(np.uint8(encrypted_image_array))

    # Save the encrypted image
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Open the image
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Decrypt the image by subtracting the key from each pixel value
    decrypted_image_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(np.uint8(decrypted_image_array))

    # Save the decrypted image
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

def main():
    choice = input("Choose an option: (1) Encrypt Image (2) Decrypt Image: ")
    if choice == '1':
        input_image_path = input("Enter the path of the image to encrypt: ")
        output_image_path = input("Enter the path to save the encrypted image: ")
        key = int(input("Enter the encryption key (an integer): "))
        encrypt_image(input_image_path, output_image_path, key)
    elif choice == '2':
        input_image_path = input("Enter the path of the image to decrypt: ")
        output_image_path = input("Enter the path to save the decrypted image: ")
        key = int(input("Enter the decryption key (an integer): "))
        decrypt_image(input_image_path, output_image_path, key)
    else:
        print("Invalid choice. Please select (1) or (2).")

if __name__ == "__main__":
    main()
