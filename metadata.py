import os
import h5py

def extract_limited_metadata(directory, max_entries=10):
    count = 0  # Initialize a counter to keep track of how many entries have been processed
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".h5") and count < max_entries:  # Check if the maximum entries limit has been reached
                file_path = os.path.join(subdir, file)
                with h5py.File(file_path, 'r') as hdf_file:
                    # Access the metadata group
                    metadata = hdf_file['metadata']
                    # Access specific datasets within the metadata group
                    artist_name = metadata['songs']['artist_name'][0].decode('utf-8')  # Decoding from bytes to string
                    song_title = metadata['songs']['title'][0].decode('utf-8')
                    #release_year = metadata['songs']['year'][0]  # Year is typically stored as an integer
                    
                    # Print the extracted information
                    print(f"File: {file_path}")
                    print(f"Artist: {artist_name}")
                    print(f"Title: {song_title}")
                    #print(f"Year: {release_year}")
                    
                    count += 1  # Increment the counter after processing each file
                if count >= max_entries:
                    break  # Break the inner loop if the maximum count is reached
        if count >= max_entries:
            break  # Break the outer loop if the maximum count is reached

# Set the top-level directory where your HDF5 files start
directory = r"C:\Users\cvhre\OneDrive\Escritorio\BigDataMusicProject\millionsongsubset"
extract_limited_metadata(directory, 10)  # Change 10 to any number you want to limit the output to