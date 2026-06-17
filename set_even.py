#QUESTION;2
colors = {"red", "green", "blue"}
colors.add("yellow")
print(colors)

# QUESTION;4
countries = {"USA", "Canada", "Mexico"}
countries.remove("Canada")
print(countries)

#QUESTION;6
seasons = set(["Spring", "Summer", "Fall", "Winter", "Spring".split(', ')])
print(seasons)

#QUESTION;8
setA = {"a", "b", "c"}
setB = {"c", "d", "e"}
print(setA.intersection(setB))

#QUESTION;10
odd_numbers = {"1", "3", "5", "7", "9"}
odd_numbers.remove("3")
print(odd_numbers)

#QUESTION;12
letters = {"a", "b", "c"}
new_letters = {"b", "c", "d"}
print(letters.difference(new_letters))
letters = {"a", "b", "c"}
new_letters = {"b", "c", "d"}
print(letters.symmetric_difference(new_letters))

#QUESTION;14
students = {"Alice", "Bob", "Charlie", "David"}
students.remove("Charlie")
print(students)
students.remove("Eve")
print(students)

#QUESTION;16
text = "hello"
print(set(text))

#QUESTION;18
gadgets =  {"laptop", "smartphone", "tablet", "smartwatch"}
print(len(gadgets))
