import hashlib
import csv
import random
import os
import time
import json
from datetime import datetime


def log(s):
    now = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    print(now + " " + s)


# Collection settings
unshuffled_metadata_folder = "unshuffled_metadata/"
collection_name = "ACIDHEADZ"
image_url = "https://api.acidheadz.cool/images/"
animation_url = "https://api.acidheadz.cool/animations/"
run_time = datetime.fromtimestamp(time.time()).strftime("%Y%m%d_%H%M%S")
ids = list(range(0, 2690))

# Hash of first ETH block mined after Nov 9th @ 11am UTC (block # will be confirmed as we get closer to the time)
# Block number: 13581763
# Etherscan URL: https://etherscan.io/block/13581763
# Block hash: 0xdb2092ccc3f9519bb9273d4b4e137c2b7e378b1e0637278f601b9c9e6083ffeb
block_hash = "0xdb2092ccc3f9519bb9273d4b4e137c2b7e378b1e0637278f601b9c9e6083ffeb"


log("Starting up")
log("ETH block hash for shuffling: " + block_hash + " - Dec: " + str(int(block_hash, 0)))


# Load unshuffled metadata
log("Loading unshuffled metadata")
unshuffled_metadata = ""
for id in ids:
    with open(unshuffled_metadata_folder + str(id), mode="r") as in_file:
        unshuffled_metadata += in_file.read()


# Calculate provenance hash
provenance_hash = hashlib.sha256(unshuffled_metadata.encode()).hexdigest()
log("Provenance hash: " + provenance_hash)


# Shuffle ID's
log("Shuffling ID's")
random.seed(int(block_hash, 0))
random.shuffle(ids)
log("Saving ID's mapping to shuffled_ids_mapping_" + run_time + ".csv")
with open("shuffled_ids_mapping_" + run_time + ".csv", mode='w') as out_file:
    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    header = [
        "Pre-Shuffling ID",
        "Post-Shuffling ID"
    ]
    out_writer.writerow(header)
    for i in range(0, len(ids)):
        out_writer.writerow([str(ids[i]),str(i)])


# Store shuffled metadata
shuffled_metadata_folder = "shuffled_metadata_" + run_time + "/"
os.mkdir(shuffled_metadata_folder)
log("Saving shuffled metadata to: " + shuffled_metadata_folder)

for i in range(0, len(ids)):
    with open(unshuffled_metadata_folder + str(ids[i]), mode="r") as in_file:
        m = json.loads(in_file.read())
        m["tokenId"] = i
        m["name"] = collection_name + " #" + str(i)
        m["image"] = image_url + str(i) + ".png"
        m["animation_url"] = animation_url + str(i) + ".mp4"
        with open(shuffled_metadata_folder + str(i), mode='w') as out_file:
            json.dump(m, out_file)