def sha256(data):
    # Инициализация начальных значений
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    # Инициализация констант
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
        0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    # Преобразование сообщения в 64-битные блоки
    message_blocks = []
    for i in range(0, len(data), 64):
        block = data[i:i + 64]
        message_blocks.append(block)

    # Основной цикл хеширования
    for block in message_blocks:
        words = [0] * 64

        for i in range(16):
            if i * 4 + 3 < len(block):
                words[i] = (block[i * 4] << 24) | (block[i * 4 + 1] << 16) | (block[i * 4 + 2] << 8) | block[i * 4 + 3]

        for i in range(16, 64):
            s0 = (rotate_right(words[i - 15], 7) ^ rotate_right(words[i - 15], 18) ^ (words[i - 15] >> 3))
            s1 = (rotate_right(words[i - 2], 17) ^ rotate_right(words[i - 2], 19) ^ (words[i - 2] >> 10))
            words[i] = (words[i - 16] + s0 + words[i - 7] + s1) & 0xFFFFFFFF

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7

        for i in range(64):
            S1 = (rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25))
            ch = ((e & f) ^ ((~e) & g))
            temp1 = (h + S1 + ch + k[i] + words[i]) & 0xFFFFFFFF
            S0 = (rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22))
            maj = ((a & b) ^ (a & c) ^ (b & c))
            temp2 = (S0 + maj) & 0xFFFFFFFF

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
        h5 = (h5 + f) & 0xFFFFFFFF
        h6 = (h6 + g) & 0xFFFFFFFF
        h7 = (h7 + h) & 0xFFFFFFFF

    # Соединение хеш-значений
    hash_result = (h0 << 224) | (h1 << 192) | (h2 << 160) | (h3 << 128) | (h4 << 96) | (h5 << 64) | (h6 << 32) | h7

    return hash_result


def rotate_right(value, shift):
    return ((value >> shift) | (value << (32 - shift))) & 0xFFFFFFFF


data = b'Eat some more of these soft French buns and drink some tea'
hash_result = sha256(data)
print(hex(hash_result))
