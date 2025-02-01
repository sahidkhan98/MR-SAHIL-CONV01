import ctypes

# Cython .so file ko load karna
cython_module = ctypes.CDLL('/path/to/your/convo1st.cython-312.so')  # .so file ka actual path dena

# Agar Cython code mein `greet` naam ka function hai jo ek string accept karta hai
cython_module.greet.argtypes = [ctypes.c_char_p]  # Function ka argument type define karna
cython_module.greet.restype = ctypes.c_char_p  # Agar function string return karta hai

# Function ko call karte hain, example: "Sahil" ko pass kar rahe hain
result = cython_module.greet(b"Sahil")  # Function ko call karte hain (byte string pass karna zaroori)

# Result ko print karte hain
print(result.decode())  # Agar result byte string hai, toh decode karke print karte hain
