#  python ./calculator-example.py  -- how to run this file in the mac terminal
# Tipping example

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax

total = meal + (meal * tip)

print("%.2f" % total)
