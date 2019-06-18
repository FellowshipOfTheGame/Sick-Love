# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label rafaelafirstdate:

    $ nDatesRafaela+=1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black with Fade(0.7,0.2,0.7)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    
    scene gym with Fade(0.7,0.2,0.7)

    "No final das contas acabei entrando pro clube de {i}kendô{/i}. O capitão era bem simpático e me animou de treinar. Mas..."
    
    "Aaaaah meus músculos" with Shake((0, 0, 0, 0), 0.5, dist=10)
    
    "Nunca pensei que eu ia conseguir ficar tão dolorido em tão pouco tempo. Não parecia ser algo tão difícil assim lutar com uma espada."
    
    "Mas desde que comecei o treino eu chego em casa, consigo me arrastar pro chuveiro e desmaio na cama até o dia seguinte. E aí um pouco depois começam as dores musculares."
    
    "Nos primeiros treinos eu não conseguia nem levantar meu braço nos dias seguintes..."
    
    "-BAM!-" with Shake((0, 0, 0, 0), 0.7, dist=15)
    
    p "Ouch."
    
    u "Eu já falei pra você parar de ficar distraído durante o treino. Você fica cheio de aberturas. Fica fácil demais de te golpear."
    
    p "Desculpa, {i}sensei{/i}. Acho que foi um pouco de cansaço acumulado. Prometo que vou me concentrar mais."
    
    u "Tudo bem. Já era o fim do treino mesmo. Você está pegando o jeito [povname]. Daqui umas semanas as dores musculares devem diminuir um pouco e você consegue focar mais nas técnicas e na agilidade com a espada."

    p "Obrigado, capitão. Assim espero."
    
    u "Dispensados, pessoal. Até a próxima."
    
    scene black with Fade(0.7,0.2,0.7)
    
    #TODO barulho de coisas sendo arrumadas?
    "..."
    
    scene gym with Fade(0.7,0.2,0.7)
    
    "Ufa. Cansei... Olha, é a {i}Rafa{/i}. Vou dar um oi pra ela."
    
    p "Hey!"
    
    show rafaela happy at noghost
    
    r "Oi, [povname]! Tudo bem? Nossa, pela sua cara de morto acho que não {i}tá{/i} tão bem não. *risos*"
    
    p "Eu {i}tô{/i} bem. ainda sinto meus braços. Acho... Então já é uma vitória. E você, como {i}tá{/i}?"
    
    r "Tudo {i}top{/i}. Vim treinar {i}hand{/i} agora. Você {i}tava{/i} no {i}kendô{/i}?"
    
    p "Sim. Sobrevivi a mais um treino. Mas {i}tá{/i} bem legal, apesar da canseira. Obrigado por me indicar o capitão!"
    
    r "{i}Suave{/i}. Ou, vai ter jogo aqui na cidade da copa feminina de futebol. Quer ir? Não sei se você curte."
    
    p "Não sou especialista em futebol, mas eu aceito ir sim. Só preciso ver se posso no dia e tenho grana pra ir. Você me manda depois os detalhes?"
    
    r "{i}Topíssimo{/i}! Mando no {i}insta{/i}, então. Foi mal mas vou ter que ir treinar. Até!"
    
    p "Até!"
    
    hide rafaela
    
    scene black with Fade(0.7,0.2,0.7)
    
    "-{i}Mais tarde{/i}-"
    
    scene bg room
    with Fade(0.7,0.2,0.7)

    "Opa! A Rafa me mandou as {i}infos{/i} do jogo... Boa! Vou conseguir ir."
    
    show sofia cell at celltransform
    
    p "Posso ir sim!"
    
    r "{i}Aeee{/i}, arrumei companhia! Boa! {i}Bora{/i} ver as {i}mina{/i} arrasar no {i}fut{/i}!"
    
    p "Uhul! Precisava dar uma saída pra relaxar. Obrigado pelo convite!"
    
    r "{i}Nada{/i}! Até lá então. {i}Bjs{/i}."
    
    p "{i}Bjs{/i}."
    
    "Caramba... Ela falou que arrumou companhia... Quer dizer que vamos só nós dois? Isso era algum tipo de encontro?"
    
    "Será que eu finalmente arrumei um encontro com uma garota descolada e bonita?"
    
    p "*Ai*" with Shake((0, 0, 0, 0), 0.3, dist=5)
    
    "Ok, melhor não comemorar muito porque meus músculos não permitem. {i}Tô{/i} morrendo. Vou dormir, amanhã eu penso nisso."

    #Ele está no ginásio treinando. Entrou para o clube de alguma coisa
    #Depois do treino ele encontra Rafaela, que está chegando para treinar algo
    #Eles conversam um pouco (mostrar que estão um pouco mais íntimos): comentar sobre partidas na televisão ou algo assim.
    #Ela fala que vai ter jogo de alguma coisa X, pergunta se ele quer ir. Ele fala que tem interesse, só precisa ver a data e se tem grana
    #Ele chega em casa, confirma a data e fala com Rafaela
    #Eles combinam tudo e vão pro jogo
    #Rola o jogo, alguns comentários sobre a partida
    #Se despedem, falam q foi mto legal e pá

    # This ends the game.

    return
