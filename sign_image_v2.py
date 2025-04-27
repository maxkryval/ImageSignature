"""Script with function to sign image that is saved to images directory."""
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


def sign_image_tail(image_path, output_path):
    """
    Function that signs image by putting key in the end of file itself.
    :param image_path:
    :param output_path:
    :return: signed image saved into images directory
    """
    # loading private key
    with open("keys/private_key.pem", "rb") as key_file:
        private_key = RSA.import_key(key_file.read())

    # reading and hashing image
    with open(image_path, "rb") as img_file:
        image_data = img_file.read()
    hash_obj = SHA256.new(image_data)

    # signing
    signature = pkcs1_15.new(private_key).sign(hash_obj)

    # writing image and signature
    with open(output_path, "wb") as out_file:
        out_file.write(image_data)
        out_file.write(b'SIGNATURE_START')
        out_file.write(signature)


if __name__ == "__main__":
    sign_image_tail("images/original_image.png", "images/signed_image_v2.png")
