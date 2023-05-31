# %%
import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# %% [markdown]
# # Loading files

# %%
root_dir = 'simulations'
simulation_folders = os.listdir(root_dir)
dataframes = {}

for folder in simulation_folders:
    folder_path = os.path.join(root_dir, folder)
    
    if os.path.isdir(folder_path):
        json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
        
        metrics = []
        for json_file in json_files:
            json_file_path = os.path.join(folder_path, json_file)
            
            with open(json_file_path, 'r') as f:
                json_data = json.load(f)
            
            items = json_data['data']['items']

            metric_data = {item['title']: item['value'] for item in items if item['title'] != 'Time to discovery'}
            metrics.append(metric_data)

        df = pd.DataFrame(metrics)
        dataframes[folder] = df

# Access the DataFrame for a specific simulation folder like this:
# dataframes['Appenzeller-Herzog_2019_-m_logistic_-e_tfidf']

# %%
def average_metrics(df):
    metric_averages = {}
    for column in df.columns:
        if df[column].dtype == "object":
            metric_list = df[column].explode().tolist()
            metric_dict = {}
            for metric in metric_list:
                if metric[0] in metric_dict:
                    metric_dict[metric[0]].append(metric[1])
                else:
                    metric_dict[metric[0]] = [metric[1]]
            for key, values in metric_dict.items():
                new_col_name = f"{column} {key}"
                metric_averages[new_col_name] = round(sum(values) / len(values), 2)
        else:
            metric_averages[column] = round(df[column].mean(), 2)
    return metric_averages

    
# split up the name into categories
def split_name(name):
    # dataset name is everything before "-m"
    dataset = name.split("-m")[0]
    # model name is everything between "-m" and "-e"
    model = name.split("-m")[1].split("-e")[0]
    # embedding name is everything after "-e"
    embedding = name.split("-e")[1]
    # remove trailing underscores
    dataset = dataset[:-1]
    model = model[1:-1]
    embedding = embedding[1:]
    return dataset, model, embedding

# %%
result_list = []
for df in dataframes:
    dataset, model, embedding = split_name(df)
    result_list.append({**{'dataset': dataset}, **{'model': model}, **{'fe': embedding}, **average_metrics(dataframes[df])})

df = pd.DataFrame(result_list)

# make into a json file
with open("results.json", "w") as json_file:
    json.dump(result_list, json_file)

# %%
# remove leftover vars
del f, folder, folder_path, json_data, json_file, json_file_path, json_files, metric_data, metrics, root_dir, model, embedding

# %% [markdown]
# # Data Science part

# %%
# df remove Walker_2018 dataset
df = df[df.dataset != 'Walker_2018']

# %%
df.groupby(['fe','model']).mean()

# %%
df.boxplot(column=['Work Saved over Sampling 0.95'], by=['fe','model'], figsize=(20,10))

# %%
df.boxplot(column=['Work Saved over Sampling 0.95'], by=['model'], figsize=(20,10))

# %%
df.boxplot(column=['Work Saved over Sampling 0.95'], by=['fe'], figsize=(16,10))

# %%
# sort by wss 0.95
df.groupby("dataset").mean().sort_values(by="Work Saved over Sampling 0.95", ascending=False)


