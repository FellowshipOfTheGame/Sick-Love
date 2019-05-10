# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label sofiaseconddate:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with Fade(0.7,0.2,0.7)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Terminei! Esse também foi intenso! Caramba, nunca pensei que fosse possível sentir medo lendo um livro."
    
    "Desde minha primeira visita na biblioteca eu virei fã de contos de terror, e agora eu terminei o último conto de Lovecraft que faltava, \"A Sombra Vinda do Tempo\"."
    
    "Foi um dos melhores dele. Acho que não senti tantos calafrios enquanto lia em nenhum outro."
    
    "Eu preciso agradecer a Sofia pelas recomendações. Nunca achei que eu ia gostar tanto de livros de Horror."
    
    "Já tá meio tarde. Será que eu mando mensagem agora? Será que ela deixa as coisas no silencioso antes de dormir?"
    
    "Eu sempre coloco porque o {i}spam{/i} é real nos grupos, mas e se eu acordar ela? Huuum, melhor esperar amanhã. Não quero que ela me odeie pro resto da vida."
    
    "É. Acho que vou dormir. Não é como se eu estivesse levemente apreensivo por ler um livro sobre criaturas de outra dimensão que podem te deixar louco só de pensar nelas."
    
    "Com certeza não. Quem ficaria com medo de um livro. Que absurdo..."
    
    # TODO: Tela preta - barulho de energia apagando
    
    p "Mas que diabos! Acabou a luz? BEM AGORA? SÉRIO!?"
    
    p "Só me faltava essa. Tem curso de engenharia elétrica na universidade e ninguém tem a capacidade de fazer manutenção na rede elétrica e não sobrecarregar o transformador."
    
    p "Não vou nem começar a falar do {i}wifi{/i}..."
    
    # TODO: Som de vento creepy
    
    "... Ok... Eu acho que vou mandar uma mensagem pra Sofia. Não por estar com medo. Com certeza não. É pra passar o tempo..."
    
    "Pior que vou ter que usar o 3G. Triste a vida."

    p "Opa! Ela respondeu."
    
    "{i}- Algumas mensagens depois -{/i}"
    
    p "Esse final de semana você vai estar livre? Eu estava pensando em ir pra algum lugar e a gente pode trocar uma ideia sobre livros, a vida, o universo e tudo mais."

    s "*risos* Gostei da referência. Eu estava querendo ir ver uma exposição temática de terror no museu. Disseram que está muito boa. Quer ir?"

    p "Claro! Não costumo ir em museus, mas depois das suas ótimas recomendações de livro, vou arriscar. Vai ver descubro mais uma coisa que eu gosto e nunca iria imaginar."
    
    p "E no pior dos casos, vai ter você pra conversar, então está ótimo!"
    
    s "Perfeito! Só não vale me culpar depois se você se apaixonar por esculturas grotescas."
    
    p "*risos* Pode deixar."

    "{i}- Algumas despedidas depois e a conversa chega ao fim -{/i}"

    "Ok, eu acho que estou mais calmo agora. Vou conseguir dormir tranquilo..."
    
    p "{i}PERA!{/i}"
    
    p "Eu acabei de marcar um encontro com uma garota?" 
    
    "Será que isso é um encontro? Eu não pensei direito porque eu {i}tava{/i} nervoso com a falta de luz e o livro..."
    
    "Caramba. Será que ela acha que eu gosto dela? Será que ela acha que é um encontro?"
    
    "Aliás... Eu gosto dela? Digo, ela é bonita e inteligente. E gosta de ler também..."
    
    "Ah, pronto. Agora sim que eu não vou dormir. Por que eu fui pensar nisso agora?"
    
    "{i}- No fim de semana -{/i}"
    
    #TODO mudar pro cenário do museu (ou do ponto de encontro)
    
    "Ufa, finalmente cheguei no museu. Será que a Sofia já chegou?"
    
    show sofia happy at noghost
    
    s "Oi! povname, {i}tô{/i} aqui!"
    
    p "Opa! Tudo bom? Faz tempo que você chegou? Desculpa se atrasei."
    
    show sofia standing at noghost
    
    s "Eu cheguei agora a pouco, não esquenta."
    
    s "E aí, preparado pra ver algumas coisas macabras?"
    
    p "{i}Bora{/i}! Eu nunca ia imaginar que tinham exposições de coisas de horror. Estou curioso com o que tem aqui dentro."
    
    s "Pelo que eu li parece que tem um pouco de tudo. Alguns quadros e esculturas, um estande de livros, posteres de filmes, algumas trivias sobre autores e diretores..."
    
    p "Legal! Onde você quer ir primeiro?"
    
    show sofia evasive at noghost
    
    s "Bem, vou deixar os livros pra depois... provavlemente eu vou comprar alguma coisa e não quero ficar carregando sacolas pro resto do dia..."
    
    show sofia standing at noghost
    
    s "Você gosta dos filmes do Tom Barton?"
    
    p "Claro! Eu vi quase todos os filmes dele. Eu amo ele desde que vi \"O Estranho Mundo de Jacó\" quando eu era pequeno."
    
    show sofia happy at noghost
    
    s "Falaram que tem bastante coisas dele na parte de filmes. {i}Bora{/i} lá!"
    
    hide sofia happy
    
    " - {i}Na seção de filmes{/i} - "
    
    p "Caramba! Tem um monte de desenhos do Tom aqui. Os traços dele são tão únicos."
    
    p "Olha lá, tem até alguns modelos das expressões do Jacó Esqueletom no filme!"
    
    show sofia happy at noghost
    
    s "Sim! E olha ali, tem os bonequinhos de pano daquele filme dele, o 8+1. Eles são muito fofos!"

    show sofia standing at noghost

    p "Nossa, finalmente encontrei alguém que assistiu esse filme. Eu achei que só eu tinha visto. Era tão bonito, mas não tinha ninguém pra conversar sobre!"
    
    s "Eu também não conhecia quase ninguém que tinha visto. Acho que é porque não tem tanta pegada macabra que nem o Tom costuma fazer. E não teve muita divulgação na época... Mas eu gostei da história."
    
    p "Verdade. Acho que os que os mais conhecidos dele são o \"Jacó\", \"A Zumbi que ia Casar\" e os filmes da \"Clarice\". Mas ele tem outros filmes bem legais."

    s "Realmente. Você já viu o..."
    
    #Tela preta pra transição?
    " - {i} Depois de alguns minutos de discussão de filmes, nós fomos para a seção de jogos a pedido meu.{/i}- "
    
    p "Uau, tem até jogos em Realidade Virtual pra jogar! Disseram que o \"Resident Bad\" tá dando um certo medo... Nossa, tem até o \"Four Nights At Franks'\" que nem saiu. Esse deve assustar pra caramba!"

    show sofia standing at noghost

    s "Acho que alguém gosta bastante de jogos..."

    p "Sim. Eu até que jogo bastante coisa. Você não gosta?"
    
    s "Huuum, nunca joguei muito, mas é mais por preferir ler do que não gostar. Não estou te julgando, fica tranquilo."
    
    p "Ufa! Menos mal. Mas acho que você devia tentar jogar alguns jogos mais focados em história. Talvez você goste. Tem alguns muito envolventes."
    
    p "Tem alguns de terror inclusive que são baseados nos livros do \"Lovecraft\". Mas nesse caso eu gostei mais dos livros."
    
    p "Vamos jogar alguns dos jogos aqui! Certeza que você vai gostar de algum deles."
    
    s "Tudo bem. Vou dar uma segunda chance."
    
    #Tela preta pra transição?
    " - {i} Depois de alguns longos minutos e alguns sustos jogando, Sofia mudou um pouco de opinião sobre jogos. E então, seguimos para a seção de livros.{/i}- "

    show sofia upset at noghost

    s "Ok, eu admito que levei alguns sustos..." 
    
    show sofia standing at noghost
    
    s "Foi mais legal do que eu imaginava. Alguns deles pareciam ter uma história bem legal."
    
    p "Fico feliz que mudou de ideia. Jogos são bem parecidos com livros. São só uma forma mais interativa de contar histórias. E muitas vezes de jeitos bem inusitados."
    
    p "Inclusive, acho que você devia dar uma olhada depois na história do \"Four Nights At Franks'\". O jogo em si quase não conta nada, diretamente. Mas a franquia tem uma história gigante."
    
    p "E está tudo escondido dentro do jogo e em brincadeiras que o autor faz no site. Deixando um monte de pistas criptografadas em lugares inusitados. É como viver uma história de detetiva na vida real. Mas não vou dar spoilers..."

    s "Poxa. Interessante. Vou procurar depois. Pareceu algo bem legal. Eu já vi alguns livros que você tem que solucionar quebra-cabeças na página atual pra desbloquear a próxima. Achei bem criativo e inusitado."

    p "Não sabia desse livro não. Vou dar ver se encontro mais tarde."
    
    s "Hey, esses estandes de livros parecem bem interessantes, {i}hein{/i}? Já terminou todos os de {i}Lovecraft{/i}?"
    
    p "Acho que já. Acabei gostando tanto que li bem mais rápido do que costumo ler. Obrigado, de novo, pelas recomendações. Tive muita sorte de te conhecer aquele dia na biblioteca."

    show sofia shy at noghost

    s "Poxa, obrigada. Mas nem foi tanta coisa assim... Só umas recomendações de livros que eu gosto."
    
    p "Claro que foi importante! Eu não conhecia quase ninguém aqui e estava nervoso com o começo da faculdade e os trabalhos."
    
    p "E aí eu conheci uma pessoa que além de me recomendar vários livros bons que me ajudaram a desestressar de todo o clima tenso da faculdade, é super legal de conversar e {i}tá{/i} aqui me fazendo companhia no final de semana."
    
    s "Hehe... Falando assim eu até fico envergonhada. Mas obrigada. Eu também fiquei feliz de ter conhecido você. Não tenho muitos contatos na faculdade. Muito menos que gostem de ler e que eu possa conversar assim tão fácil..."
    
    "Poxa, ela fica muito fofa sem graça assim... Mas eu não sei muito o que dizer agora... Não sou muito bom nessas situações... Mas ela é uma garota realmente interessante. Será que eu tenho alguma chance com ela?"
    
    show sofia happy at noghost
    
    s "Epa! Esse livro é o novo de um autor que eu gosto bastante. Até esqueci que já tinha lançado. Acho que eu vou levar."
    
    show sofia standing at noghost
    
    p "Huuum... acho que vou levar também. Suas recomendações não me decepcionaram até hoje. E, além disso, vamos poder discutir o livro conforme formos lendo."

    show sofia happy at noghost

    s "Gostei da ideia! Sempre fico com vontade de discutir o que eu estou lendo com os outros, mas é difícil arrumar companhia."
    
    s "Vamos dar uma olhada nos outros livros também. Aproveito e te recomendo mais alguns se você quiser."
    
    show sofia standing at noghost
    
    p "Claro! Vamos lá."
    
    " - {i} Depois de uma busca incessante por livros e a compra de livros que possivelmente ficarão na estante antes de serem lidos por mais tempo do que você gostaria de admitir, termina o evento. {/i} "
    
    p "Bem, hora de ir. Obrigado por ter saído comigo. Me diverti bastante hoje!"
    
    show sofia shy at noghost
    
    s "Eu que agradeço por ter me convidado e aceitado vir aqui. Me diverti bastante também."
    
    show sofia standing at noghost
    
    p "Que bom que gostou. Aliás, eu preciso te apresentar uns jogos de terror pra ver se você gosta de algum. Um dia desses te chamo para jogar lá em casa."
    
    s "Tudo bem. Vou dar uma outra chance para os jogos. Preciso ver depois aqueles que você comentou. Bem, vou indo nessa. A gente vai conversando sobre o livro, beleza? Tchau!"
    
    p "Tchau! Até a próxima!"
    
    "Ok. Esse foi um fim de semana divertido. Preciso chamar a Sofia para sair mais vezes, ela é uma pessoa muito legal."
    
    "Bem, {i}bora{/i} pra casa. O {i}rolê{/i} foi divertido mas deu uma {i}baita{/i} canseira ficar o dia todo andando de um lado pro outro. Vou chegar em casa, tomar um banho, comer alguma coisa e dormir..."
    
    "AH NÃO! TEM SEMINÁRIO PRA APRESENTAR AMANHÃ!"
    
    "Droga. Eu nem comecei. Ok, essa noite vai ser longa..."
    
    # This ends the game.

    return
