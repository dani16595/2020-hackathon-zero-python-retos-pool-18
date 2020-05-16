from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    """
    It says the result of the game
    :param player: string player's move ["Piedra", "Papel", "Tijeras"]
    :param ai: string ai's move ["Piedra", "Papel", "Tijeras"]
    :return: result ['Empate!','Ganaste!','Perdiste!']
    """
    player=player.lower()
    ai=ai.lower()
    if(player==ai):
        return "Empate!"
    else:
        if(player=="piedra"):
            if(ai=="papel"):
                return "Perdiste!"
            else:
                return "Ganaste!"
        if(player=="papel"):
            if(ai=="piedra"):
                return "Ganaste!"
            else:
                return "Perdiste!"
        if(player=="tijeras"):
            if(ai=="piedra"):
                return "Perdiste!"
            else:
               return "Ganaste!"

# Entry Point
def Game():
    #
    #
    for i in range(len(options)):
        print(str(i)+". :"+options[i])
    opcion=int(input("Elige opcion : "))
    player=options[opcion]
    ai=options[randint(0,2)]
    print(ai)
    #
    #
    
    winner = quienGana(player, ai)

    print(winner)
