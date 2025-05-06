import os

# Get the directory of the current Jupyter Notebook
notebook_dir = os.getcwd()

# File name to check
file_name = "owid-covid-data.csv"

# Full path to the file
file_path = os.path.join(notebook_dir, file_name)

# Check if the file exists in the same directory as the notebook
if os.path.exists(file_path):
    print(f"'{file_name}' is present in the same directory as the notebook.")
else:
    print(f"'{file_name}' is missing. Please ensure it is in the same directory as the notebook.")