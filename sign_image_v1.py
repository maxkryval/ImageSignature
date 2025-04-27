"""Script with function to sign image that is saved to images directory."""
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from PIL import Image, PngImagePlugin


def sign_image(image_path, output_path):
    """
    Function that signs image and saves into images directory with signature.
    Saving signature into PNG metadata.

    :param image_path: path original of original image
    :param output_path: path of output signed image
    :return: saving signed original image into signed image separate file
    """
    # loading private key
    with open("keys/private_key.pem", "rb") as key_file:
        private_key = RSA.import_key(key_file.read())

    # loading image and converting to numerical format
    image = Image.open(image_path)
    image_bytes = image.tobytes()

    # hashing image
    hash_obj = SHA256.new(image_bytes)

    # creating signature
    signature = pkcs1_15.new(private_key).sign(hash_obj)

    # writing signature into PNG metadata
    meta = PngImagePlugin.PngInfo()
    meta.add_text("Signature", signature.hex())

    image.save(output_path, "PNG", pnginfo=meta)


if __name__ == "__main__":
    sign_image("images/original_image.png", "images/signed_image_v1.png")
