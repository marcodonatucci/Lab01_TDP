import random


def leggi_domande(file):
    f = open(file, 'r', encoding='UTF-8')
    line = f.readline()
    domande = []
    while len(line) > 0:
        try:
            testo = line
            livello = f.readline()
            risposta_esatta = f.readline()
            risposta1 = risposta_esatta
            risposta2 = f.readline()
            risposta3 = f.readline()
            risposta4 = f.readline()
            vuoto = f.readline()
            line = f.readline()
            domanda = Domanda(testo, int(livello), risposta_esatta, risposta1, risposta2, risposta3, risposta4)
            domande.append(domanda)
        except StopIteration:
            domanda = Domanda(testo, int(livello), risposta_esatta, risposta1, risposta2, risposta3, risposta4)
            domande.append(domanda)
    f.close()
    return domande


def leggi_player(file):
    f = open(file, 'r', encoding='UTF-8')
    line = f.readline()
    player_return = {}
    while len(line) > 0:
        campi = line.split(" ")
        name = campi[0]
        punti = int(campi[1])
        player1 = Player(name, punti)
        player_return[name] = punti
        line = f.readline()
    f.close()
    return player_return


class Domanda:

    def __init__(self, testo, livello, risposta_esatta, risposta1, risposta2, risposta3, risposta4):
        self.testo = testo
        self.livello = livello
        self.rispostaEsatta = risposta_esatta
        self.risposte = [risposta1, risposta2, risposta3, risposta4]


class Player:
    def __init__(self, name, punteggio):
        self.name = name
        self.punteggio = punteggio


class Game:

    def __init__(self):
        self.domande = leggi_domande("domande.txt")
        self.risposta_corretta = 0
        self.players = leggi_player("punti.txt")

    def proponi_domanda(self, livello):
        while True:
            domanda = random.choice(self.domande)
            if domanda.livello == livello:
                risposte = domanda.risposte
                random.shuffle(risposte)
                self.risposta_corretta = risposte.index(domanda.rispostaEsatta) + 1
                risposte[3] = risposte[3][:-1]
                return f"Livello {livello}) {domanda.testo}1. {risposte[0]}2. {risposte[1]}3. {risposte[2]}4. {risposte[3]}"

    def livello_massimo(self):
        livelli = []
        for d in self.domande:
            livelli.append(d.livello)
        livello_massimo_ = max(livelli)
        return livello_massimo_

    def aggiorna_player(self, nome, pt, file):
        if self.players.__contains__(nome):
            self.players[nome] = pt
        player2 = Player(nome, pt)
        self.players[nome] = pt
        sorted_players = sorted(self.players, key=self.players.get, reverse=True)
        f = open(file, 'w', encoding='UTF-8')
        for n in sorted_players:
            f.write(f"{n} {self.players[n]}\n")


game = Game()
livello_massimo = game.livello_massimo()
for i in range(0, livello_massimo + 1):
    print(game.proponi_domanda(i))
    risposta = int(input("Inserisci la risposta: "))
    if risposta == game.risposta_corretta:
        print("Risposta corretta!\n")
    else:
        print(f"Risposta sbagliata! La risposta corretta era: {game.risposta_corretta}")
        nickname = input(str("Inserisci il tuo nickname: "))
        game.aggiorna_player(nickname, i, 'punti.txt')
        exit()
nickname = input(str("Inserisci il tuo nickname: "))
game.aggiorna_player(nickname, 4, 'punti.txt')
