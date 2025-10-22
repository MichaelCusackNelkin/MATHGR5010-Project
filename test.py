import databento as db
import numpy as np
import pandas as pd
import glob

sym_1 = 'AMDL'
sym_2 = "AMD"

# Get all CSV files in the data folder per desired symbol
sym1_files = glob.glob(f'data/EQUS-OHLCV-1d/*.ohlcv-1d.{sym_1}.dbn.zst')
sym2_files = glob.glob(f'data/EQUS-OHLCV-1d/*.ohlcv-1d.{sym_2}.dbn.zst')

# Read all files into a list of dataframes
dfs_sym1 = [db.DBNStore.from_file(file).to_df(tz = "US/Eastern") for file in sym1_files]
dfs_sym2 = [db.DBNStore.from_file(file).to_df(tz = "US/Eastern") for file in sym2_files]

# Concatenate and sort
sym1 = pd.concat(dfs_sym1, join='inner').sort_index()
sym2 = pd.concat(dfs_sym2, join='inner').sort_index()

# Combine into one dataframe
data = pd.DataFrame({"sym1": sym1['close'], "sym2": sym2['close']})