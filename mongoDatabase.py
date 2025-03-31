from pymongo import MongoClient
import pandas as pd
from dataCleansing import read_h5_files, fill_missing_values

def main():
    directory = r"C:\Users\cvhre\OneDrive\Escritorio\BigDataMusicProject\millionsongsubset"
    data_frames = read_h5_files(directory)
    big_df = pd.concat(data_frames, ignore_index=True)
    
    big_df = fill_missing_values(big_df)

    client = MongoClient('mongodb://localhost:27017/')
    db = client['music_data']
    collection = db['songs']

    data_dict = big_df.to_dict("records")

    # Use upsert to avoid duplicating data
    for record in data_dict:
        query = {'song_id': record['song_id']} 
        update = {'$set': record}
        collection.update_one(query, update, upsert=True)

    print("Data has been successfully inserted or updated in MongoDB.")

if __name__ == '__main__':
    main()