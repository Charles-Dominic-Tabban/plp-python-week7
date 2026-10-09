# PLP Python Week 7 - List Warmup

shopping_list = ["rice", "beans", "milk", "bread"]

print("Original shopping list:", shopping_list)

# Access the first and last items
print("First item:", shopping_list[0])
print("Last item:", shopping_list[-1])

# Count the items using len()
print("Number of items:", len(shopping_list))

# Change an item
shopping_list[1] = "lentils"
print("After changing an item:", shopping_list)

# Add an item
shopping_list.append("eggs")
print("After adding eggs:", shopping_list)

# Check before removing an item
if "milk" in shopping_list:
    shopping_list.remove("milk")

print("After removing milk:", shopping_list)

# Print every item
print("Final shopping list:")
for item in shopping_list:
    print(item)