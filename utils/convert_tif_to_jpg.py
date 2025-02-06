from PIL import Image
import os


def convert_tif_to_jpg(directory):
    """
    Converts all TIFF images in the specified directory to JPEG format.

    Parameters:
    - directory: str, the path to the directory containing TIFF images.
    """
    # Ensure the output directory exists
    output_directory = os.path.join(directory, "converted_to_jpg")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate over all TIFF files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".tif") or filename.endswith(".tiff"):
            # Construct the full file path
            file_path = os.path.join(directory, filename)

            # Open the image
            with Image.open(file_path) as img:
                # Convert and save the image in JPEG format
                output_filename = filename.replace('.tif', '.jpg').replace('.tiff', '.jpg')
                output_path = os.path.join(output_directory, output_filename)

                # Convert image to RGB if it is not already to avoid issues saving as JPEG
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                img.save(output_path, "JPEG")
                print(f"Converted {filename} to JPEG format.")


if __name__ == "__main__":
    directory = "PRE_splitted"
    convert_tif_to_jpg(directory)
