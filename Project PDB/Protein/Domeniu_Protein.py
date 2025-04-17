
from List_Proteins import *

def create_protein(protein_id, name, atoms, organism, total_structure_weight):
    return {
        "protein_id": protein_id,
        "name": name,
        "atom_count": atoms,
        "organism": organism,
        "total_structure_weight": total_structure_weight
    }

def get_protein_id(protein):
    return protein["protein_id"]
def get_name(protein):
    return protein["name"]
def get_atoms(protein):
    return protein["atom_count"]
def get_amino_acids(protein):
    return protein["atom_count"]
def get_organism(protein):
    return protein["organism"]
def get_total_structure_weigth(protein):
    return protein["total_structure_weight"]

def test_create_protein():
    protein_id:1
    name = "4HHB"
    atoms = 146
    organism = "Homo Sapiens"
    total_structure_weigth = 64.74
    epsilon = 0.000001
    protein = create_protein(id, name, atoms, organism, total_structure_weigth)
    assert id == get_protein_id(protein)
    assert name == get_name(protein)
    assert atoms == get_atoms(protein)
    assert organism == get_organism(protein)


test_create_protein()

proteins = ["4HHB", "1BLX", "103L"]
def get_protein_from_proteins(_proteins):
    proteins = ["4HHB", "1BLX", "103L"]
    


def validate_protein():
    pass

def test_validate_protein():
    assert True

def run_all_tests():
    test_create_protein()
    test_validate_protein()

run_all_tests()

#print("All tests run succesfully")