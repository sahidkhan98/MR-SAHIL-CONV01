import ctypes

# Absolute path se Cython .so file ko load karte hain
cython_module = ctypes.CDLL('/data/data/com.termux/files/home/MR-SAHIL-CONVO/MR-SAHIL-CONVO1/convo1st.cpython-312.so')  # Correct file path

# Agar Cython code mein `greet` function hai
cython_module.greet.argtypes = [ctypes.c_char_p]  # Function ka argument type define karna
cython_module.greet.restype = ctypes.c_char_p  # Agar function string return karta hai

# Function ko call karte hain, example: "Sahil" ko pass kar rahe hain
result = cython_module.greet(b"Sahil")  # Function ko call karte hain (byte string pass karna zaroori)

# Result ko print karte hain
print(result.decode())  # Agar result byte string hai, toh decode karke print karte hain
