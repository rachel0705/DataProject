import pandas as pd
import numpy as np
from dataCleansing import fill_missing_values

def test_fill_missing_values():
    # Create a DataFrame with missing values
    df = pd.DataFrame({
        'artist_name': ['Adele', None],
        'popularity': [85, np.nan]
    })

    # Run your cleaning function
    cleaned_df = fill_missing_values(df)

    # Check that missing text values are filled with "Unknown"
    assert cleaned_df['artist_name'].iloc[1] == 'Unknown'

    # Check that numeric missing values are filled (no NaNs left)
    assert not pd.isnull(cleaned_df['popularity']).any()