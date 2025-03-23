import numpy as np
#claude協助
def encrypt_hill_cipher(plaintext, key_matrix, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """
    使用希爾密碼加密明文
    
    參數:
    plaintext (str): 要加密的明文字符串
    key_matrix (numpy.ndarray): 2x2 加密鑰匙矩陣
    alphabet (str): 使用的字母表，默認為英文大寫字母
    
    返回:
    str: 加密後的密文
    """
    mod = len(alphabet)
    
    # 確保明文長度為偶數（希爾密碼以2個字符為一組進行加密）
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  # 如果長度為奇數，添加填充字符
    
    # 將明文轉換為數字 (A=0, B=1, ..., Z=25)
    plain_nums = [alphabet.index(char) for char in plaintext]
    
    # 將明文分組進行加密
    ciphertext = ""
    for i in range(0, len(plain_nums), 2):
        # 取一組兩個字符
        plain_pair = np.array([plain_nums[i], plain_nums[i+1]])
        
        # 使用鑰匙矩陣加密
        cipher_pair = np.dot(key_matrix, plain_pair) % mod
        
        # 將數字轉回字符
        ciphertext += alphabet[cipher_pair[0]] + alphabet[cipher_pair[1]]
    
    return ciphertext

def matrix_determinant_mod(matrix, mod):
    """計算矩陣在指定模數下的行列式"""
    det = int(round(np.linalg.det(matrix))) % mod
    return det

def mod_inverse(a, m):
    """計算a在模m下的乘法逆元"""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def matrix_mod_inverse(matrix, mod):
    """計算矩陣在指定模數下的逆矩陣"""
    # 計算行列式
    det = matrix_determinant_mod(matrix, mod)
    
    # 計算行列式的模乘法逆元
    det_inv = mod_inverse(det, mod)
    if det_inv is None:
        raise ValueError(f"矩陣在模{mod}下不可逆，因為行列式{det}在模{mod}下沒有乘法逆元")
    
    # 對於2x2矩陣，計算伴隨矩陣
    adj = np.zeros_like(matrix)
    adj[0, 0] = matrix[1, 1]
    adj[0, 1] = -matrix[0, 1]
    adj[1, 0] = -matrix[1, 0]
    adj[1, 1] = matrix[0, 0]
    
    # 確保所有元素都是整數且在模範圍內
    adj = adj.astype(int) % mod
    
    # 計算逆矩陣
    inv_matrix = (det_inv * adj) % mod
    
    return inv_matrix

def decrypt_hill_cipher(ciphertext, key_matrix, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """
    使用希爾密碼解密密文
    
    參數:
    ciphertext (str): 要解密的密文字符串
    key_matrix (numpy.ndarray): 2x2 加密鑰匙矩陣
    alphabet (str): 使用的字母表，默認為英文大寫字母
    
    返回:
    str: 解密後的明文
    """
    mod = len(alphabet)
    
    # 計算鑰匙矩陣的逆矩陣
    inv_key = matrix_mod_inverse(key_matrix, mod)
    
    # 將密文轉換為數字
    cipher_nums = [alphabet.index(char) for char in ciphertext]
    
    # 將密文分組並解密
    plaintext = ""
    for i in range(0, len(cipher_nums), 2):
        # 取兩個字符一組
        cipher_pair = np.array([cipher_nums[i], cipher_nums[i+1]])
        
        # 應用逆矩陣解密
        plain_pair = np.dot(inv_key, cipher_pair) % mod
        
        # 轉換回字符
        plaintext += alphabet[plain_pair[0]] + alphabet[plain_pair[1]]
    
    return plaintext

def main():
    # 明文和鑰匙矩陣
    plaintext = "WINDOW"
    key_matrix = np.array([[2, 3], [1, 3]])
    
    # 加密
    ciphertext = encrypt_hill_cipher(plaintext, key_matrix)
    
    # 輸出結果
    print(f"明文: {plaintext}")
    print(f"鑰匙矩陣:\n{key_matrix}")
    print(f"密文: {ciphertext}")
    
    # 計算過程展示
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print("\n加密計算過程:")
    for i in range(0, len(plaintext), 2):
        if i+1 < len(plaintext):
            p1, p2 = plaintext[i], plaintext[i+1]
            p1_idx, p2_idx = alphabet.index(p1), alphabet.index(p2)
            
            print(f"明文對: {p1}{p2} -> 數值: [{p1_idx}, {p2_idx}]")
            
            # 矩陣乘法
            c1 = (key_matrix[0][0] * p1_idx + key_matrix[0][1] * p2_idx) % 26
            c2 = (key_matrix[1][0] * p1_idx + key_matrix[1][1] * p2_idx) % 26
            
            print(f"  計算: [{key_matrix[0][0]}*{p1_idx} + {key_matrix[0][1]}*{p2_idx}, {key_matrix[1][0]}*{p1_idx} + {key_matrix[1][1]}*{p2_idx}] mod 26")
            print(f"  結果: [{c1}, {c2}] -> {alphabet[c1]}{alphabet[c2]}")
    
    # 解密驗證
    decrypted = decrypt_hill_cipher(ciphertext, key_matrix)
    print(f"\n解密驗證: {decrypted}")
    
    # 計算鑰匙矩陣的行列式和逆矩陣
    det = matrix_determinant_mod(key_matrix, 26)
    try:
        inv_matrix = matrix_mod_inverse(key_matrix, 26)
        print(f"\n鑰匙矩陣的行列式 (mod 26): {det}")
        print(f"鑰匙矩陣的逆矩陣 (mod 26):\n{inv_matrix}")
    except ValueError as e:
        print(f"\n無法計算逆矩陣: {e}")

if __name__ == "__main__":
    main()