import operator

from Errors.Error_Validation import ErrorValidation
from Repository.RepositoryError import RepositoryError
from operator import itemgetter

class Console:
    def __init__(self,service):
        self.__service = service
        self.__commands = {
            "add_protein":self.__ui_add_protein,
            "display_proteins":self.__ui_display_proteins,
            "len_protein":self.__ui_len_protein,
            "remove_protein": self.__ui_remove_protein,
            "search_protein": self.__ui_search_protein,
            "sort_proteins":self.__ui_sort_proteins,
            "filter_proteins": self.__ui_filter_proteins,
        }

    def __ui_add_protein(self):
        id_protein = input("Enter protein id:")
        molecular_weight = float(input("Enter molecular weight:"))
        deposited_atom_count = int(input("Enter deposited atom count:"))
        self.__service.fabric_protein(id_protein,deposited_atom_count,molecular_weight)

    def __ui_remove_protein(self):
        identifier_protein = input("Enter the ID of the protein to remove: ")
        try:
            self.__service.remove_protein(identifier_protein)
            print(f"Protein '{identifier_protein}' removed successfully.")
        except RepositoryError as BADID:
            print(f"Error: {BADID}")


    def __ui_display_proteins(self):
        proteins = self.__service.get_all()
        if not proteins:
            print("No stored proteins.")
            return
        print("\nStored Proteins (ID, Molecular Weight, Atom Count)")

        for protein in proteins:
            print(protein)

    def __ui_len_protein(self):
        proteins = self.__service.get_all()
        print(len(proteins))

    def __ui_search_protein(self):
        protein = input("Enter the protein to search: ")
        proteins = self.__service.get_all_protein_ids()
        for p in proteins:
            if p == protein:
                print("Protein ", protein, " is in the database.")
                break
        else:
            print("Protein ", protein, " is not in the database.")

    def __ui_sort_proteins(self):
        proteins = self.__service.get_all()
        if not proteins:
            print("No stored proteins.")
            return
        order = input("asc or desc")
        sorted_proteins = sorted(proteins, key=lambda p: p.get_molecular_weight(), reverse=(order == "desc"))
        for protein in sorted_proteins:
            print(protein)


    def __ui_filter_proteins(self):
        starts_with = input("Enter prefix to filter proteins by: ").strip()
        filtered_proteins = self.__service.filter_proteins(starts_with)

        if not filtered_proteins:
            print("No matching protein")
        else:
            print("\nFiltered Proteins:")
            for protein in filtered_proteins:
                print(protein)





    def run(self):
        print("\n=== Available Commands ===")
        print("1  Add a protein         (or type: add_protein)")
        print("2  Show stored proteins  (or type: display_proteins)")
        print("3  Show protein count    (or type: len_protein)")
        print("4  Delete protein        (or type: remove_protein")
        print("5  Search protein (or type: search_protein)")
        print("6  Sort proteins (or type: sort_proteins)")
        print("7  Filter proteins (or type: filter_proteins)")
        print("8  Exit                  (or type: exit)")

        while True:
            command_shortcuts = {
                "1": "add_protein",
                "2": "display_proteins",
                "3": "len_protein",
                "4": "remove_protein",
                "5": "search_protein",
                "6": "sort_proteins",
                "7": "filter_proteins",
                "8": "exit"
            }

            command = input("Enter command:")
            command = command.strip().lower()
            if command in command_shortcuts:
                command = command_shortcuts[command]

            if command == "":
                continue
            if command == "exit":
                return
            if command in self.__commands:
                try:
                    self.__commands[command]()
                except ValueError:
                    print("Invalid numerical value!")
                except ErrorValidation as ev:
                    print("Validation error:\n"+str(ev))
                except RepositoryError as re:
                    print("Repository error:\n"+str(re))

            else:
                print("Invalid command!")