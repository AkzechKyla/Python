import json
import os
from pyinaturalist import Observation, enable_logging, get_observations
from rich import print

enable_logging()


def save_to_JSON(data, filename):
    existing_data = []

    # Check if the file exists and is not empty
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r", encoding="utf-8") as file:
            existing_data = json.load(file)

    # Append new data, avoiding duplicates
    for url in data:
        if url not in existing_data:
            existing_data.append(url)
        else:
            print(f"URL already exists: {url}")

    # Write the updated list back to the file
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4)

    print(f"Data successfully added to {filename}")


def fetch_observations(taxon_name):
    response = get_observations(
        taxon_name=taxon_name,
        photos=True,
        page=1,
        per_page=100,
    )

    return Observation.from_json_list(response)


def modify_image_size(photo_url, former_size, new_size):
    """
    square → Small square thumbnail (75x75 px)
    small → Small size (240px)
    medium → Medium size (500px)
    large → Large size (1024px)
    original → Full-size image
    """
    return photo_url.replace(former_size, new_size)


def fetch_photo_urls(observations):
    photo_urls = []
    for obs in observations:
        for photo in obs.photos:
            modified_url = modify_image_size(photo.url, "square", "original")
            photo_urls.append(modified_url)
    return photo_urls


if __name__ == "__main__":
    taxon_name = "Passer montanus"
    observations = fetch_observations(taxon_name)
    photo_urls = fetch_photo_urls(observations)

    print(f"Number of observations: {len(observations)}")
    print(f"Number of photo URLs: {len(photo_urls)}")

    filename = f"{taxon_name.lower().replace(' ', '_')}_photo_urls.json"
    save_to_JSON(photo_urls, filename)
