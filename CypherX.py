import base64
import urllib.parse

def encode_base64(text):
    return base64.b64encode(text.encode()).decode()

def decode_base64(text):
    return base64.b64decode(text.encode()).decode()

def encode_hex(text):
    return text.encode().hex()

def decode_hex(text):
    return bytes.fromhex(text).decode()

def encode_rot13(text):
    return text.translate(str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    ))

def decode_rot13(text):
    return encode_rot13(text)

def encode_binary(text):
    return ' '.join(format(ord(c), '08b') for c in text)

def decode_binary(binary_str):
    return ''.join(chr(int(b, 2)) for b in binary_str.split())

def encode_url(text):
    return urllib.parse.quote(text)

def decode_url(text):
    return urllib.parse.unquote(text)

def auto_detect_and_decode(text):
    try:
        decoded = decode_base64(text)
        if decoded.isprintable():
            return "Base64", decoded
    except: pass

    try:
        decoded = decode_hex(text)
        if decoded.isprintable():
            return "Hex", decoded
    except: pass

    try:
        decoded = decode_binary(text)
        if decoded.isprintable():
            return "Binary", decoded
    except: pass

    try:
        decoded = decode_url(text)
        if decoded.isprintable():
            return "URL", decoded
    except: pass

    decoded = decode_rot13(text)
    if decoded.isprintable() and decoded != text:
        return "ROT13", decoded

    return "Unknown", "Could not decode or detect encoding."

def main():
    while True:
        print("\n=== CypherX Encoder/Decoder ===")
        print("1. Encode")
        print("2. Auto Decode")
        print("0. Exit")

        choice = input("Choose action: ")
        if choice == "0":
            print("Exiting...")
            break

        text = input("Enter your text: ")

        if choice == "1":
            print("[1] Base64 [2] Hex [3] ROT13 [4] Binary [5] URL Encode")
            method = input("Choose encoding method: ")

            if method == "1":
                result = encode_base64(text)
                method_name = "Base64"
            elif method == "2":
                result = encode_hex(text)
                method_name = "Hex"
            elif method == "3":
                result = encode_rot13(text)
                method_name = "ROT13"
            elif method == "4":
                result = encode_binary(text)
                method_name = "Binary"
            elif method == "5":
                result = encode_url(text)
                method_name = "URL"
            else:
                print("Invalid method.")
                continue

            print(f"\nEncoded using {method_name}: {result}")

        elif choice == "2":
            method_name, result = auto_detect_and_decode(text)
            print(f"\nDetected Method: {method_name}\nDecoded Output: {result}")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()