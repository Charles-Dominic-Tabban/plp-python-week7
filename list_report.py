# PLP Python Week 7 - Shopping List Report

shopping_list = ["bread", "milk", "eggs", "rice", "apples"]

print("===== SHOPPING LIST REPORT =====")

item_count = 0

for item in shopping_list:
    item_count += 1
    print(str(item_count) + ". " + item.title())

print("Total number of items:", item_count)

if shopping_list:
    print("First item:", shopping_list[0].title())
    print("Last item:", shopping_list[-1].title())

if "milk" in shopping_list:
    print("Milk is on the shopping list.")
else:
    print("Milk is not on the shopping list.")