import unittest
import pandas as pd
import numpy as np

from dataCleansing import fill_missing_values, convert_byte_strings
from searchByName import search_by_artist_or_song

class TestMusicProject(unittest.TestCase):

    def test_fill_missing_values(self):
        df = pd.DataFrame({
            'genre': ['pop', None, 'rock'],
            'popularity': [10, None, 30]
        })

        cleaned_df = fill_missing_values(df)

        self.assertFalse(cleaned_df.isnull().values.any())
        self.assertIn('Unknown', cleaned_df['genre'].values)

    def test_convert_byte_strings(self):
        df = pd.DataFrame({
            'artist_name': [b'Shawn Mendes', b'Taylor Swift']
        })

        converted_df = convert_byte_strings(df)
        self.assertTrue(all(isinstance(x, str) for x in converted_df['artist_name']))

    def test_search_by_artist(self):
        # Mock a version of the function using a small sample
        # Since the actual function reads files, you'd ideally use mock or test small dummy data
        pass  # Placeholder — optional if no mock available

    
if __name__ == '__main__':
    unittest.main()