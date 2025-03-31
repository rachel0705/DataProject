import os
import h5py

def find_h5_files(directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".h5"):
                file_path = os.path.join(subdir, file)
                with h5py.File(file_path, 'r') as hdf_file:
                    print(f"File: {file_path}")
                    print("Keys: %s" % list(hdf_file.keys()))

# Set the top-level directory where your HDF5 files start
directory = r"C:\Users\cvhre\OneDrive\Escritorio\BigDataMusicProject\millionsongsubset"
find_h5_files(directory)
#just a test