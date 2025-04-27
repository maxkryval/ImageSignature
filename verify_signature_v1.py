"""Script that verifies signature of signed image."""
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from PIL import Image


def verify_signature(image_path):
    """
    Function to verifies signature put into PNG metadata.

    :param image_path: path to signed image
    :return: confirmation of success/fail of signature check
    """
    with open("keys/public_key.pem", "rb") as key_file:
        public_key = RSA.import_key(key_file.read())

    # loading image
    image = Image.open(image_path)

    # getting signature from PNG metadata
    signature_hex = image.info.get('Signature', None)
    if signature_hex is None:
        print("No signature found.")
        return False

    signature = bytes.fromhex(signature_hex)

    # hashing image
    image_bytes = image.tobytes()
    hash_obj = SHA256.new(image_bytes)

    # checking signature
    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        print("Valid signature.")
        return True
    except (ValueError, TypeError):
        print("Non-valid signature.")
        return False


if __name__ == "__main__":
    verify_signature("images/signed_image_v1.png")
