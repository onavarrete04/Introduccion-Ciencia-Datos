def solution(queries):
    contenedor = []
    respuestas = []
    cuentas = []

    for query in queries:
        if query[0] == "CREATE_ACCOUNT":
            peticion, idd, descripcion = query
            if not descripcion in cuentas:
                respuestas.append("true")
                contenedor.append(query)
                cuentas.append(query[2])

            else:
                respuestas.append("false")

    if query[0] == "DEPOSIT":
        peticion, idd, descripcion, valor = query

        if query[2] in cuentas:
            for i in range(len(contenedor)-1):
                print(contenedor[i][2])
                if contenedor[i][2] == query[2]:
                    contenedor[i].append(valor)
                    print(contenedor)
                    break

        else:
            respuestas.append("")

    elif query[0] == "PAY":
        peticion, idd, descripcion, valor = query

        for account in contenedor:
            if account[0] == idd:
                if account[2] < int(valor):
                    account[2] -= int(valor)
                    respuestas.append(str(account[2]))

                else:
                    respuestas.append("")

    return respuestas


print(solution([["CREATE_ACCOUNT", "1", "account1"],
                ["CREATE_ACCOUNT", "2", "account2"],
                ["DEPOSIT", "3", "account1", "2500"],
                ["DEPOSIT", "4", "account1", "500"],
                ["DEPOSIT", "5", "account2", "1000"]]))
