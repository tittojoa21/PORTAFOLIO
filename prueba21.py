# definir una funcion que reciba un string y devuelva un string codificado
# definir una funcion que reciba un string codificado y devuelva un string decodificado

def codifystring(strl :str) -> str:
    strl = strl.replace("a", "4")
    strl = strl.replace("e", "3")
    strl = strl.replace("i", "1")
    strl = strl.replace("o", "0")
    strl = strl.replace("u", "9")
    return strl
def decodifystring(strl :str) -> str:
    strl = strl.replace("4", "a")
    strl = strl.replace("3", "e")
    strl = strl.replace("1", "i")
    strl = strl.replace("0", "o")
    strl = strl.replace("9", "u")
    return strl

palabra = input("Ingresa una palabra: ")
codificada = codifystring(palabra)
print(f"Palabra codificada: {codificada}")
print(f"Palabra decodificada: {decodifystring(codificada)}")
