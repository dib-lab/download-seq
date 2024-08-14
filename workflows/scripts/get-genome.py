#! /usr/bin/env python

import urllib.request

def generate_url(identifier):
    base_url = "https://ftp.ncbi.nlm.nih.gov/genomes/all/"
    parts = identifier.split('_')
    print(parts)
    accession = parts[1]  # Extract the accession number
    print(accession)
    version = parts[2]  # Extract the version number
    print(version)

    if parts[0] == 'GCA':
        url = f"{base_url}GCA/{accession[:3]}/{accession[3:6]}/{accession[6:]}/{identifier}_ASM{version}/{identifier}_ASM{version}_genomic.fna.gz"
    elif parts[0] == 'GCF':
        url = f"{base_url}GCF/{accession[:3]}/{accession[3:6]}/{accession[6:]}/{identifier}_ASM{version}/{identifier}_ASM{version}_genomic.fna.gz"
    else:
        url = None

    return url

def download_url(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded {url} to {filename}")
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")

url = generate_url("GCA_000143535.4")
download_url(url, "GCA_000143535.4_genomic.fna.gz")
