import ctypes

cython_module = ctypes.CDLL('/data/data/com.termux/files/home/MR-SAHIL-CONVO/MR-SAHIL-CONVO1/convo1st.cpython-312.so')

# Available functions ko print karte hain
print(dir(cython_module))
