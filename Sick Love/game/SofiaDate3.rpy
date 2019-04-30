# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label sofiathirddate:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with Fade(0.7,0.2,0.7)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    "Caramba, acho que finalmente vou ter um tempo pra viver agora que essa leva de provas e trabalhos acabou. Vida de universitário não é nada fácil."

	"Acho que aquela galera que ficava me falando no colegial que tudo ia ser festa e felicidade depois que eu passasse na faculdade devia ser processada por calúnia..."
	
	"Bem, vamos ver se temos alguma novidade interessante do mundo lá fora. Faz um tempo que não vejo se saiu alguma coisa nova."
	
	"Huuum... {i}tretas{/i} sobre jogos com microtransação... Nenhuma novidade aqui. Mais {i}tretas{/i} de {i}crunch time{/i} em empresas de jogos... Nada novo também."
	
	"Saiu mais um {i}Murder's Creed{/i}... Também não é novidade alguma... {i}PERA!{/i} Ninguém reclamou de estar cheio de {i}bugs{/i} esse daí? Ok, isso sim é uma novidade."
	
	"Huuum... Olha só, vai estrear no cinema, nesse final de semana, a adaptação pra filme do {Four Nights at Frank's}{/i}... A Sofia disse que gostou dos livros que fizeram sobre o jogo, talvez ela goste do filme também."
	
	p "Vou mandar uma mensagem pra ela, ver se ela está livre no final de semana."
	
	#TODO transição pra tela de celular?
	
	" - {i} Algumas mensagens depois {/i}- "
	
	s "Eu vou estar livre, sim! Finalmente as minhas provas também acabaram (por enquanto). Pelo {i}trailer{/i} parece que não vai ser tão ruim assim. Digo, normalmente adaptações de livros costumam ser bem tristes de ver."
	
	s "Especialmente depois que a gente já leu o livro e vai no {i}hype{/i} pro cinema esperando que eles vão ser fiéis o suficiente para pelos menos contar a mesma história do livro..."
	
	p "Eu te entendo... Com jogos é até pior. A maioria dos filmes não chega a passar nem a mesma ideia geral do que o jogo é. Esses dias eu vi o {i}trailer{/i} do filme do {i}Zomik{/i} que vai sair e quase infartei de tanta tristeza."
	
	p "Mas, então, posso confirmar o filme?"
	
	s "Claro! Só não vai pular no meu colo se ficar com muito medo. *risos*"
	
	p "{i}Oloco{/i}!E esse {i}bullying{/i} gratuito aí? Nem tive que discar {i}0800{/i} pra receber. Vou me lembrar disso se um dia você vier aqui jogar os jogos do {i}Four Nights at Frank's{/i}. Não terá clemência quando você pular com os sustos. *risos*"
	
	s "Tudo bem, eu deixo você segurar minha mão se ficar com medo, não vou ser tão cruel... Mas, ou, povname, vou ter que dar uma saída daqui. Vou ficar um tempo sem responder. Em todo caso, até o filme!"
	
	" - {i} Algumas despedidas depois {/i}- "
	
	"{i}YES{/i}! Ela {i}topou{/i} ir... Ok, eu acho que posso dizer que estou gostando dela mesmo. Não é normal ficar feliz assim quando uma garota que você não sente nada por aceita sair com você."
	
	"Aliás... eu fiz de novo, né? Marquei um encontro e nem percebi. Eu não sei se estou ficando muito bom no flerte ou se estou ficando cada dia mais {i}tapado{/i}..."
	
	p "Triste a vida..."
	
	"Mas e aquela história de segurar na mão? Será que foi uma indireta? Será que ela também gosta de mim? Será que vai rolar alguma coisa no filme?"
	
	p "AAAAAAAH eu não vou conseguir dormir direito pensando nisso. DE NOVO!"
	
	p "Ok, respira fundo, povname. Vai fazer alguma coisa pra distrair a cabeça. Você consegue..."
	
	"Já sei, vou ler um livro."
	
	" - {i} Depois de tentar ler em vão, ver séries das quais ele nem lembra mais o que assistiu e jogar um pouco, o sono chega, assim como o grande momento no final de semana. {/i}- "
	
	#TODO carregar cena do cinema
	
	p "Caramba, eu fiquei tão ansioso que acabei chegando um pouco antes. Pelo menos já comprei os ingressos..."
	
	s "Oi, povname, cheguei!"
	
	p "Oi, Sofia! Tudo bem?"
	
	s "Tudo, e você? Te fiz esperar muito?"
	
	p "Não, tá tranquilo. Eu aproveitei e já comprei os ingressos."
	
	s "Poxa, valeu! Então eu compro a pipoca pra gente dividir."
	
	p "Beleza. {i}Bora{/i} lá!"
	
	" - {i} No filme... {/i}- "
	
	"Huuum... o filme até que ficou legal. "
	
	#Finish
	return 