int_list = [int(num) for num in "-1,-2,0,42,21,1,4551,-142,-2".split(",")]
print("list = ", int_list, "\n")

positive_list = [num for num in int_list if num>0]
print("positive list = ", positive_list)

square_list = [num**2 for num in int_list]
print("square list = ", square_list)

word = "orange"

vowels = "a,e,i,o,u"

vowels_list = [letter for letter in word if letter in vowels]
print(f"Vowels list from {str(word)} = {vowels_list}")

ord_values = [ord(letter) for letter in word]
print(f"Ordinal Values = {ord_values}")
