# PLP Python Week 7 - List Warmup

shopping_list = ["rice", "beans", "milk", "bread"]

print("Original shopping list:", shopping_list)

print("First item:", shopping_list[0])
print("Third item:", shopping_list[2])

shopping_list[1] = "lentils"
print("After changing an item:", shopping_list)

shopping_list.append("eggs")
print("After adding eggs:", shopping_list)

if "milk" in shopping_list:
    shopping_list.remove("milk")

print("After removing milk:", shopping_list)

print("Final shopping list:")
for item in shopping_list:
    print(item)