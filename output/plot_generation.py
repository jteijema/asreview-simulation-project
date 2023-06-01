# %%
import matplotlib.pyplot as plt
import json
import os
import pandas as pd
import numpy as np

from asreviewcontrib.insights.plot import _plot_recall


# %%
# get all folders in simulations
folders = os.listdir("simulations")

# %%
dataset_records = {
    "Appenzeller-Herzog_2019": 2873,
    "Bos_2018": 4878,
    "Brouwer_2019": 38114,
    "Chou_2003": 1908,
    "Chou_2004": 1630,
    "Donners_2021": 258,
    "Hall_2012": 8793,
    "Jeyaraman_2020": 1175,
    "Leenaars_2019": 5812,
    "Leenaars_2020": 7216,
    "Meijboom_2021": 882,
    "Menon_2022": 975,
    "Moran_2021": 5214,
    "Muthu_2021": 2719,
    "Nelson_2002": 366,
    "Oud_2018": 952,
    "Radjenovic_2013": 5935,
    "Sep_2021": 271,
    "Smid_2020": 2627,
    "van_de": 4544,
    "Valk_2021": 725,
    "van_der": 1970,
    "van_Dis": 9128,
    "Walker_2018": 48375,
    "Wassenaar_2017": 7668,
    "Wolters_2018": 4280
}


# %%
def get_labels(df):
    return [[inner_list[1] for inner_list in row] for row in df.iloc[:, 4].apply(lambda x: x['value'])]


def tds_to_records(labels):
    records = []
    for i in range(labels[-1]):
        if i+1 in labels:
            records.append(1)
        else:
            records.append(0)
    return records


def pad_simulation_labels(labels, n_records):
    return labels + np.zeros(n_records - len(labels)).tolist()


# %%
for folder in folders:
    metrics = []

    # get all json files in folder
    files = os.listdir("simulations\\" + folder)

    # loop over files and append metrics to list
    for file in files:
        if file.endswith(".json"):
            # open file
            with open(os.path.join("simulations\\", folder, file), 'r') as f:
                data = json.load(f)
                metrics.append(data['data']['items'])

    df = pd.DataFrame(metrics)

    fig, ax = plt.subplots()

    # get n_records from dataset_records (first part of folder name is key)
    n_records = dataset_records[folder.split("_")[0]+"_"+folder.split("_")[1]]

    for label in get_labels(df):
        _plot_recall(ax, pad_simulation_labels(tds_to_records(label), n_records), y_absolute=True)

    # folder name as title but _ is space
    plt.title(folder.replace("_", " "))

    # set size
    fig.set_size_inches(6.4, 4.8)

    # save figure
    plt.savefig(".\plots\plot_recall_sim_"+folder+".png", facecolor='w', dpi=100)
    print("Saved plot for " + folder)
