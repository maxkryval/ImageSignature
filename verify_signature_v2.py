"""Script that verifies signature of signed image."""
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


def verify_signature_tail(image_path):
    """
    Function that verifies image signature.

    :param image_path: path to the signed image
    :return: confirmation of success/fail of image signature finding
    """
    with open("keys/public_key.pem", "rb") as key_file:
        public_key = RSA.import_key(key_file.read())

    with open(image_path, "rb") as img_file:
        data = img_file.read()

    # looking for mark in the file
    marker = b'SIGNATURE_START'
    marker_index = data.find(marker)

    if marker_index == -1:
        print("❌ Підпис не знайдено.")
        return False

    # separating signature symbols
    image_data = data[:marker_index]
    signature = data[marker_index + len(marker):]

    # check
    hash_obj = SHA256.new(image_data)

    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        print("Valid signature.")
        return True
    except (ValueError, TypeError):
        print("Non-valid signature.")
        return False


if __name__ == "__main__":
    verify_signature_tail("images/signed_image_v2.png")
