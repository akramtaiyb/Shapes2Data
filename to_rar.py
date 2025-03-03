import os
import zipfile

def zip_images(directory, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.png'):
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory))

if __name__ == "__main__":
    images_directory = os.path.join(os.path.dirname(__file__), 'images')
    output_zip_path = os.path.join(os.path.dirname(__file__), 'shapes2data.rar')
    zip_images(images_directory, output_zip_path)