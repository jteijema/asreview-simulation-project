import os
import json

# Specify the directories
plots_dir = "./output/plots"
simulations_dir = "./output/simulations"

# Collect data about the images
images_data = []
for file_name in os.listdir(plots_dir):
    if file_name.endswith(".png"):
        image_path = os.path.join("plots", file_name).replace("\\", "/")
        images_data.append({"name": file_name[:-4], "imagePath": "https://sos-de-fra-1.exo.io/asreview-output/"+ image_path})

# Count the number of simulations
count = 0
for folder_name in os.listdir(simulations_dir):
    folder_path = os.path.join(simulations_dir, folder_name)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".json"):
                count += 1

print(f"There are {count} simulations in the folder.")
print(f"There are {count*6511} datapoints in the results.")

with open("data.json", "w") as json_file:
    json.dump({"images": images_data, "count": count}, json_file)
    print("Data written to data.json")