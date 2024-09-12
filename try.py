strn = "IF hello THEN Hello Rohan"
rules = {}
condition,response = strn.split(" THEN ")
new_condition = condition.replace("IF ","")

rules[new_condition] = response
print(rules)