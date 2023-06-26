# PIP
Steganography is the art of hiding secret messages inside another innocent-looking message. It has been widely used for secret communication in various fields, such as military, politics, and business. One of the traditional steganography techniques, the LSB-based steganography, hides the secret message by replacing the least significant bit of a pixel in an image with the secret message bit. However, the attackers can use statistical analysis or visual inspection to detect the presence of hidden messages, which leads to the exposure of secret messages.

To overcome these limitations and enhance the security of steganography, it is necessary to implement more advanced cryptographic protocols on the LSB based steganography. Therefore, this report proposes and implement an application of combination of LSB based steganography, AES (Advanced Encryption Standard), and Pixel-location Image Password (PLP).

Proposed Solution:

To implement the proposed security application, we will use a combination of LSB steganography, AES encryption, and PIP to ensure the secure transmission of hidden messages within images.

Pixel-location Image Password (PLP): generate a sequence of index that is unique to a specific image and the password and can be generated randomly by the sender. During decoding, PLP acts as a key. The values in the generated Location Sequence represent the coordinates of the pixels in the image, with every three coordinates used to store one character. Therefore, this technique can store the Encoded Message in a shuffled order within the image, and during decryption, the Location Sequence can be obtained in reverse order using PIP to identify the coordinate groups corresponding to each character.

The process will involve the following steps:

Encryption: 
The plaintext message will be encrypted using the AES encryption algorithm with a symmetric key which is generated based on the password entered by the user. Afterwards, the system generates a Pixel Location Password randomly, and then uses the information from the Original Image and the Pixel Location Password to create a random seed, which is used to generate a Location Sequence. Finally, the Encoded Message is hidden in the Original Image using LSB techniques based on the Location Sequence, resulting in the Stego Image.

 
Decryption: 
To retrieve the hidden message from the image, frstly, the Location Sequence is generated using PIP based on the Stego Image and the Pixel Location Sequence, and then the Encoded Message hidden in the image is extracted using LSB techniques according to the Location Sequence. Finally, the encrypted information is decrypted into plaintext using a password through ASE.


 


Novelty:

The proposed security application is novel in several ways: The application combines the use of LSB steganography, AES encryption, and PLP create a more secure and robust method of transmitting hidden messages within images. This technique offers an advantage over other methods because it prevents attackers from accessing the data sequentially. By scattering the location of the data across random pixel locations and using AES encryption, the attacker will be unable to easily access the information. Overall, the proposed security application provides a novel and secure method for transmitting hidden messages within images that can be used in various applications, including secure communication, information hiding, and data protection.

