import unittest
from tkinter import Tk, Text
from PIL import Image
from io import BytesIO
from final_code import Stegno 

class TestStegnoTool(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.final_code = Stegno()

    def test_encode_and_decode(self):
        test_message = "Hello, this is a test message for steganography."

        encoded_image_file = self.encode_test_image(test_message)

        decoded_message = self.decode_test_image(encoded_image_file)

        self.assertEqual(test_message, decoded_message)

    def encode_test_image(self, message):
        test_image = Image.new('RGB', (200, 200), color='white')

        self.final_code.encode_enc(test_image, message)

        image_file = BytesIO()
        test_image.save(image_file, format='PNG')

        return image_file

    def decode_test_image(self, image_file):
        test_image = Image.open(image_file)

        decoded_message = self.final_code.decode(test_image)

        return decoded_message

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
