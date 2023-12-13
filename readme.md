# Unsplash Image Scraper using Python

This Python script provides a simple way to download and filter images from Unsplash based on a specified search term. The script utilizes the `httpx` library for making HTTP requests and `selectolax` for parsing HTML.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/mehadi/unsplash-image-scraper-using-python.git
    ```

2. Install the required dependencies:

    ```bash
    pip install httpx selectolax
    ```

3. Run the script:

    ```bash
    python main.py
    ```

Make sure to modify the `search_term` variable in the script to specify the desired search term.

## Features

- **Fetch Image Tags:** The script fetches image tags from Unsplash based on the provided search term.
- **Filter Images:** You can filter out images based on specified keywords to exclude certain types of images.
- **Download and Save:** The script downloads and saves images to a specified directory, skipping those that already exist.
- **High-Resolution Images:** Extracts high-resolution image URLs from the original URLs.

## Configuration

- The default download directory is set to "images." You can change this by modifying the `img_dir` parameter in the `ImageScraper` class.
- Specify your search term by changing the value of the `search_term` variable in the script.
- Add or remove keywords in the `filter_images` method to customize the image filtering process.


Feel free to customize the script according to your needs and contribute to its improvement. If you encounter any issues or have suggestions, please create an issue or pull request.

Happy image downloading! 📷