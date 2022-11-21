"""Script to output amino acid frequencies in FASTA file"""

#   Copyright 2022 Michael Riffle
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from pyteomics import fasta
import argparse
import os
import sys


def main(fasta_file):
    """Calculate amino acid frequencies in FASTA file then output report

    Parameters:
        fasta_file (string): Path to FASTA file

    Returns:
        None
    """

    if not os.path.isfile(fasta_file):
        print('Could not find file: ' + fasta_file, file=sys.stderr)
        exit(1)

    residue_counts = dict()
    total_residues = 0

    with open(fasta_file, mode='rt') as f:
        for description, sequence in fasta.FASTA(f):
            total_residues = total_residues + len(sequence)

            for residue in sequence:
                if residue not in residue_counts:
                    residue_counts[residue] = 1
                else:
                    residue_counts[residue] = residue_counts[residue] + 1

    print_report(fasta_file, total_residues, residue_counts)


def print_report(fasta_file, total_residues, residue_counts):
    """Print report for frequencies of amino acids in FASTA file

    Parameters:
        fasta_file (string): Path to FASTA file
        total_residues (int): Total number of residues found in all proteins
        residue_counts (dict): Dict mapping single letter amino acid codes to respective counts

    Returns:
        None
    """

    print("Profile for: " + fasta_file)

    print("\tTotal residues: " + str(total_residues))

    print("\tTotals for each amino acid code:")

    print("\t\tAA\tcount\tfrac")
    print("\t\t--\t-----\t----")

    for residue in sorted(residue_counts):
        rcount = residue_counts[residue]
        rperc = rcount / total_residues

        print("\t\t" + residue + "\t" + str(rcount) + "\t" + str(round(rperc, 6)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("fasta_file", nargs=1)
    args = parser.parse_args()

    main(args.fasta_file[0])
