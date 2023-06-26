import numpy as np
from PIL import Image
from hashlib import sha512
from typing import Tuple, List

class LSB:
    @staticmethod
    def get_pixel_location(width: int, height: int, len_en_message: int, plp: str) -> List[int]:
        """This function generates a list of pixel locations, given the pixel location password,
        the size of the image, and the length of the encoded information"""

        plp_seed = plp.encode()
        plp_seed = plp_seed + sha512(plp_seed).digest()
        plp_seed = int.from_bytes(plp_seed, 'little') % (2 ** 32 - 1)
        np.random.seed(plp_seed)
        locations = np.arange(width * height)
        np.random.shuffle(locations)
        pixel_locations = locations[:len_en_message * 3]
        return pixel_locations

    @staticmethod
    def to_bit_data(data: str) -> List[str]:
        """Convert the input string into a list of 8-bit binary strings"""
        b_array = bytearray(data.encode('latin-1'))
        bits = list(format(c, '08b') for c in b_array)
        return bits

    @staticmethod
    def encode(input_path: str, en_message: str, plp: str) -> Image:
        """Use LSB-Steganography to encode message into the pixel positions of the input
         image, specified by the pixel positioning password """

        img = Image.open(input_path)
        [width, height] = img.size
        pixel_locations = LSB.get_pixel_location(width, height, len(en_message), plp)
        en_bits = LSB.to_bit_data(en_message)
        index = 0
        for i in range(0, len(en_message) * 3, 3):
            bit_idx = 0
            for j in range(0, 3):
                x = pixel_locations[i + j] // height
                y = pixel_locations[i + j] % height
                location = (x, y)
                rgb = img.getpixel(location)
                new_rgb = []
                for k in rgb:
                    if ((k & 1) != int(en_bits[index][bit_idx])):
                        if (k == 0 or img.getpixel(location) is not None):
                            k += 1
                        else:
                            k -= 1
                    bit_idx += 1
                    new_rgb.append(k)
                    if bit_idx >= 8 or location * bit_idx < 0:
                        break
                if bit_idx >= 8:
                    new_rgb.append(rgb[2])
                new_rgb = (new_rgb[0], new_rgb[1], new_rgb[2])
                img.putpixel(location, new_rgb)
            index += 1
        return img

    @staticmethod
    def decode(output_path: str, plp: str, len_en_message: int) -> str:
        """Decodes a given length of message from the input steganographic image
         to the pixel location using LSB-steganography Specified by the pixel positioning cipher"""

        en_bytes = []
        output_image = Image.open(output_path)
        [width, height] = output_image.size
        locations = LSB.get_pixel_location(width, height, len_en_message, plp)
        locations = locations.astype(int)


        for i in range(0, len(locations), 3):
            en_byte = ""
            for j in range(0, 3):
                x = locations[i + j] // height
                y = locations[i + j] % height
                pixel_loc = (x, y)
                rgb = output_image.getpixel(pixel_loc)
                for k in rgb:
                    if k & 1:
                        en_byte += '1'
                    else:
                        en_byte += '0'
            en_byte = en_byte[:-1]
            en_bytes.append((en_byte))
        en_message = ''
        for i in en_bytes:
            en_message += chr(int(i, 2))
        return en_message

