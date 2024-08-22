import pandas as pd

df = pd.read_csv('data.csv')

#print dataset but only first 5 and last 5
print(df)

#prints whole dataset
# print(df.to_string())

#prints specifit row by index number
# print(df.loc[0])

#print 0 and 5
# print(df.loc[[0 5]])

#prints data from 0 to 5
# print(df.loc[0:5])

index = int(input("Enter Row number : "))
print()

if index <= 0 :
    print("Less than 0 not available !!!")
elif index >= len(df) + 1:
    print("Greater than the records !!!")
else:
    print(df.loc[index - 1])