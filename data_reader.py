import csv
from typing import Dict, List

files = ["openings/a.tsv", "openings/b.tsv", "openings/c.tsv", "openings/d.tsv", "openings/e.tsv"]

def read_openings(files: List[str] = files) -> Dict[str, List[str]]:
    
    openings = {}

    for file in files:
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for row in reader:
                openings[row[0]] = row
    
    return openings
    