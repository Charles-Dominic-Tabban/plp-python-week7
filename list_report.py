# PLP Python Week 7 - Shopping List Report

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

print("===== SHOPPING LIST REPORT =====")

# Print each item with a number
number = 1
for item in items:
    print(str(number) + ". " + item)
    number += 1

# Count items with more than four letters
long_items_count = 0
for item in items:
    if len(item) > 4:
        long_items_count += 1

print("Items with more than four letters:", long_items_count)

# Find the longest item using a manual loop comparison
longest_item = items[0]
for item in items:
    if len(item) > len(longest_item):
        longest_item = item

print("Longest item:", longest_item)