import requests
import os
from concurrent.futures import ThreadPoolExecutor

# Base URL for the images
base_url = "https://starzone.ragalahari.com/april2021/hd/anjali-maguva-nee-vijayam-event/anjali-maguva-nee-vijayam-event{}.jpg"

# Range of image numbers you want to download
start_number = 1  # Starting number
end_number = 112  # Ending number

# Specify the directory where you want to save the images
download_directory = "images/"

# Create the directory if it doesn't exist
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Function to download an image
def download_image(number):
    image_url = base_url.format(number)
    response = requests.get(image_url)
    if response.status_code == 200:
        filename = f"anjali_{number}.jpg"
        with open(os.path.join(download_directory, filename), "wb") as file:
            file.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download image{number}.jpg")

# Use ThreadPoolExecutor to run the downloads concurrently
with ThreadPoolExecutor(max_workers=60) as executor:  # Adjust max_workers as needed
    for number in range(start_number, end_number + 1):
        executor.submit(download_image, number)

print("Download complete!")
