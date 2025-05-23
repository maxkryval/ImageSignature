# ImageSignature

## Motivation
Digital signature could be important in numerous areas, some of which are:
- Secure software distribution
- Authentication of legal and financial documents
- Verification of digital art and media ownership
- Protection of sensitive communications<br>
## Method 1
**Description:** The RSA signature is embedded as additional metadata inside the PNG file.<br>
**Disadvantage:** signature can be found via photo editor application that allows viewing image metadata.<br><br>

## Method 2
**Description:** The RSA signature is appended after the formal end of the PNG file (IEND chunk).<br>
**Advantage:** signature can be found through either decoding image file through code or special text editors.<br><br>

## Usage
1. Clone the repository `git clone https://github.com/maxkryval/ImageSignature.git`.
2. Navigate to the directory with the cloned project.
Perform commands below in your local terminal in root directory of the project (`ImageSignature`)
3. Install `requirements.txt` `pip install requirements.txt` (or `pip3`, depending on your specifications).
4. Use existing keys or generate new ones by `python generate_keys.py` (or `python3`, make sure to have `keys` directory present).
5. Use existing signed images or sign yourself. Make sure `images` directory is present and original image is named `original_image.png`.
   Use `python sign_image_v1.py` for described Method 1, `python sign_image_v2.py` for described Method 2.
6. Verify signature by running `python verify_signature_v1.py` or `python verify_signature_v2.py`.
