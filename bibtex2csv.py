import bibtexparser
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="bibtex to csv converter")
parser.add_argument("-i", "--input-file", help="Input file to be used", required=True)
parser.add_argument("-o", "--output-file", help="Output file to be used", required=True)
args = vars(parser.parse_args())
input_file, output_file = args["input_file"], args["output_file"]

with open(input_file) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
    df = pd.DataFrame(bib_database.entries)
    df.to_csv(output_file, index=False)
