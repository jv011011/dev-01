animes = {
     "rezero" : {
          "nome original" : "re_zero",
          "tempo" : "50 episodios",
          "lançamento" : "2016",
          "protagonista" : "subaru natsuki",
          "autor" : "tappei nagatsuki",
     },
     "naruto" : {
          "nome original" : "naruto classico",
          "tempo" : "350 episodios",
          "lançamento" : "2006",
          "protagonista" : "naruto",
          "autor" : "masashi kishimoto",
     },
     "dragon ball" : {
          "nome original" : "dragon ball z",
          "tempo" : "1000 episodios",
          "lamçamento" : "1998",
          "protagonista" : "kakaroto",
          "autor" : "akira toriama",
     },
     "hunterxhunter" : {
          "nome original" : "hunterxhunter",
          "tempo" : "148 episodios",
          "lamçamento" : "1998",
          "protagonista" : "gon",
          "autor" : "youchiro thogashi",
     },
     "demon slyer" : {
          "nome original" : "kimetsu no yaba",
          "tempo" : "128 episodios",
          "lamçamento" : "2019",
          "protagonista" : "tanjiro",
          "autor" : "gotouge koyoharu",
     },
     "blue lock" : {
          "nome original" : "blue lock",
          "tempo" : "33 episodios",
          "lamçamento" : "2022",
          "protagonista" : "isagi",
          "autor" : "kaneshiro",
     },
     "dandandan" : {
          "nome original" : "dandaan",
          "tempo" : "9 episoios",
          "lamçamento" : "2024",
          "protagonista" : "okarum",
          "autor" : "yukinobu",
     },
     "bleach" : {
          "nome original" : "one pice",
          "tempo" : "366 episoios",
          "lamçamento" : "1997",
          "protagonista" : "ichigo",
          "autor" : "kubo tite",
     },
      "soul eater" : {
          "nome original" : "soul eater",
          "tempo" : " 50 episoios",
          "lamçamento" : "2009",
          "protagonista" : "soul",
          "autor" : "ookubo atsushi",
     },
     "boruto" : {
          "nome original" : "boruto",
          "tempo" : " 293episoios",
          "lamçamento" : "2022",
          "protagonista" : "boruto",
          "autor" : "mashashi kishimoto",
     },
}

def exibir(nome):
     if nome in animes:
          anime = animes[nome]
          print(f"nome: {nome}")
          print(f"nome original: {anime['nome original']}")
          print(f"tempo: {anime['tempo']}")
          print(f"lançamento: {anime['lançamento']}")
          print(f"protagonista: {anime['protagonista']}")
          print(f"autor: {anime['autor']}")
     else:
          print("anime nao encontrado")

nome_anime = input("digite um anime : ").lower()

exibir(nome_anime)