import pandas as pd

def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file, print its dimensions, and return it as a pandas DataFrame.

    Args:
    path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded dataset, or None if there was an error.
    """
    try:
        df = pd.read_csv(path)

        rows, cols = df.shape

        print(f"Loading dataset of dimensions ({rows}, {cols})")

        return df
    
    except FileNotFoundError:
        print(f"Error: File not found at path: {path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {path} is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Unable to parse the file at {path}. Make sure it's a valid CSV.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    dataset = load("life_expectancy_years.csv")
    if dataset is not None:
        print(dataset.head())
