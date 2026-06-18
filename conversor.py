#%%
#Conversor de pdf/csv 

from pypdf import PdfReader
import csv 

reader = PdfReader("Item.pdf")

with open("output.csv", "w",
            newline="") as f:

    writer = csv.writer(f)

    for page in reader.pages:
        writer.writerow(
            [page.extract_text()]
        )

print("CSV criando!")

#%%
#Converson dde pdf/json

from pypdf import PdfReader 
import json 

reader = PdfReader("Item.pdf")

pages = {}

for i, page in enumerate(reader.pages):
    pages[f"Page_{i+1}"] = page.extract_text()

with open("data.json", "w") as f:
    json.dump(pages, f, indent = 4)

print("JSON criando!")