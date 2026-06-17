"""
1. Create a set called fruits with values {"air", "water", "food"}. Check if "food" is in 
the set and print the result.

3. Given the set animals = {"cat", "dog", "rabbit"}, add multiple items ["horse", "sheep"] to the set and print the updated set.

5. Given the set cities = {"New York", "Los Angeles", "Chicago"}, remove "Houston" which is not in the set without raising an error.

7. Create two sets, set1 = {1, 2, 3} and set2 = {3, 4, 5}. Use the union method to join the sets and print the result.

9. Create a set called prime_numbers with values {2, 3, 5, 7}. Add the number 11 to the set and print the updated set.

11. Create a set called vowels with values {"a", "e", "i", "o", "u"}. Empty the set and print the result.

13. Create a set called tech_brands with values {"Apple", "Google", "Microsoft"}. 
	Add the items from another set {"Amazon", "Facebook"} and print the updated set 
	tech_brands without creating a new set.

15. Given a list numbers_list = [1, 2, 3, 4, 4, 5, 5], convert this list to a set to remove duplicates and print the resulting set.

17. Create a set called vehicles with values {"car", "bike", "bus", "train"}. Find out how 
	many items are in the set and print the result.

"""


"""
SOLUTIONS:

"""
#1.
fruits = {"air", "water", "food"}
is_in_fruits = "food" in fruits
print(f"it is {is_in_fruits} that 'food' is in fruits")  # Output: True

#3.
animals = {"cat", "dog", "rabbit"}
animals.update(["horse", "sheep"])

print(f"animals: {animals}")

#5.
cities = {"New York", "Los Angeles", "Chicago"}
cities.discard("Houston")

#7.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
res_set = set1.union(set2)
print(f"res_set: {res_set}")

#9.
prime_numbers = {2, 3, 5, 7}
prime_numbers.add(11)
print(f"prime_numbers: {prime_numbers}")

#11.
vowels = {"a", "e", "i", "o", "u"}
vowels.clear()
print(f"vowels: {vowels}")

#13.
tech_brands = {"Apple", "Google", "Microsoft"}
tech_brands.update({"Amazon", "Facebook"})
print(f"tech_brands: {tech_brands}")

#15.
numbers_list = [1, 2, 3, 4, 4, 5, 5]
numbers_set = set(numbers_list)
print(f"numbers_set: {numbers_set}")

#17.
vehicles = {"car", "bike", "bus", "train"}
vehicles_count = len(vehicles)
print(f"vehicles count is : {vehicles_count}")
