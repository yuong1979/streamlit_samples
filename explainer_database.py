from deta import Deta  # pip install deta


DETA_KEY = "<YOUR DETA KEY>"

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("monthly_reports")


def insert_period(period, incomes, expenses, comment):
    """Returns the user on a successful user creation, otherwise raises and error"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)

# Example Data
period = "2022_April"
comment = "Some comment"
incomes = {'Salary': 1500, 'Blog': 50, 'Other Income': 10}
expenses = {'Rent': 600, 'Utilities': 200, 'Groceries': 300,
            'Car': 100, 'Other Expenses': 50, 'Saving': 10}


insert_period(period, incomes, expenses, comment)

fetch_all_periods()

get_period("2022_April")


