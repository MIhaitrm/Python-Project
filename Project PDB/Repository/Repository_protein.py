import csv
import os
from Repository.RepositoryError import RepositoryError
from Domeniu.Protein import Protein
import operator

class RepositoryProtein:
    def __init__(self, filename="proteins.csv"):
        self._proteins = {}
        self.filename = filename
        self.load_from_file()

    def add_protein(self, protein):
        if protein.get_identifier() in self._proteins:
            raise RepositoryError("Protein exists!")
        self._proteins[protein.get_identifier()] = protein
        self.save_to_file()

    def remove_protein(self, identifier_protein):
        if identifier_protein not in self._proteins:
            raise RepositoryError("Protein does not exist!")
        del self._proteins[identifier_protein]
        self.save_to_file()

    def update_protein(self, identifier_protein, new_protein):
        if identifier_protein not in self._proteins:
            raise RepositoryError("Protein does not exist!")
        self._proteins[identifier_protein] = new_protein

    def search_protein(self, identifier_protein):
        if identifier_protein not in self._proteins:
            raise RepositoryError("Protein does not exist!")
        return self._proteins[identifier_protein]


    def filter_words(self, starts_with):
        starts_with = str(starts_with)
        filtered_proteins = []
        for protein in self._proteins.values():
            if protein.get_identifier().find(starts_with) == 0:
                filtered_proteins.append(protein)
        return filtered_proteins


    def __len__(self):
        return len(self._proteins)

    def sort_proteins(self):
        return list(sorted(self._proteins.values()))




    def get_all(self):
        return list(self._proteins.values())

    def save_to_file(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Molecular Weight", "Atom Count"])
            for protein in self._proteins.values():
                writer.writerow(
                    [protein.get_identifier(), protein.get_deposited_atom_count(), protein.get_molecular_weight()])

    def load_from_file(self):
        with open(self.filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            self._proteins = {row[0]: Protein(row[0], int(row[1]), float(row[2])) for row in reader}
