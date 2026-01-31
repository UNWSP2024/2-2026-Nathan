# By Nathan Nelsen
# Written 1/30/26
# Calculate Total Purchase

def calculate_total_purchase():
    # A customer in a store is purchasing five items.
    # Write a program that asks for each item,
    itema = 5
    itemb = 15
    itemc = 24
    itemd = 132
    iteme = 89
    # then displays the subtotal of the sale,
    subtotal = itema + itemb + itemc + itemd + iteme
    # the amount of sales tax, and the total.
    sales_tax = 0.07
    total = subtotal*(1+sales_tax)
    print("The subtotal is", subtotal)
    print("The sales tax is 7%")
    print("The total is", total)
    # Assume the sales tax is 7 percent.

calculate_total_purchase()
