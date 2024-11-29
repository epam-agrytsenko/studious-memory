# Shopping Cart

Create a simple shopping cart system where users can add items, view their cart, and remove items. The program should maintain a list of items in the cart and allow users to interact with it through a menu.

#### Requirements:
1. The user should be able to **add** items to the shopping cart.
2. The user should be able to **view** all items in the shopping cart.
3. The user should be able to **remove** a specific item from the cart by name.
4. The user should be able to **exit** the program when done.

#### Instructions:
Display a menu with the following options:
 - 1: Add item
 - 2: View cart
 - 3: Remove item
 - 0: Exit

#### Example:
```
Welcome to the Shopping Cart System!
Please choose an option:
1. Add item
2. View cart
3. Remove item
0. Exit

Choice: 1
Enter item to add: Apples

Choice: 2
Items in your cart: ['Apples']

Choice: 1
Enter the item to add: Bananas

Choice: 2
Items in your cart: ['Apples', 'Bananas']

Choice: 1
Enter the item to add: Cat

Choice: 2
Items in your cart: ['Apples', 'Bananas', 'Cat']

Choice: 3
Enter the item to remove: #0
Item 'Apples' removed from your cart.

Choice: 3
Enter the item to remove: Cat
Item 'Cat' removed from your cart.

Choice: 2
Items in your cart: ['Bananas']

Choice: 0
Thank you for using the Shopping Cart System!
```

---

### Hints:
- Use a **list** to store the items in the cart.
- Use a **while True** to keep the program running until the user chooses to exit.
- Use **conditionals** to handle menu selections and **input validation** for non-existent items or options.
