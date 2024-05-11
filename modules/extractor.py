# folder_reader.py
import os
import logging
from scrapper import scrapData

# Set up logging to print to the console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def readFolder(folder, db_name, collection_name):
    try:
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                words_list, title, total_reviews = scrapData(file_path, db_name, collection_name)
                logger.info(f"Processed file: {file_path}")
                logger.info(f"Title: {title}, Total Reviews: {total_reviews}, Words Count: {len(words_list)}")
    except Exception as e:
        logger.error(f"Error while reading folder {folder}: {e}")

if __name__ == "__main__":
    # This block runs only when this script is executed directly, not when imported as a module
    readFolder("../data", "your_db_name", "your_collection_name")
