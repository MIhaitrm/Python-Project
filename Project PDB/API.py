import operator

import requests
from Bio.PDB import PDBList
from operator import itemgetter
# Create an instance of the PDBList class
pdb_list = PDBList()

# Specify the PDB ID of the structure you want to download
pdb_id = "4hhb" #zinc finger

# Download the MMCIF file using the retrieve_pdb_file method
pdb_filename = pdb_list.retrieve_pdb_file(pdb_id, pdir="data/PDB_files", file_format="mmCif")

# Print the name of the downloaded file
print(pdb_filename)






import requests

data = requests.get("https://data.rcsb.org/rest/v1/core/entry/4hhb")

print(data.status_code)

info_4hhb = data.json()
print(info_4hhb.keys())
dictionary_name=["key_name"]
interface = requests.get("https://data.rcsb.org/rest/v1/core/interface/4hhb/1/1")
interface_info = interface.json()
print(interface_info["rcsb_interface_info"])

import json

my_query = {
    "query": {
        "type": "terminal",
        "service": "full_text",
        "parameters": {
            "value": '"oxygen storage"'
        }
    },

    "return_type": "entry"
}

my_query = json.dumps(my_query)
print(my_query)
data = requests.get(f"https://search.rcsb.org/rcsbsearch/v2/query?json={my_query}")
results = data.json()
print(results)

print(info_4hhb["rcsb_entry_info"])


pdb_id1 = "2BMM"

pdb_filename = pdb_list.retrieve_pdb_file(pdb_id1, pdir="data/PDB_files", file_format="mmCif")

# Print the name of the downloaded file
print(pdb_filename)

data = requests.get("https://data.rcsb.org/rest/v1/core/entry/2bmm")
info_2BMM = data.json()
print(info_2BMM["rcsb_entry_info"])


# f = operator.itemgetter('molecular weight')
# print(f)