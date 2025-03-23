def vigenere_encrypt(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) - shift) % 26 + ord(base))
            key_index += 1
        else:
            result += char
    return result

if __name__ == "__main__":
    text = input("輸入要加密的文字: ")
    key = input("輸入密鑰: ")
    encrypted = vigenere_encrypt(text, key)
    print("加密後的結果:", encrypted)
    print("解密後的結果:", vigenere_decrypt(encrypted, key))
