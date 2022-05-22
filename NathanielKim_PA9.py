""" Python Program that process food orders """

def menu():
   """ Printing menu """
   print("\nMenu\n\n1 - Appetizers\n2 - Entrees\n3 - Beverages\n4 - Desserts\n5 - Side Orders\nc - Checkout\n")
  
def checkout(foodCart):
   """ Printing report   """
   print("\n\nSummary of food bill:\n\n")
   print("%-15s %-25s %-20s\n"%("Category", "Number of Items", "Cost of Items"))
   # For Updating values
   qty=0
   cost=0
   # Iterating over items in dict
   for item in foodCart.keys():
       # Checking quantity
       if foodCart[item][0] != 0:
           # Printing results
           print("%-20s %-20d $ %-20.1f"%(item, foodCart[item][0], foodCart[item][1]))
           # Updating totals
           qty += foodCart[item][0]
           cost += foodCart[item][1]
   print("\n%-20s %-20d $ %-20.2f"%("Total", qty, cost))
   # Returning values
   return [qty, cost]
      
def process():
   """ Function that process the order """
   # Dictionary that holds the items as Keys, quantity and cost as list values
   foodCart = {'Appetizers':[0,0], 'Entrees':[0,0], 'Beverages':[0,0], 'Desserts':[0,0], 'Side Orders':[0,0], 'Checkout':[0,0]}
   items = ['Appetizers', 'Entrees', 'Beverages', 'Desserts', 'Side Orders']
   # Loop till user want to quit
   while True:
       # Printing menu
       menu()
       # Reading selection
       selection = input('Enter your selection: ')
       # Checking selection
       if selection.lower() == 'c':
           break
       # Converting selection to integer
       selection = int(selection)
       # Reading quantity and cost
       qty = int(input('Enter quantity: '))
       # Reading cost
       cost = float(input('Enter cost: $'))
       # Updating in dictionary
       foodCart[items[selection-1]][0] += qty
       foodCart[items[selection-1]][1] += cost
   # Returning cart
   return foodCart
      
def main():
   """ Main program """
   # Total values
   numCarts = 0
   totalQuantity = 0
   totalPrice = 0
   # Loop till user want to end
   while True:
       # Calling function
       cart = process()
       # Printing check out
       [qty, cost] = checkout(cart)
       # Updating total values
       numCarts += 1
       totalQuantity += qty
       totalPrice += cost
       # Prompting for continuation
       ch = input('\nDo you want to process more food carts? (y/n): ')
       # Checking input
       if ch.lower() == 'n':
           break
   # Printing final values
   print("\n\nTotal number of carts processed: ", numCarts)
   print("\nTotal Food Items: ", totalQuantity)
   print("\nTotal cost: $", totalPrice)
      
# Calling main
main()