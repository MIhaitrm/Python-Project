class Protein:
    def __init__(self, identifier, deposited_atom_count, molecular_weight):
        self.__identifier = identifier
        self.__deposited_atom_count = deposited_atom_count
        self.__molecular_weight = molecular_weight

    def get_identifier(self):
        return self.__identifier

    def get_deposited_atom_count(self):
        return self.__deposited_atom_count

    def get_molecular_weight(self):
        return self.__molecular_weight

    def __str__(self):
        return f"{self.__identifier},{self.__molecular_weight},{self.__deposited_atom_count}"

