# this function take three arguments string,position,character and it replace character in in specific position in string
def replace_character_in_specific_position_in_string(string, position, character):
    # convert string into list to make it mutable
    temp_list = list(string)
    # take a position to replace the character into this position
    temp_list[position] = character
    # join the list to return it back to string
    string = "".join(temp_list)
    return string


print(replace_character_in_specific_position_in_string("abracadabra", 5, "k"))
