# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label sofiafirstdate:

    $ nDatesSofia+=1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg campus
    with Fade(0.7,0.2,0.7)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Bem, já que não trouxe muita coisa comigo pro dormitório, acho que a melhor coisa que posso fazer pra passar o tempo é pegar um bom livro."

    "Será que aqui na biblioteca tem só livros técnicos? Seria bom se desse para pegar alguns livros mais divertidos às vezes..."
    
    "Falaram que era só atravessar a praça, subir umas escadas, seguir reto e procurar um prédio à direita cheio de janelas para chegar na biblioteca."
    
    scene black with Fade(0.7,0.2,0.7)

    "-{i}Depois de andar muito...{/i}-"
    
    scene bg campus
    with Fade(0.7,0.2,0.7)
    
    "Huuum... acho que é aquele prédio ali. Uau! Que prédio grande! Deve ser umas 5 vezes maior que a biblioteca da minha escola."
    
    "Caramba, qual o problema do pessoal dessa universidade que não coloca placas com direções e nem com o nome dos prédios em um lugar visível?"
    
    "Quando me falaram que a universidade era um lugar que amadurece as pessoas eu não imaginei que parte do amadurecimento era aprender a adivinhar onde ficam coisas má sinalizadas..."
    
    if nDatesRafaela > 0:
        "E eu achando que ia ser fácil que nem achar o ginásio..."
    
    "É aqui mesmo. Ufa! Beleza, agora é sair procurando o que tem em cada seção..."
    
    scene bg library
    with Fade(0.7,0.2,0.7)
    
    "Caramba! Quanto livro de cálculo. Deve ter livro aqui de uns 100 anos... Tenho dó de quem tem rinite."
    
    "*suspiro* Pior que o professor já passou lista de exercício. E mal começaram as aulas... Preciso ver depois quais os livros que ele vai usar e reservar aqui."
    
    "Tem uma seção só de publicação científica. Será que alguém pega pra ler algo daqui?"
    
    "Olha só, aparentemente tem livros de ficção! Finalmente encontrei o que eu procurava. Hum..."
    
    "\"Senhor dos Anéis\" eu já tentei ler. Mas aquelas árvores genealógicas infinitas e dezenas de páginas descrevendo toda a família de cada personagem novo me desanimaram."
    
    "Os filmes são muito bons, pelo menos..."
    
    "\"Eu, Robô\" é bem legal. Eu gosto bastante das discussões filosóficas sobre tecnologia do Asimov."
    
    "\"A Torre Negra\"... Nossa, esse é bem legal, apesar de super grande com aqueles 7 volumes um maior que o outro... {i}Pera{/i}, se tem {i}King{/i} aqui eu to na seção de terror, então."
    
    "Nossa, tem terror aqui também, que inusitado. Nada como estudar numa universidade com cursos que estudam literatura."
    
    "Caramba, {i}Lovecraft{/i}! Eu lembro de alguns jogos que fazem referência aos livros dele. Pareciam bem aterrorizantes..."
    
    "... E tinham uns memes na internet sobre aquele monstro dele. Como chamava mesmo aquele monstro?"
    
    p "Huuum... aquele monstro famoso de Lovecraft..."
    
    p "Claudio? Cleber?"
    
    show sofia happy at noghost
    
    s "*risos* {i}Cthulhu{/i}?"

    p "Isso! {i}Pera{/i}, oi?"

    show sofia standing at noghost

    s "Oi. Desculpa se te assustei. É que ouvi você murmurando e respondi por impulso."
    
    p "Não... Relaxa. Eu que não percebi que estava falando sozinho. Foi mal."
    
    p "E obrigado por me ajudar a lembrar. Eu {i}tava{/i} procurando algum livro legal e lembrei que eu já tinha ouvido falar bastante do {i}Lovecraft{/i}, mas não lembrava o nome do monstro."
    
    s "Fica tranquilo. Eu também falo sozinha às vezes. E não é como se você tivesse falado errado o nome dele."
    
    p "Como assim? Não é {i}Cthulu{/i}, que nem você falou agora? Como que eu acertei falando Cleber?"
    
    show sofia happy at noghost

    s "É só uma brincadeira. O nome do monstro é impronunciável pelos humanos, então a gente nunca vai acertar o nome dele. Inclusive tem vários jeitos de falar e escrever o nome \"correto\"."
    
    show sofia standing at noghost
    
    s "Katulu, Kutulu, Tulu... Então no fim você não {i}tá{/i} tão errado assim. O que importa é que ele é um dos Antigos que causa terrores inimagináveis na mente de meros mortais só por exercer sua presença."
    
    s "E no dia que ele despertar de sua casa em {i}R'lyeh{/i}, todos encontraremos nosso fim."
    
    p "Nossa. Você realmente entende do assunto! Acho que encontrei a pessoa certa pra perguntar se eu deveria começar a ler."
    
    show sofia shy at noghost
    
    s "Ah, desculpa. Eu me empolguei e falei demais, né? Eu fiquei te prendendo aqui falando besteira. Desculpa."
    
    p "{i}Tá{/i} tudo bem. Eu {i}tava{/i} querendo alguém que me recomendasse um bom livro, e eu acho muito legal ver alguém falando empolgado do que gosta."
    
    show sofia standing at noghost
    
    p "Eu fiquei bem animado de começar a ler os livros do {i}Lovecraft{/i} depois de ver toda sua empolgação."
    
    p "Aliás, sou [povname], sou novo aqui e vim conhecer a biblioteca hoje. Ainda bem que encontrei alguém que parece gostar de livros também."
    
    show sofia happy at noghost
    
    s "Opa, não me apresentei também. Sou Sofia. Também sou nova aqui, mas provavelmente a biblioteca já virou minha segunda casa."
    
    s "Eu gosto muito de ler. De tudo um pouco. Mas eu gosto bastante de terror, horror, suspense e mistério. Penso que são gêneros que te prendem demais na história e te envolvem emocionalmente em maior grau que os outros."
    
    show sofia standing at noghost
    
    p "Eu não li muitas coisas desses gêneros, mas lembro de ler algumas coisas da {i}Christie{/i} e do {i}King{/i} e achei bem legais. Conheço mais histórias de ficção científica e fantasia."
    
    p "Mas acho que vou dar uma chance pros horrores de {i}Lovecraft{/i} dessa vez... Qual livro você recomenda eu ler primeiro? Tem uma cronologia?"
    
    show sofia happy at noghost
    
    s "Ótima escolha! *hehe* a maioria das histórias são bem desconexas, mas fazem parte do mesmo mundo. Como você {i}tava{/i} curioso com o {i}Cleber{/i}, acho que você pode começar com ele mesmo. *risos* É um ótimo conto."
    
    p "Ok, vou levar \"O Chamado do Cleber\", então *risos*. Obrigado!"
    
    show sofia standing at noghost
    
    s "De nada!"
    
    p "Ah... eu sei que a gente mal se conhece. Mas você usa algum aplicativo de mensagem pra gente continuar se falando? Eu não tenho ninguém aqui ainda pra conversar sobre livros, e nem me recomendar contos de terror..."
    
    s "Claro! Vou te passar meu Zapzap... Pronto! Me fala o que achou quando terminar o livro."
    
    p "Pode deixar. Obrigado pela ajuda! Eu vou ter que ir agora, mas a gente vai se falando. Foi um prazer!"
    
    show sofia happy at noghost
    
    s "Até! O prazer foi meu. Boa leitura!"

    # This ends the game.

    return
