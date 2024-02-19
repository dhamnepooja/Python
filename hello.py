#ask user for their name strip and capitalize
name= input("whats ur name? ").strip().title()

#Split users name into first name and last name
first, last = name.split(" ")

#Say hello to user
print(f"hello , {first}")



