
from Errors.Error_Validation import ErrorValidation


class ValidateProtein:
    def validate_protein(self,protein):
        errors = ""
        if protein.get_identifier() == "":
            errors += "Protein cannot be an empty string."
        # if protein.get_identifier() != str:
        #     errors += "Protein id contains invalid characters."
        if protein.get_molecular_weight() < 0:
            errors += "Protein has a negative molecular weight."
        if protein.get_deposited_atom_count() < 0:
            errors += "Protein has a negative atomic count."

        if len(errors) > 0:
            raise ErrorValidation(errors)






