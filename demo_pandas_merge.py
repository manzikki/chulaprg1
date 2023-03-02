#demonstration of reading CSV data from a file into data frames and merging them
import pandas as pd

persons = pd.read_csv("data.csv")
pets = pd.read_csv("pets.csv")

ppets = persons.merge(pets)
print(ppets)

ppets = persons.merge(pets, how="outer")
print(ppets)


