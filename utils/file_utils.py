from typing import Any, Optional
import requests
from config import ROOT
import pandas as pd
from pathlib import Path

IMG_PATH = ROOT / 'img'
CSV_PATH = ROOT / 'csv'


def download_hero_img(hero_name: str, img_url: str) -> Optional[Path]:
    """
    Download an image from the given URL and save it with the specified name.

    Parameters:
        hero_name (str): The name to be used for saving the image.
        img_url (str): The URL of the image to be downloaded.

    Returns:
        Optional[Path]: The path where the image is saved if successful, else None.
    """
    IMG_PATH.mkdir(exist_ok=True)
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(IMG_PATH / f'{hero_name}.png', 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded and saved at {IMG_PATH}")
        return IMG_PATH / f'{hero_name}.png'
    else:
        print(f"Failed to download image from {img_url}")
        return None


def write_hero_info_to_csv(hero_info: Any, csv_name: str) -> None:
    """
    Write hero information to a CSV file.

    Parameters:
        hero_info (Any): The hero information to be written to the CSV file.
        csv_name (str): The name of the CSV file.

    Returns:
        None
    """
    CSV_PATH.mkdir(exist_ok=True)
    csv_file_path = CSV_PATH / f'{csv_name}.csv'
    df = pd.json_normalize(hero_info)
    if csv_file_path.exists():
        df.to_csv(csv_file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_file_path, index=False)
