# Author: Larbi OUIYZME
# Version: 1.1
# Date: March 8, 2024

import base64

def encode_base64(data):
    """
    Encode data into Base64 format.
    
    Args:
        data (str): The data to be encoded.
    
    Returns:
        str: The encoded data.
    """
    encoded_bytes = base64.urlsafe_b64encode(data.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

def decode_base64(encoded_string):
    """
    Decode Base64 encoded data.
    
    Args:
        encoded_string (str): The Base64 encoded string.
    
    Returns:
        str: The decoded data.
    """
    # If the length of the encoded string is not a multiple of 4, add padding ('==')
    if len(encoded_string) % 4 != 0:
        encoded_string += '=' * (4 - len(encoded_string) % 4)
    decoded_bytes = base64.urlsafe_b64decode(encoded_string.encode('utf-8'))
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string

def main():
    """
    Main function to handle user input and perform encoding/decoding.
    """
    while True:
        choice = input("Enter 'e' to encode, 'd' to decode, or 'q' to quit: ").strip().lower()
        
        if choice == 'e':
            data = input("Enter the message to encode: ").strip()
            encoded_data = encode_base64(data)
            print("Encoded message:", encoded_data)
            print("-" * 50)  # Add a line after encoding
        elif choice == 'd':
            encoded_data = input("Enter the message to decode: ").strip()
            decoded_data = decode_base64(encoded_data)
            print("Decoded message:", decoded_data)
            if len(encoded_data) % 4 != 0:
                print("Note: '==' padding added to the original encoded message.")
            print("-" * 50)  # Add a line after decoding
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
