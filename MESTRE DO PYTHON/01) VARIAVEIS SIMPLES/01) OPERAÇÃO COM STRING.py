frase = "Curso em vídeo Python"

print(frase)
print("⭐1>",frase[3:13])
print("⭐2>",frase[5:10])
print("⭐3>",frase[:13])
print("⭐4>",frase[1:15:2])
print("⭐5>",frase[1::2])
print("⭐6>",frase[::2])
print("⭐7>",frase.count("o"))
print("⭐8>",frase.count("O"))
print("⭐9>",frase.count("a"))
print("⭐10>",frase.count("A"))
print("⭐11>",frase.upper())
print("⭐12>",frase.upper().count("o"))
print("⭐13>",len(frase))
print("⭐14>",len(frase.strip()))
print("⭐15>",frase.replace("Python", "Android"))

frase = frase.replace("Python", "Windows")
print("⭐16>",frase)
print("⭐17>","Curso" in frase)
print("⭐18>",frase.find("Vídeo"))
print("⭐19>",frase.lower().find("vídeo"))
print("⭐20>",frase.split())

dividido = frase.split()
print("⭐21>",dividido[0])
print("⭐22>",dividido[2][3])