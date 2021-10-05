class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


invalid = False
valid_domains = {"com", "bg", "org", "net"}
while True:
    line = input()
    if line == "End":
        break

    email_parts = line.split("@")
    if len(email_parts) == 1:
        invalid = True
        raise MustContainAtSymbolError("Email must contain @")

    name, domain_name = email_parts

    if len(name) <= 4:
        invalid = True
        raise NameTooShortError("Name must be more than 4 characters")

    domain_name_parts = domain_name.split(".")
    domain = domain_name_parts[-1]
    if len(domain_name_parts) != 2:
        invalid = True
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if domain not in valid_domains:
        invalid = True
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

if not invalid:
    print("Email is valid")