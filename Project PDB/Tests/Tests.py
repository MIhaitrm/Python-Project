from Domeniu.Protein import Protein
from Errors.Error_Validation import ErrorValidation
from Validation.Validate_Protein import ValidateProtein


class Tests:
    def run_all_tests(self):
        print("Running all tests")
        self.__run_tests_Domeniu()
        self.__run_tests_Validate_Protein()
        print("All tests passed")

    def __run_tests_Domeniu(self):
        print("Running tests Domeniu")
        identifier = "1BLX"
        molecular_weight = -19.92
        deposited_atom_count = -4
        protein = Protein(identifier, deposited_atom_count, molecular_weight)
        assert protein.get_identifier() == identifier
        assert protein.get_molecular_weight() == molecular_weight
        assert protein.get_deposited_atom_count() == deposited_atom_count
        print("All tests passed")

    def __run_tests_Validate_Protein(self):
        print("Running tests Validation")
        identifier = "1BLX"
        molecular_weight = 19.92
        deposited_atom_count = 4
        protein = Protein(identifier, deposited_atom_count,molecular_weight)
        validation_protein = ValidateProtein()
        validation_protein.validate_protein(protein)
        bad_identifier = ""
        bad_molecular_weight = -19.92
        bad_deposited_atom_count = -4
        bad_protein = Protein(bad_identifier, bad_molecular_weight, bad_deposited_atom_count)
        try:
            validation_protein.validate_protein(bad_protein)
            assert False
        except ErrorValidation as e:
            assert str(e) == "Protein cannot be an empty string.Protein has a negative molecular weight.Protein has a negative atomic count."
        print("All tests passed")



