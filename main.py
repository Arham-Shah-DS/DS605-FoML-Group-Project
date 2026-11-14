from pathlib import Path

def main():
    print("Project structure is ready.")

    data_path = Path("data/raw/Soil‑Weather Multivariate Crop Disease Dataset.csv")

    if data_path.exists():
        print("Dataset found.")
    else:
        print("Next: place the dataset in data/raw/")

if __name__ == "__main__":
    main()
