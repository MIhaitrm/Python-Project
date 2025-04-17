from Business.Service import ServiceProtein
from Tests.Tests import *
from Validation.Validate_Protein import ValidateProtein
from Repository.Repository_protein import RepositoryProtein
from UI.Console import Console
tests = Tests()
tests.run_all_tests()
validate_protein=ValidateProtein()
repository_protein=RepositoryProtein()
service_protein=ServiceProtein(validate_protein, repository_protein)
ui = Console(service_protein)
ui.run()
