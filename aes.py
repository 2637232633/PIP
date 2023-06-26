import fire
import pyaes
import binascii
import pbkdf2

class AES:

    PasswordSalt: bytes = b'\\`\x03\xc0\xd6\xf0\xd4z\xb6p\xe8O\xdd\xa8\xdaB'
    iv: int = 81758493089852126930117852331904660891236515198964819874563125848546201498563

    @staticmethod
    def encrypt(message: str, pwd: str) -> str:
        """Encrypt the input information with AES"""

        key = pbkdf2.PBKDF2(pwd, AES.PasswordSalt).read(32)
        aes_algor = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(AES.iv))
        en_byte = aes_algor.encrypt(message)
        return binascii.hexlify(en_byte).decode('utf-8')

    @staticmethod
    def decrypt(encrypted_message: str, pwd: str) -> str:
        """Decrypt messages encrypted by AES"""

        en_byte = binascii.unhexlify(bytes(encrypted_message, 'utf-8'))
        key = pbkdf2.PBKDF2(pwd, AES.PasswordSalt).read(32)
        aes_algor = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(AES.iv))
        de_byte = aes_algor.decrypt(en_byte)
        return de_byte.decode('utf-8')






