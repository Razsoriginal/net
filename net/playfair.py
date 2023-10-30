def prepare_key(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_set = set(key)
    matrix = [key]

    for char in alphabet:
        if char not in key_set:
            matrix[-1] += char
            key_set.add(char)
            if len(matrix[-1]) == 5:
                matrix.append("")

    return matrix

def find_coordinates(matrix, char):
    for row, row_data in enumerate(matrix):
        if char in row_data:
            return row, row_data.index(char)

def playfair_encrypt(plain_text, key):
    matrix = prepare_key(key)
    plain_text = plain_text.upper().replace("J", "I").replace(" ", "")
    encrypted_text = ""
    
    for i in range(0, len(plain_text), 2):
        char1, char2 = plain_text[i], plain_text[i + 1]
        row1, col1 = find_coordinates(matrix, char1)
        row2, col2 = find_coordinates(matrix, char2)
        
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]

    return encrypted_text


key = "KEYWORD"
message = "HELLO WORLD"

encrypted_text = playfair_encrypt(message, key)
print("Encrypted:", encrypted_text)

