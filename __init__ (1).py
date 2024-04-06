consultas = []

def validar_data_hora(data, hora):
    # Aqui você pode adicionar lógica mais complexa de validação de data e hora, se necessário
    # Por simplicidade, vou apenas verificar se a data e hora são não vazias
    if data.strip() == "" or hora.strip() == "":
        return False
    return True

def marcar_consulta():
    data = input("Digite a data da consulta (DD/MM/AAAA): ")
    hora = input("Digite a hora da consulta (HH:MM): ")

    if not validar_data_hora(data, hora):
        print("Data ou hora inválida. Certifique-se de preencher ambos os campos.")
        return

    for consulta in consultas:
        if consulta["data"] == data and consulta["hora"] == hora:
            print("Essa data e hora já estão reservadas para outra consulta.")
            return

    paciente = input("Digite o nome do paciente: ")
    consultas.append({"data": data, "hora": hora, "paciente": paciente})
    print("Consulta marcada com sucesso!")

def ver_consultas():
    if not consultas:
        print("Não há consultas marcadas no momento.")
    else:
        print("Consultas marcadas:")
        for idx, consulta in enumerate(consultas, start=1):
            print(f"{idx}. Data: {consulta['data']} Hora: {consulta['hora']} Paciente: {consulta['paciente']}")

def desmarcar_consulta():
    if not consultas:
        print("Não há consultas marcadas para desmarcar.")
        return

    print("Consultas marcadas:")
    for idx, consulta in enumerate(consultas, start=1):
        print(f"{idx}. Data: {consulta['data']} Hora: {consulta['hora']} Paciente: {consulta['paciente']}")

    escolha = input("Digite o número da consulta que deseja desmarcar: ")
    try:
        idx = int(escolha) - 1
        if 0 <= idx < len(consultas):
            consultas.pop(idx)
            print("Consulta desmarcada com sucesso!")
        else:
            print("Número de consulta inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

print("Bem-vindo ao Hospital Chatbot!")

while True:
    print("O que você gostaria de fazer?")
    print("1. Marcar uma consulta")
    print("2. Ver consultas marcadas")
    print("3. Desmarcar consulta")
    print("4. Outro")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        marcar_consulta()
    elif escolha == "2":
        ver_consultas()
    elif escolha == "3":
        desmarcar_consulta()
    elif escolha == "5":
        print("Obrigado por usar o Hospital Chatbot, obrigado!")
        break
    elif escolha == "4":
        print("Certo um atendente humano sera encaminhado para ajudar em seu atendimento, obrigado!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

