from cli import CLI



if __name__ == '__main__':
    input_image_path = ""
    output_image_path = ""
    message_password ="123123"

    cli = CLI()
    # encrypt
    pixel_location_password, len_encoded_message = cli.encrypt(input_image_path, output_image_path, message_password)
    #decrypt
    decrypted_message = cli.decrypt(output_image_path, message_password, pixel_location_password, len_encoded_message)

