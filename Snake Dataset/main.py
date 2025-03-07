import json
from pyinaturalist import Observation, enable_logging, get_observations
from rich import print

enable_logging()


def save_to_JSON(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")


def fetch_observations(taxon_name):
    response = get_observations(
        taxon_name=taxon_name,
        photos=True,
        page=2,
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


taxon_name = "Eranthis hyemalis"
observations = fetch_observations(taxon_name)
photo_urls = fetch_photo_urls(observations)

filename = f"{taxon_name.lower().replace(' ', '_')}_observations.json"
save_to_JSON(photo_urls, filename)
