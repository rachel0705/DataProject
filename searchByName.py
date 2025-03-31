import os
import h5py

def search_by_artist_or_song(directory, search_artist=None, search_song=None):
    found = 0  # Counter for found entries
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".h5"):
                file_path = os.path.join(subdir, file)
                with h5py.File(file_path, 'r') as hdf_file:
                    # Access the metadata group
                    metadata = hdf_file['metadata']
                    # Access specific datasets within the metadata group
                    artist_name = metadata['songs']['artist_name'][0].decode('utf-8')  # Decoding from bytes to string
                    song_title = metadata['songs']['title'][0].decode('utf-8')
                    #release_year = metadata['songs']['year'][0]  # Year is typically stored as an integer

                    # Check if the current song matches the search criteria
                    if (search_artist and search_artist.lower() in artist_name.lower()) or (search_song and search_song.lower() in song_title.lower()):
                        print(f"File: {file_path}")
                        print(f"Artist: {artist_name}")
                        print(f"Title: {song_title}")
                        #print(f"Year: {release_year}")
                        found += 1  # Increment the found counter

                    # Optional: break after a certain number of results
                    if found >= 10:  # You can change this number to limit results
                        return  # Exit the function after finding enough matches

# Set the top-level directory where your HDF5 files start
directory = r"C:\Users\cvhre\OneDrive\Escritorio\BigDataMusicProject\millionsongsubset"
search_by_artist_or_song(directory, search_artist="mendes")  # Change to the artist or song you're looking for