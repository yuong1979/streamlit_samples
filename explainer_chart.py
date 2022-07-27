import plotly.graph_objects as go  # pip install plotly



# data
label = ["Income", "Other Income", "Total Income", "Rent", "Food"]
source = [0, 1, 2, 2]
target = [2, 2, 3, 4]
value = [10, 2, 6, 4]

# data to dict, dict to sankey
link = dict(source = source, target = target, value = value)
node = dict(label = label, pad=50, thickness=5)
data = go.Sankey(link = link, node=node)

# plot
fig = go.Figure(data)
fig.show()



incomes = {'Salary': 1000, 'Other Income': 500}
expenses = {'Rent': 500, 'Utilities': 300, 'Groceries': 200, 'Other Expenses': 300}


label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
print (label)


value = list(incomes.values()) + list(expenses.values())
print (value)

target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
print (target)


# Create sankey chart
label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
value = list(incomes.values()) + list(expenses.values())

# Data to dict, dict to sankey
link = dict(source=source, target=target, value=value)
node = dict(label=label, pad=20, thickness=30, color="#E694FF")
data = go.Sankey(link=link, node=node)

# Plot it!
fig = go.Figure(data)
fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
fig.show()


