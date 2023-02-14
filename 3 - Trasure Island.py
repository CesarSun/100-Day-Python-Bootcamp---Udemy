def validate_input(message, options):
    """
    Valida e retorna a entrada do usuário.
    :param message: str: A mensagem para ser exibida ao usuário.
    :param options: list: As opções válidas de entrada.
    :return: str: A opção selecionada pelo usuário.
    """
    while True:
        user_input = input(message).strip().lower()
        if user_input in options:
            return user_input
        else:
            print(f"Entrada inválida. As opções válidas são {options}")


print('Bem-vindo à Ilha do Tesouro!')
print('Sua missão é encontrar o tesouro.')

direction_options = ['esquerda', 'direita']
direction_choice = validate_input('Você está em uma encruzilhada. Para onde deseja ir? Digite "esquerda" ou "direita": ', direction_options)

if direction_choice == 'direita':
    print("Fim de Jogo")
else:
    lake_options = ['esperar', 'nadar']
    lake_choice = validate_input("Você chegou a um lago. Há uma ilha no meio do lago. Digite 'esperar' para esperar por um barco. Digite 'nadar' para nadar até a ilha: ", lake_options)

    if lake_choice == 'nadar':
        print("Fim de Jogo")
    else:
        door_options = ['vermelho', 'amarelo', 'azul']
        door_choice = validate_input("Você chegou à ilha ileso. Há uma casa com 3 portas, uma vermelha, uma amarela e uma azul. Qual cor você escolhe? Digite 'vermelho', 'amarelo' ou 'azul': ", door_options)

        if door_choice == 'vermelho':
            print("Fim de Jogo")
        elif door_choice == 'azul':
            print("Fim de Jogo")
        else:
            print("Parabéns! Você encontrou o tesouro e ganhou o jogo!")
