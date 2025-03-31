import os
import h5py
import pandas as pd
import numpy as np

def read_h5_files(directory):
    data_frames = []
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".h5"):
                file_path = os.path.join(subdir, file)
                with h5py.File(file_path, 'r') as hdf_file:
                    # Assume you know the structure and data you need
                    data = hdf_file['metadata/songs'][:]
                    df = pd.DataFrame(data)
                    data_frames.append(df)
    return data_frames

def fill_missing_values(df):
    # Handle numeric columns
    for col in df.select_dtypes(include=[np.number]).columns:
        if pd.isnull(df[col]).any():
            df[col] = df[col].fillna(df[col].median())  # Direct assignment

    # Handle non-numeric columns
    for col in df.select_dtypes(exclude=[np.number]).columns:
        if pd.isnull(df[col]).any():
            df[col] = df[col].fillna('Unknown')  # Direct assignment

    return df

def convert_byte_strings(df):
    # Convert columns that are of byte string type to regular string type
    for col in df.columns:
        if df[col].dtype == 'O':  # Object type, potentially holding byte strings
            try:
                df[col] = df[col].str.decode('utf-8')
            except (AttributeError, UnicodeDecodeError):
                # Handles cases where conversion isn't applicable or fails
                df[col] = df[col].astype(str)
    return df

def main():
    directory = r"C:\Users\cvhre\OneDrive\Escritorio\BigDataMusicProject\millionsongsubset"
    data_frames = read_h5_files(directory)
    big_df = pd.concat(data_frames, ignore_index=True)
    
    # Convert byte strings to strings
    big_df = convert_byte_strings(big_df)

    # Clean the DataFrame
    big_df = fill_missing_values(big_df)

    # Save to HDF5 file format
    big_df.to_hdf(path_or_buf='cleaned_data.h5', key='cleaned_music_data', format='table', data_columns=True)
    # Alternatively, save to CSV
    big_df.to_csv('cleaned_music_data.csv', index=False)

if __name__ == '__main__':
    main()