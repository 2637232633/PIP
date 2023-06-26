import os
import fire
import string
import random
from typing import Tuple, List
from aes import AES
from lsb import LSB


class CLI:
    @staticmethod
    def encrypt(input_path: str, output_path: str, message: str, message_pwd: str) -> Tuple[str, int]:
        """Encryption of secret message into the input image using AES and LSB steganography"""

        def _generate_pixel_location_pwd() -> str:
            temp = string.digits + string.ascii_letters
            temp_pwd = random.choices(temp, k=64)
            return ''.join(temp_pwd)

        if os.path.exists(input_path):
            if os.path.exists(output_path):
                os.remove(output_path)
            en_message = AES.encrypt(message, message_pwd)
            plp = _generate_pixel_location_pwd()
            output_image = LSB.encode(input_path, en_message, plp)
            output_image.save(output_path)
            return plp, len(en_message)
        else:
            return 'Input Wrong Image'

    @staticmethod
    def decrypt(output_path: str, message_pwd: str, plp: str, len_en_message: int) -> str:
        """Decrypting secret message from input steganographic images using AES and LSB steganography"""

        if os.path.exists(output_path):
            de_text = LSB.decode(output_path, plp, len_en_message)
            de_message = AES.decrypt(de_text, message_pwd)
            return de_message
        else:
            return "Input Wrong Image"

fire.Fire(CLI)