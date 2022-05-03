class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class TooManyAtSymbols(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidDomainName(Exception):
    pass


allowed_domains = ['.com', '.bg', '.org', '.net']

while True:
    emails = input()

    if emails == 'End':
        break

    if '@' not in emails:
        raise MustContainAtSymbolError('Email must contain @')

    username, domain, *args = emails.split('@')  # args defense for too many @'s

    if len(args) > 0:  # custom made error for more @'s in email
        raise TooManyAtSymbols('Only one @ is allowed in email')

    if len(username) < 5:
        raise NameTooShortError('Name must be more than 4 characters')

    if len([x for x in domain.split('.') if x]) != 2:  # custom made error for invalid domain name
        raise InvalidDomainName('Invalid domain name.')

    if '.' + domain.split('.')[-1] not in allowed_domains:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(allowed_domains)}')
    else:
        print('Email is valid')
