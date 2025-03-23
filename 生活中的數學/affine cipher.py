def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr(((a * (ord(char) - ord(base)) + b) % 26) + ord(base))
        else:
            result += char
    return result

def affine_decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("a 和 26 不是互質，無法解密")
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((a_inv * (ord(char) - ord(base) - b) % 26) + ord(base))
        else:
            result += char
    return result

if __name__ == "__main__":
    text = input("輸入要加密的文字: ")
    a = int(input("輸入 a (須與 26 互質): "))
    b = int(input("輸入 b: "))
    encrypted = affine_encrypt(text, a, b)
    print("加密後的結果:", encrypted)
    print("解密後的結果:", affine_decrypt(encrypted, a, b))