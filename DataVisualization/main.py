import os
import json
import matplotlib.pyplot as plt
import numpy as np


def load_snake_data(directory_path):
    """Load raw JSON data for each snake species from files."""
    data_dict = {}

    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            file_path = os.path.join(directory_path, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            snake_species = filename.replace("_photo_urls.json", "")
            data_dict[snake_species] = data

    return data_dict


def count_image_sources_per_species(data_dict):
    """Count occurrences of 'static.inaturalist' and 'inaturalist-open-data' per snake species."""
    counts = {}

    for species, urls in data_dict.items():
        static_count = sum("static.inaturalist" in url for url in urls)
        open_data_count = sum("inaturalist-open-data" in url for url in urls)
        counts[species] = (static_count, open_data_count)

    return counts


def plot_snake_data(counts):
    """Plot a grouped bar chart for static and open-data image counts per snake species."""
    if not counts:
        print("No data available to plot.")
        return

    # Extracting data for plotting
    species = list(counts.keys())
    static_counts = [counts[sp][0] for sp in species]
    open_data_counts = [counts[sp][1] for sp in species]

    # Plot settings
    x = np.arange(len(species))  # X-axis positions
    width = 0.4  # Bar width

    fig, ax = plt.subplots(figsize=(max(12, len(species) * 0.2), 6))
    ax.bar(
        x - width / 2, static_counts, width, label="static.inaturalist", color="blue"
    )
    ax.bar(
        x + width / 2,
        open_data_counts,
        width,
        label="inaturalist-open-data",
        color="orange",
    )

    # Labels and Title
    ax.set_xlabel("Snake Species")
    ax.set_ylabel("Count")
    ax.set_title("Count of Snake Images by Data Source")

    # Adjust x-ticks for readability
    ax.set_xticks(x)
    ax.set_xticklabels(species, rotation=45, ha="right", fontsize=8)

    ax.legend()

    # Add more space at the bottom for better readability
    plt.subplots_adjust(bottom=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    directory_path = "../SnakeDataCollection/"
    raw_data = load_snake_data(directory_path)
    counts = count_image_sources_per_species(raw_data)
    plot_snake_data(counts)
