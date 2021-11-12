from itertools import combinations as cbts
import csv
from bf_dataset_model import DataSet as ds

data_set = []
the_csv_file = "./csv/BruteForce.csv"
MONEY = 500
the_combinations = []
best_combinations_price = 0
gains_count = 0
prices_count = 0

# open the file then put the data into the data_set list
with open(the_csv_file, newline="") as csv_file:  # O(1)
    reader = csv.DictReader(csv_file)  # O(n)
    for elem in reader:  # O(n)
        data_set.append(
            ds(elem["name"], elem["price"], elem["profit"]).serialize_dataset()
        )  # O(1)

# Search for all possible combinations
# use cbs on data_set to get all possible combinations
for i in range(1, len(data_set) + 1):  # O(n)
    for combination in cbts(data_set, i):  # O(n)
        for elem in combination:  # O(n)
            if elem["price"] <= 0:
                pass
            elif sum(elem["price"] for elem in combination) <= MONEY:
                the_combinations.append(combination)  # O(1)


best_combination = max(
    the_combinations, key=lambda x: sum(elem["profit"] for elem in x)  # O(n)
)


print("\nLa meilleure combinaison est:\n")
print("NOM        |PRIX|PROFIT")
for elem in best_combination:  # O(n)
    print("______________________")  # O(1)
    print(f"{elem['name']} | {elem['price']} | {elem['profit']}   ")  # O(1)
print(
    f"\nPour un investissement total de {sum(x['price'] for x in best_combination)}€ de votre budget"
)
print(
    f"Vous récoltez un bénéfice de {sum(x['profit'] for x in best_combination)}€ sur 2 ans"
)

# ? FAIRE EN SORTE QUE LE NOM D'UN DATASET N'APPARAISSE PAS PLUSIEURS FOIS ET DONC
# ? QUE SON PRIX NE SOIT PAS CALCULE PLUSIEURS FOIS AUSSI
