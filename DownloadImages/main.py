import os
import json
import matplotlib.pyplot as plt
import numpy as np


def load_snake_data(directory_path):
    """Load image source counts for each snake species from JSON files."""
    counts = {}

    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            file_path = os.path.join(directory_path, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            snake_species = filename.replace("_photo_urls.json", "")

            # Count occurrences within each file
            static_count = sum("static.inaturalist" in url for url in data)
            open_data_count = sum("inaturalist-open-data" in url for url in data)

            counts[snake_species] = (static_count, open_data_count)

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

    fig, ax = plt.subplots(figsize=(12, 6))
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
    ax.set_xticks(x)
    ax.set_xticklabels(species, rotation=45, ha="right")
    ax.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    directory_path = "../SnakeDataCollection/"
    counts = load_snake_data(directory_path)
    plot_snake_data(counts)
