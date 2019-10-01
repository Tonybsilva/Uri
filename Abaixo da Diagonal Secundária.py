operacao = input()
resultado = 0
for i in range(12):
    for j in range(12):
        n = float(input())
        if j > 11 - i:
            resultado += n
if operacao == "S":
    print("%.1f"%(resultado))
else:
    print("%.1f"%(resultado/66))
