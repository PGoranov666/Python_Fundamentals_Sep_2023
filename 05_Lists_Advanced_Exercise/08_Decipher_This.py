def decode_secret_message(message):
    words = message.split()

    decoded_words = []
    for word in words:
        first_num_str = ''
        for char in word:
            if char.isdigit():
                first_num_str += char
            else:
                break

        if first_num_str:
            first_char = chr(int(first_num_str))
            decoded_word = first_char + word[len(first_num_str):]

            if len(decoded_word) > 2:
                second_char = decoded_word[1]
                last_char = decoded_word[-1]

                decoded_word = decoded_word[0] + last_char + decoded_word[2:-1] + second_char
                decoded_words.append(decoded_word)
            else:
                decoded_words.append(decoded_word)
        else:
            decoded_words.append(word)

    decoded_message = ' '.join(decoded_words)
    return decoded_message


secret_message = input()
decoded_message = decode_secret_message(secret_message)
print(decoded_message)
