import pandas as pd
import os
from sklearn.model_selection import train_test_split


def read_and_concat_csv(data_directory, test_data_size=0.3, random_init_seed=42):
    """
    Lee todos los archivos CSV de un directorio, los concatena y agrega una columna 'ciudad'
    basada en el nombre del archivo.

    Args:
        data_directory (str): Ruta del directorio que contiene los archivos CSV

    Returns:
        pd.DataFrame: DataFrame concatenado con la nueva columna 'ciudad'
    """
    # Leer todos los archivos CSV en el directorio
    all_files = [
        os.path.join(data_directory, f)
        for f in os.listdir(data_directory)
        if f.endswith(".csv")
    ]

    # Leer cada archivo CSV
    dfs = []
    for file in all_files:
        df = pd.read_csv(file)
        df.insert(1, "city", file.split("/")[-1].split(".csv")[0])
        # añadimos el dataframe a la lista
        dfs.append(df)

    # Concatenar todos los DataFrames
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df = combined_df.sample(frac=1)
    train_df, test_df = train_test_split(
        combined_df, test_size=test_data_size, random_state=random_init_seed
    )

    return combined_df, train_df, test_df
