import operator

import pandas as pd

from List_Proteins import *
from Protein import *
from operator import itemgetter

def display_menu():
    print("1. Search for ... ")
    print("2. Filter by ... ")
    print("3. Sorting ...")
    print("4. Exit")

def search_for_protein(protein, protein_list):
    for w in protein_list:
        if w == protein:
            return True
    return False

def filter_proteins(starts_with, protein_list):
    new_list=[]
    for protein in protein_list:
        if protein.find(starts_with) == 0:
            new_list.append(protein)
    return new_list

def sort_list(protein_list):
    return sorted(protein_list)

running = True
proteins = ["4HHB", "1BLX", "103L"]
while running:
    display_menu()
    option = int(input("Choose option: "))
    if option == 1:
        protein = input("Please input a protein to search for: ")
        while protein == " ":
            protein = input("Please input a valid word or 'exit' if you want to return to the menu: ")
            if protein == "exit":
                break
        if protein == "exit":
            continue
        if search_for_protein(protein, proteins):
            print("The protein", protein, "is part of the proteins list.")
        else:
            print("The protein", protein, "is not part of the proteins list.")
    elif option == 2:
        starting_character = input("Please provide the starting string for filtering: ")
        result = filter_proteins(starting_character, proteins)
        print("The proteins from the protein_list that start with", starting_character, "are:", result)
    elif option == 3:
        result = sort_list(proteins)
        print("The sorted list is: ", result)
    elif option == 4:
        running = False


f = operator.itemgetter('molecular weight')
print(f)