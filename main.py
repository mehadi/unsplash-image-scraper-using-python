from httpx import get
from selectolax.parser import HTMLParser
import os


class ImageScraper:
    def __init__(self, search_term, img_dir="images"):
        self.search_term = search_term
        self.img_dir = img_dir
        self.image_nodes = []
        self.img_urls = []

    def fetch_image_tags(self):
        """Fetch image tags from Unsplash based on the provided search term."""
        if not self.search_term:
            raise Exception("No search term provided")

        url = f"https://unsplash.com/s/photos/{self.search_term}"
        response = get(url)

        if response.status_code != 200:
            raise Exception(f"Error getting response. Status code: {response.status_code}")

        tree = HTMLParser(response.text)
        self.image_nodes = tree.css("figure a img")
        self.img_urls = [i.attrs['src'] for i in self.image_nodes]

    def filter_images(self, keywords):
        """Filter out images based on specified keywords."""
        return [url for url in self.img_urls if not self.img_filter_out(url, keywords)]

    @staticmethod
    def img_filter_out(url, keywords):
        """Check if any keyword is present in the image URL."""
        return any(x in url for x in keywords)

    @staticmethod
    def get_high_res_img_url(img_urls):
        """Extract high-resolution image URLs from the original URLs."""
        return [url.split("?")[0] for url in img_urls]

    def save_images(self, img_urls, tag=""):
        """Download and save images to the specified directory."""
        for img_url in img_urls:
            print(f"Downloading [{img_url}]...")
            filename = os.path.basename(img_url.split("?")[0])
            filepath = os.path.join(self.img_dir, f"{tag}_{filename}.jpeg")

            if os.path.exists(filepath):
                print(f"Skipping {filename} as it already exists.")
                continue

            response = get(img_url)

            if not os.path.exists(self.img_dir):
                os.makedirs(self.img_dir)

            with open(filepath, "wb") as f:
                f.write(response.content)
                print(f"Saved {filename}, with size {round(len(response.content) / 1024 / 1024, 2)} MB.")


if __name__ == '__main__':
    search_term = "python"
    try:
        downloader = ImageScraper(search_term)
        downloader.fetch_image_tags()
        relevant_urls = downloader.filter_images(['premium', 'profile', 'plus', 'data:image/bmp'])
        high_res_img_urls = ImageScraper.get_high_res_img_url(relevant_urls)
        downloader.save_images(high_res_img_urls, search_term)
    except Exception as e:
        print(e)
