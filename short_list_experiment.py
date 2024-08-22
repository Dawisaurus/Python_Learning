"""3-8. Seeing the World: Think of at least five places in the world youd like to
visit.
•	 Store the locations in a list. Make sure the list is not in alphabetical order.
•	 Print your list in its original order. Dont worry about printing the list neatly,
just print it as a raw Python list.
•	 Use sorted() to print your list in alphabetical order without modifying the
actual list.
•	 Show that your list is still in its original order by printing it.
•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
•	 Show that your list is still in its original order by printing it again.
•	 Use reverse() to change the order of your list. Print the list to show that its
order has changed."""

places_list = ['Poland', 'Croatia', 'Netherlands', 'Sweden', 'Portugal', 'Greece']
print(places_list)
print (sorted(places_list))
print (list(reversed(places_list)))

magicians = ['Alice', 'Jared', 'Domer']
for magician in magicians:
    print(magician)

numbers = list(range(0, 21, 5))
print (numbers)

squares = []
for value in range (1, 11):
    square = value ** 2
    squares.append(square)
    print (squares)

print (min(squares))
print (max(squares))
print (sum(squares))

squares = [value**2 for value in range(1, 11)]
print(squares)


for i in list(range(1, 1000000)):
    print(i)

million_numbers = list(range(1, 1000001))
print(million_numbers)