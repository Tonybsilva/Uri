n = int(input())
y = []
for i in range(n):
    h_inicio,h_fim = map(int,input().split())
    y.append((h_fim,h_inicio))
y.sort()
consultas = 1
ultima_selecionada = y[0][0]
for i in range(1,n):
    if ultima_selecionada <= y[i][1]:
        consultas += 1
        ultima_selecionada = y[i][0]
print(consultas)
