def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    text = input("輸入要加密的文字: ")
    shift = int(input("輸入位移量: "))
    encrypted = caesar_encrypt(text, shift)
    print("加密後的結果:", encrypted)
    print("解密後的結果:", caesar_decrypt(encrypted, shift))