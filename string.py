def count_a_in_string(s):
    return s.lower().count('a')

string = input("Informe uma string: ")
count = count_a_in_string(string)
print(f"A letra 'a' aparece {count} vezes na string '{string}'.")
