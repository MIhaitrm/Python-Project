from Domeniu import Protein
from Domeniu.Protein import *
from Domeniu_Protein import validate_protein
from Validation import *
class ServiceProtein:
    def __init__(self, validate_protein, repository_protein):
        self.__validation_protein = validate_protein
        self.__Repository_proteins = repository_protein


    def fabric_protein(self, identifier, deposited_atom_count, molecular_weight):
        new_protein = Protein(identifier, deposited_atom_count, molecular_weight)
        self.__validation_protein.validate_protein(new_protein)
        self.__Repository_proteins.add_protein(new_protein)

    def get_all(self):
        return self.__Repository_proteins.get_all()


    def remove_protein(self, identifier_protein):
        self.__Repository_proteins.remove_protein(identifier_protein)

    def search_protein(self, identifier_protein):
        self.__Repository_proteins.search_protein(identifier_protein)

    def get_all_protein_ids(self):
        protein_ids = []
        for protein in self.__Repository_proteins.get_all():
            protein_ids.append(protein.get_identifier())

        return protein_ids

    def filter_proteins(self, starts_with):
        return self.__Repository_proteins.filter_words(starts_with)

    def sort_proteins(self, proteins):
        return self.__Repository_proteins.sorted_proteins(proteins)

    def get_all_protein_mw(self):
        protein_mw = []
        for protein in self.__Repository_proteins.get_all():
            protein_mw.append(protein.get_molecular_weight())
        return protein_mw




