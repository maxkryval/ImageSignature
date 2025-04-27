"""Script defining function that generates keys and providing execution capabilities."""
from Crypto.PublicKey import RSA


def generate_keys():
    """
    Function generating public and private keys for
    future image signing and signature verifications processes.
    :return: saved private_key.pem and public_key.pem files into keys directory
    """
    key = RSA.generate(4096)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("keys/private_key.pem", "wb") as private_file:
        private_file.write(private_key)

    with open("keys/public_key.pem", "wb") as public_file:
        public_file.write(public_key)


if __name__ == "__main__":
    generate_keys()
