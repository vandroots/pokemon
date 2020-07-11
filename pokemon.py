

pokemons = [
  {
    "Pokemon": "Zubat",
    "HP": 40,
    "Attack": 45,
    "Defense": 35,
    "Sp. Attack": 30,
    "Sp. Defense": 40,
    "Speed": 55,
    "Total": 245,
    "Average": 40.83
  },
  {
    "Pokemon": "Arbok",
    "HP": 60,
    "Attack": 95,
    "Defense": 69,
    "Sp. Attack": 65,
    "Sp. Defense": 79,
    "Speed": 80,
    "Total": 448,
    "Average": 74.67
  },
  {
    "Pokemon": "Pikachu",
    "HP": 35,
    "Attack": 55,
    "Defense": 40,
    "Sp. Attack": 50,
    "Sp. Defense": 50,
    "Speed": 90,
    "Total": 320,
    "Average": 53.33
  },
  {
    "Pokemon": "Psyduck",
    "HP": 50,
    "Attack": 52,
    "Defense": 48,
    "Sp. Attack": 65,
    "Sp. Defense": 50,
    "Speed": 55,
    "Total": 320,
    "Average": 53.33
  },
  {
    "Pokemon": "Poliwrath",
    "HP": 90,
    "Attack": 95,
    "Defense": 95,
    "Sp. Attack": 70,
    "Sp. Defense": 90,
    "Speed": 70,
    "Total": 510,
    "Average": 85
  },
  {
    "Pokemon": "Abra",
    "HP": 25,
    "Attack": 20,
    "Defense": 15,
    "Sp. Attack": 105,
    "Sp. Defense": 55,
    "Speed": 90,
    "Total": 310,
    "Average": 51.67
  },
  {
    "Pokemon": "Kadabra",
    "HP": 40,
    "Attack": 35,
    "Defense": 30,
    "Sp. Attack": 120,
    "Sp. Defense": 70,
    "Speed": 105,
    "Total": 400,
    "Average": 66.67
  },
  {
    "Pokemon": "Alakazam",
    "HP": 55,
    "Attack": 50,
    "Defense": 45,
    "Sp. Attack": 135,
    "Sp. Defense": 95,
    "Speed": 120,
    "Total": 500,
    "Average": 83.33
  },
  {
    "Pokemon": "Machop",
    "HP": 70,
    "Attack": 80,
    "Defense": 50,
    "Sp. Attack": 35,
    "Sp. Defense": 35,
    "Speed": 35,
    "Total": 305,
    "Average": 50.83
  },
  {
    "Pokemon": "Victreebel",
    "HP": 80,
    "Attack": 105,
    "Defense": 65,
    "Sp. Attack": 100,
    "Sp. Defense": 70,
    "Speed": 70,
    "Total": 490,
    "Average": 81.67
  }
]

pokemom = ""
while(pokemom!="S"):
    pokemom = input("Qual pokémon você deseja checar? Tecle [S] para sair")

    for poke in pokemons:
      if(poke["Pokemon"]==pokemom):

        print("Nome: "+poke["Pokemon"])
        print("HP: "+str(poke["HP"]))

        print("Attack: "+str(poke[ "Attack"]))
        if(poke[ "Attack"]>150):
          print("EXTREMAMENTE PERIGOSO")

        print("Defense: "+str(poke["Defense"]))
        print("Sp. Attack: "+str(poke["Sp. Attack"]))
        print("Sp. Defense: "+str(poke["Sp. Defense"]))
        print("Speed: "+str(poke["Speed"]))
        print("Total: "+str(poke["Total"]))
        print("Average: "+str(poke["Average"]))

        if(poke["Average"]<40):
          print("Fraco")
        elif(poke["Average"]<80):
          print("Médio")
        else:
          print("Forte")

print("Fim do programa")
    
