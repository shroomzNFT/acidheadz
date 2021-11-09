# acidheadz

Using the resources in this repository, users can verify the fairness of Acidheadz reveal.
Here is the process:
1) Validate that the pre-reveal metadata is authentic, by getting its SHA256 hash and comparing it to the provenance hash that was incorporated in the contract prior to the launch. This will prove that we are working with the same metadata to do the shuffling: no tampering of the metadata.
2) Shuffle the metadata using the hash of the first ETH block mined after Tue Nov 9th @ 11am UTC as seed.
3) Compare that shuffled metadata with the live metadata: they will be identical.

To run the process, simply download this repository and run `python shuffle.py`
