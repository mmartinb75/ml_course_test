import pandas as pd
import os
from typing import List


def read_and_concat_csv(data_directory: str) -> pd.DataFrame:
    """
    Reads and concatenates all CSV files from a directory, adding a 'city' column
    based on the filename.

    Args:
        data_directory: Path to the directory containing CSV files.

    Returns:
        pd.DataFrame: Concatenated DataFrame with randomized row order, containing
        all data from input CSVs with an additional 'city' column.

    Example:
        >>> df = read_and_concat_csv("path/to/csv/directory")
        >>> print(df.columns)
        ['original_columns', 'city', ...]
    """
    # Get paths of all CSV files in directory
    csv_files: List[str] = [
        os.path.join(data_directory, f)
        for f in os.listdir(data_directory)
        if f.lower().endswith(".csv")
    ]

    if not csv_files:
        raise ValueError(f"No CSV files found in directory: {data_directory}")

    # Read and process each CSV file
    dataframes: List[pd.DataFrame] = []
    for file_path in csv_files:
        df = pd.read_csv(file_path)
        city_name = os.path.splitext(os.path.basename(file_path))[0]
        df.insert(1, "city", city_name)
        dataframes.append(df)

    # Concatenate all DataFrames and randomize row order
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df.sample(frac=1, random_state=42)
