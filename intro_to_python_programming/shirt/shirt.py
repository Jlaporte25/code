import sys
import os
from PIL import Image
from PIL import ImageOps


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: Python3 shirt.py <input_path.jpg> <output_path.jpg>")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()
    valid_extensions = [".jpg", ".jpeg", ".png"]

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid file format. Use .jpg, .jpeg, or .png.")

    if input_ext != output_ext:
        sys.exit("Input and output file extensions do not match.")

    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Shirt image 'shirt.png' not found.")
    except Exception as e:
        sys.exit(f"Error opening shirt image: {e}")

    try:
        photo = Image.open(input_path)
    except FileNotFoundError:
        sys.exit(f"Input file '{input_path}' does not exist.")
    except Exception as e:
        sys.exit(f"Error opening input file: {e}")

    shirt_size = shirt.size
    cropped_photo = ImageOps.fit(image=photo, size=shirt_size)

    cropped_photo.paste(shirt, shirt)

    try:
        cropped_photo.save(output_path)
    except Exception as e:
        sys.exit(f"Error saving output file: {e}")


if __name__ == "__main__":
    main()
