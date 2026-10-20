import classe_lampada

ligado = 0
desligado = 0
queimou = 0
while True:
    print("1- Ligado \n2-Desligado \n3-sair")
    estado = input("luz -> ").strip()
    referencia = classe_lampada.Lampada(estado)
    estado = int(estado)
    reg_estado = classe_lampada.Salva_registro()
    if estado == 1:
        ligado += 1
        reg_estado.registro("ligado", ligado)
        referencia.lampada_ligada()
    elif estado == 2:
        desligado += 1
        reg_estado.registro("desligado", desligado)
        referencia.lampada_desligada()
    else:
        queimou += 1
        reg_estado.registro("queimou", queimou)
        referencia.lampada_queimou()
        break