#Beispiel 1

""" a_string = "Ich bin ein String mit 0"
a_string2 = "False"
a_string3 = ['F','a','l','s','e','0']
print(a_string, any(a_string))
print(a_string, all(a_string))
print(a_string2, any(a_string2))
print(a_string3, all(a_string3)) """


#Beispiel 2

""" a_list_of_bool = [False,False,False]
a_list_of_bool_1 = [False,False,True]
a_list_of_bool2 = [0,0,0]
a_list_of_bool2_1 = [0,0,5]

print(any(a_list_of_bool))
print(any(a_list_of_bool_1))
print(any(a_list_of_bool2))
print(any(a_list_of_bool2_1)) """


#Beispiel 3

""" an_iterable = [2,12,42,60]

a_lambda = lambda x: x % 2 == 0

result = [a_lambda(step) for step in an_iterable]


print(result)

if any(result):
    print("Mindestens eine Zahl gerade")
else:    
    print("Keine Zahl gerade")

if all(result):
    print("Alle Zahlen sind gerade") """


#Beispiel 4


""" an_iterable2 = "Nach Buchstaben suchen"

a_lambda2 = lambda x: x  == 'e'

result2 = [a_lambda2(step) for step in an_iterable2]


print(result2)

if any(result2):
    print("Mindestens ein e enthalten")
else:    
    print("Keine e enthalten") """

# Beispiel 5

liste=("manne", 1, "string")

a_lambda = lambda x: type(x)==str

result= [a_lambda(step) for step in liste]

print(result)
print(all(result))
