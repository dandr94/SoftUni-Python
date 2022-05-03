class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        date_args = date.split('.')
        year = int(date_args[2])
        month = int(date_args[1])
        if str(month).isdigit():
            if month == 1:
                month = 'January'
            elif month == 2:
                month = 'February'
            elif month == 3:
                month = 'March'
            elif month == 4:
                month = 'April'
            elif month == 5:
                month = 'May'
            elif month == 6:
                month = 'June'
            elif month == 7:
                month = 'July'
            elif month == 8:
                month = 'August'
            elif month == 9:
                month = 'September'
            elif month == 10:
                month = 'October'
            elif month == 11:
                month = 'November'
            elif month == 12:
                month = 'December'

        return cls(name, id, year, month, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. " \
               f"Status: {'rented' if self.is_rented else 'not rented'}"
