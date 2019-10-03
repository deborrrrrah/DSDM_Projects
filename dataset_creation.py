import os
import pandas as pd
# import re

base_dir = 'fraud_detection'
directory = os.fsencode(base_dir)

dummy = pd.read_csv(base_dir + '/DataminingContest2009.Task1.CV1.Test.Inputs')

df_columns = dummy.columns.tolist()
df_columns.append('target')

train_df_list = []
test_df_list = []
train_str = "Train"
test_str = "Test"
inputs_str = "Inputs"
targets_str = "Targets"

for file in os.listdir(directory) :
    filename = os.fsdecode(file)
    path = base_dir + '/' + filename

    if ((train_str in path)  and (inputs_str in path)) :
        df = pd.read_csv(path)
    elif ((train_str in path) and (targets_str in path)) :
        df['target'] = pd.read_csv(path)
        train_df_list.append(df) 
    elif ((test_str in path) and (inputs_str in path)) :
        df = pd.read_csv(path)
    elif ((test_str in path) and (targets_str in path)) :
        df['target'] = pd.read_csv(path)
        test_df_list.append(df)

train_dfs = pd.DataFrame(columns=df_columns)
test_dfs = pd.DataFrame(columns=df_columns)

train_dfs = pd.concat([df for df in train_df_list])
test_dfs = pd.concat([df for df in test_df_list])

train_dfs.to_csv('train.csv')
test_dfs.to_csv('test.csv')

train_df = pd.read_csv('train.csv', index_col=0)
test_df = pd.read_csv('test.csv', index_col=0)
print ('Training Data')
print (train_df.shape)
print (train_df.head(20))

print ()

print ('Testing Data')
print (test_df.shape)
print (test_df.head(20))