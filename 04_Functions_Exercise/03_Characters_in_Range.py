def all_characters(char1:str, char2:str) -> list:
    characters = []
    for current_character in range(ord(char1)+1, ord(char2)):
        characters.append(chr(current_character))
    return characters

character1 = input()
character2 = input()

final_result = all_characters(character1, character2)
print(" ".join(final_result))
