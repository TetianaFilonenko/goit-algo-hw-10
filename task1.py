import pulp

# Create the problem
prob = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# Variables
lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('fruit_juice', lowBound=0, cat='Continuous')

# Objective function
prob += lemonade + fruit_juice, "Total_Drinks_Produced"

# Resource constraints
prob += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Limit"
prob += 1 * lemonade <= 50, "Sugar_Limit"
prob += 1 * lemonade <= 30, "Lemon_Juice_Limit"
prob += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

# Solve the problem
prob.solve()

# Results
print("Status:", pulp.LpStatus[prob.status])
print("Lemonade produced:", pulp.value(lemonade))
print("Fruit Juice produced:", pulp.value(fruit_juice))
print("Total drinks produced:", pulp.value(lemonade + fruit_juice))
