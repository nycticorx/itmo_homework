import pandas as pd

FILE_ID = "1LtthrtKpMg1cPQEDkKJjglbqGIUDFjYr"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

raw_data = pd.read_csv(file_url)     

print(raw_data.head(10))             
