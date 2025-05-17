import requests
import os
import zipfile
import logging

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

download_dir = "downloads"


def processFile(downlaod_dir, uri):
    uri_split = uri.split("/")
    filename = uri_split[-1]
    response = requests.get(uri)
    dest_file = f"{download_dir}/{filename}"
    if response.status_code == 200:
        logging.info(f"Downloading {filename} to {dest_file}")
        with open(dest_file, "wb") as file:
            file.write(response.content)
        logging.info(f"Successfully downloaded the file: {dest_file}")

        logging.info(f"Unzipping: {dest_file}")
        # Each file is a `zip`, extract the `csv` from the `zip` and delete the `zip` file.
        with zipfile.ZipFile(dest_file, 'r') as zObject:
            zObject.extractall(path=f"{download_dir}")
        logging.info(f"Successfully extracted the file: {dest_file}")

        logging.info(f"Removing zip file: {dest_file}")
        os.remove(f"{dest_file}")
        logging.info(f"Successfully removed the file: {dest_file}")
    else:
        logging.warning(f"Failed to download the file: {dest_file}. Status code: {response.status_code}")


def main():
    # your code here
    logging.basicConfig(level=logging.INFO)
    # create the directory `downloads` if it doesn't exist
    logging.info("Creating download directory {download_dir}")
    os.makedirs(download_dir, exist_ok=True)
    # download the files one by one.
    for uri in download_uris:
        processFile(download_dir, uri)
    logging.info("All done!")

if __name__ == "__main__":
    main()
