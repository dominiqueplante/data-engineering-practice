import requests
import os
import zipfile

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
        with open(dest_file, "wb") as file:
            file.write(response.content)
        print(f"Successfully downloaded the file: {dest_file}")
        print(f"Unzipping: {dest_file}")
        # Each file is a `zip`, extract the `csv` from the `zip` and delete the `zip` file.
        with zipfile.ZipFile(dest_file, 'r') as zObject:
            zObject.extractall(path=f"{download_dir}")
        print(f"Removing zip file: {dest_file}")
        os.remove(f"{dest_file}")
    else:
        print(f"Failed to download file {dest_file}. Status code: {response.status_code}")

def main():
    # your code here
    # create the directory `downloads` if it doesn't exist
    os.makedirs(download_dir, exist_ok=True)
    # download the files one by one.
    for uri in download_uris:
        processFile(download_dir, uri)
    print("Done!")

if __name__ == "__main__":
    main()
