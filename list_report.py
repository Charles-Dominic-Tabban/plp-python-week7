# PLP Python Week 7 - Shopping List Report

shopping_list = ["bread", "milk", "eggs", "rice", "apples"]

print("===== SHOPPING LIST REPORT =====")
print("Shopping list:", shopping_list)

# Count items with more than four letters
long_items_count = 0

for item in shopping_list:
    if len(item) > 4:
        long_items_count += 1

print("Items with more than four letters:", long_items_count)

# Find the longest item using a manual loop comparison
longest_item = shopping_list[0]

for item in shopping_list:
    if len(item) > len(longest_item):
        longest_item = item

print("Longest item:", longest_item)