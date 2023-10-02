import os

# Directory where your image files are located
image_directory = '/home/aadhithbala/Datasets/SaiPallavi'

# List all files in the directory
image_files = os.listdir(image_directory)

# Define a counter
counter = 1

# Loop through the image files and rename them
for file_name in image_files:
    if file_name.endswith('.jpg'):
        # Create the new file name
        new_name = f'sai_pallavi_{counter}.jpg'
        
        # Build the full paths to the old and new file names
        old_path = os.path.join(image_directory, file_name)
        new_path = os.path.join(image_directory, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        # Increment the counter
        counter += 1

print("Renaming complete.")
