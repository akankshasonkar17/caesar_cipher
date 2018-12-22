alphabet = 'abcdefghijklmnopqrstuvwxyz'
SPECIAL_CHARS = " ,.-;:_?!="

key = 3
newMessage = ''
Message = input('Please enter a message:')

for character in Message:
	if character in alphabet:
		position = alphabet.find(character)
		newPosition = (position +key)%26
		newCharacter = alphabet[newPosition]
		newMessage += newCharacter
	else:
		newMessage += character
print('Your new message is:',newMessage)



def find_key_from_cipher(newMessage):
    index_of_most_common_letter = 4 #Index of 'e'

    #Calculate distribution
    distribution_dict = analyse_letter_distribution(newMessage)
    #Get common letters
    common_letters = sorted(distribution_dict, key=distribution_dict.get, reverse=True)

    #Use most common letter to get key
    key = alphabet.find(common_letters[0]) - index_of_most_common_letter
    print("key is",key,"\n")
    return key

def analyse_letter_distribution(newMessage):
    distribution_dict = {}
    for letter in newMessage:
        if letter in SPECIAL_CHARS:
            continue
        if letter not in distribution_dict:
            distribution_dict[letter] = 1
        else:
            distribution_dict[letter] += 1
    if len(distribution_dict.values()) != len(distribution_dict.values()):
        print("Multiple letters appear the same amount of times! Uh oh.")
    print("distribution_dict is",distribution_dict,"\n")
    return distribution_dict



key = find_key_from_cipher(newMessage)
plainMessage = ''
for character in newMessage:
	if character in alphabet:
		position = alphabet.find(character)
		newPosition = (position -key)%26
		newCharacter = alphabet[newPosition]
		plainMessage += newCharacter
	else:
		plainMessage += character
print('Your new message is:',plainMessage)




