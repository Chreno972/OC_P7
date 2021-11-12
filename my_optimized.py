import pandas as pd
import time
from bf_dataset_model import DataSet as ds

source = "./csv/BruteForce.csv"
dataset1 = "./csv/dataset1_Python+P7.csv"
dataset2 = "./csv/dataset2_Python+P7.csv"
dataset3 = "./csv/dataset3.csv"
the_combinations = []
sum_prices = 0
sum_profit = 0
START_BUDGET = 2000
BUDGET = 2000

data = pd.read_csv(dataset3)

data_sorted = data.sort_values(by="profit", ascending=False)

for item in data_sorted.itertuples():
    if item.price < BUDGET:
        if item.price <= 1:
            pass
        else:
            thing = ds(item.name, item.price, item.profit)
            BUDGET -= item.price
    else:
        pass

print("La meilleure combinaison est :")
for item in ds.liste_dataset:
    print(item.name, item.price, item.profit)
    sum_prices += int(item.price)
    sum_profit += int(item.profit)

print(
    "\nbudget restant {:0.2f}€ sur un budget de départ de {}€".format(
        BUDGET, START_BUDGET
    )
)
print("\nArgent investi : {:0.2f}".format(sum_prices))
print("\nProfit obtenu : {:0.2f}".format(sum_profit))
