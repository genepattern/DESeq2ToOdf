import pandas as pd
from txt2odf_functions import *
import os

txt_file = parse_arguments(sys.argv)

name_of_file = os.path.basename(txt_file).strip('txt')+'odf'

data_df = pd.read_table(txt_file)
data_df.insert(1, 'Description', data_df['id'])
data_df.insert(0, 'Rank', data_df.index.values+1)
data_df.insert(3, 'Score', data_df['stat'])
data_df.rename(columns={'id': 'Feature'}, inplace=True)

# formatted_df = pd.DataFrame()
# formatted_df['Rank'] =
# formatted_df['Feature'] =
# formatted_df['Description'] =


vals = dict()
vals['gct'] = txt_file
vals['cls'] = txt_file
vals['n_perm'] = 1
vals['class_0'] = 'Class_0'
vals['class_1'] = 'Class_1'
vals['func'] = 'stat'
vals['rand_seed'] = 123456789
vals['dat_lines'] = len(data_df)

df2odf(data_df=data_df, vals=vals, file_name=name_of_file)

if True:
    print('File', name_of_file, "has been written!")
    print(data_df)
    print(len(data_df))
