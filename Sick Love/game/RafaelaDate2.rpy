# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label rafaelaseconddate:

    $ nDatesRafaela+=1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black with Fade(0.7,0.2,0.7)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    
    scene bg gym with Fade(0.7,0.2,0.7)

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
    
    scene bg gym with Fade(0.7,0.2,0.7)
    
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
    
    show rafaela cell at celltransform
    
    p "Posso ir sim!"
    
    r "{i}Aeee{/i}, arrumei companhia! Boa! {i}Bora{/i} ver as {i}mina{/i} arrasar no {i}fut{/i}!"
    
    p "Uhul! Precisava dar uma saída pra relaxar. Obrigado pelo convite!"
    
    r "{i}Nada{/i}! Até lá então. {i}Bjs{/i}."
    
    p "{i}Bjs{/i}."
    
    hide rafaela cell
    
    "Caramba... Ela falou que arrumou companhia... Quer dizer que vamos só nós dois? Isso era algum tipo de encontro?"
    
    "Será que eu finalmente arrumei um encontro com uma garota descolada e bonita?"
    
    p "*Ai*" with Shake((0, 0, 0, 0), 0.3, dist=5)
    
    "Ok, melhor não comemorar muito porque meus músculos não permitem. {i}Tô{/i} morrendo. Vou dormir, amanhã eu penso nisso."

    scene black with Fade(0.7,0.2,0.7)

    "-{i}No dia do jogo...{/i}-"
    
    scene bg stadium
    with Fade(0.7,0.2,0.7)
    
    p "Hey, Rafa, cheguei. Valeu pelo convite! Vai ser minha primeira vez vendo um jogo ao vivo."
    
    show rafaela happy at noghost
    
    r "{i}Yo{/i}!{i}Suave manolo{/i}, não esquenta não. {i}Tô{/i} feliz que você veio. Muito mais {i}top{/i} assistir jogo junto com alguém. Dá pra ficar discutindo os {i}rolês{/i}."
    
    show rafaela standing at noghost
    
    r "Mas, nossa. Como assim você nunca viu um jogo ao vivo? Nenhum? De nada?"
    
    p "Digamos que eu não sou um fã tão grande de esportes... Mas agora na faculdade estou tentando melhorar e ser mais saudável." 
    
    p "E acho que assistir a galera profissional se esforçando assim, de perto, vai ser bom pra me motivar."
    
    r "Acho que é um bom começo mesmo. Eu gosto de esportes desde pequena..." 
    
    show rafaela happy at noghost
    
    r "Sabe, quando eu {i}tô{/i} ali jogando com o pessoal, desafiando meus limites, dando o meu melhor, é quando me sinto mais viva!"

    "Os olhos dela brilham tanto quando ela começa a falar das coisas que ela gosta... Ela fica ainda mais linda..."
    
    "É incrível como quando eu estou com ela eu começo a gostar de esportes, mesmo sendo algo que nunca tive muito interesse."

    r "E eu fico muito feliz que hoje em dia finalmente os campeonatos femininos {i}tão{/i} ganhando mais visibilidade." 
    
    show rafaela sad at noghost
    
    r "Eu adoro assistir jogos, mas eu ficava meio triste quando pequena porque quase todos os campeonatos que passavam na TV eram os masculinos... Às vezes eu pensava que isso não era pra mim..."
    
    p "É... Eu imagino como devia ser bem chato isso. Eu nunca fui muito fã de esportes assim, então eu só consigo lembrar dos jogos masculinos quando penso na minha infância..."
    
    p "O que é bem bizarro quando a gente para pra pensar, mas o jeito como as coisas aconteciam fazia parecer tão natural, especialmente pra gente, que via os outros homens jogando e não percebia nada errado."

    r "Sim. Esse tipo de coisa acaba ficando tão enraizado na sociedade que nem mesmo as mulheres percebem a maioria das vezes. Ainda bem que muita gente vem lutando por isso e as coisas vem melhorando..."
    
    show rafaela happy at noghost
    
    r "Mas {i}bora{/i} parar com essas {i}bad vibes{/i}! Eu to muito feliz de estar aqui vendo o jogo com você! E já vai começar! Ai, que emoção!"
    
    "Realmente... a Rafa consegue irradiar energia mesmo depois de falar de algo que com certeza incomodava ela... Que garota incrível!"
    
    "Eita, começou. Melhor eu prestar atenção no jogo e não ficar aqui divagando."
    
    hide rafaela
    
    scene black with Fade(0.7,0.2,0.7)

    "-{i}Perto do fim do jogo...{/i}-"
    
    scene bg stadium
    with Fade(0.7,0.2,0.7)
    
    show rafaela upset at noghost
    
    r "AAAAAH VAI VIRA ESSE JOGO! VAMO LÁ DESEMPATA! VOCÊS CONSEGUEM! AAAAAAAH"
    
    "O jogo estava empatado, 1x1, depois da nossa seleção começar perdendo. Agora perto do final a Rafa {i}tiltada{/i} nervosa com a galera, aparentemente. Não consigo dizer se ela está torcendo ou xingando eles..."
    
    "É um pouco assustador, mas ela fica fofa mesmo irritada."
    
    show rafaela standing at noghost
    
    p "ELAS TÃO COM A BOLA, AGORA VAI! Caramba, falta pouco pra acabar a partida. Elas precisam fazer agora pra virar..."
    
    "Ok, confesso que eu também estou com os ânimos exaltados com o jogo. Nunca pensei que assistir um jogo ao vivo fosse tão empolgante assim." 
     
    "Pra quem {i}tá{/i} acostumado a só vibrar em campeonato de MOBA e evento de {i}speedrun{/i}, isso aqui é uma grande novidade."
    
    p "VAI, CHUTA. AGORA VAI!"
    
    "E então a atacante chuta a bola que recebeu de um lindo passe, direto para o gol. Em um chute forte e extremamente bem colocado, deixando a goleira da seleção adversária sem tempo de reagir."
    
    "E a bola, como um ataque especial totalmente carregado posicionado exatamente no ponto fraco daquele chefe impossível daquele jogo difícil, acerta o alvo em cheio."
    
    show rafaela happy at noghost

    r "GOOOOOOOOOOL!" (multiple=2)
    
    p "GOOOOOOOOOOL!" (multiple=2)
    
    "E então, a torcida vai à loucura. Todos pulam e gritam e comemoram. Mas, o que eu não esperava, é o que aconteceria durante essa comemoração."
    
    "Empolgados com o gol, eu e a Rafa nos abraçamos. Ao final do abraço, tomada pela euforia e felicidade, ela me beija."
    
    "Me assusto por um momento. O coração bate mais forte." with Shake((0, 0, 0, 0), 0.3, dist=3)
    
    show rafaela shy at noghost
    
    "Ela se afasta um pouco, o rosto envergonhado. Eu me aproximo dela de novo e retribuo o beijo."
    
    "Sentamos em nossos lugares. Alguns segundos de silêncio se passam. Ou será que foram minutos? Eu não sei. Meu coração está disparado. A euforia do gol e do beijo, juntas numa descarga de adrenalina e endorfina."
    
    "Meu coração parece que vai explodir. Por um momento um pensamento totalmente idiota e fora de contexto vem à minha mente: \"Caramba, é hoje que eu infarto. Ainda bem que estou fazendo exercícios pra melhorar meu {i}cardio{\i}\""
    
    "E eu me imagino olhando com reprovação para meu cérebro e repreendendo-o: \"O que você tá me fazendo pensar nessas horas? Eu acabei de beijar uma garota linda, \"5/7\", e é isso que você pensa?\""

    "Me pergunto como deveria reagir. Não sei. Preso em meus pensamentos, só sou salvo de meu cativeiro mental pelo apito da juíza. Acabou a partida. Mais comemorações. Olho para o lado..."

    show rafaela happy at noghost

    r "AEEEEEEEEEE! GANHAMOS!"
    
    "A Rafa parece estar de boa com tudo. Comemora como se nada tivesse acontecido. Concordo que é a melhor coisa a fazer. Depois pergunto para ela o que foi isso que rolou. Pode ter sido apenas a adrenalina?"
    
    "Abraço ela para comemorar. Ela também me abraça. Sem um beijo dessa vez. Tudo bem. Não dá para ouvir nada com a comemoração. Não adianta conversar agora. Deixo a ansiedade de lado para aproveitar esse momento."
    
    hide rafaela
    
    scene black with Fade(0.7,0.2,0.7)

    "-{i}Após a torcida se acalmar um pouco{/i}-"
    
    scene bg stadium
    with Fade(0.7,0.2,0.7)
    
    show rafaela happy at noghost
    
    r "Caramba, que jogo {i}mega top{/i}! Emoção até o último segundo! Bora ir saindo, a fila vai ser grande. E aqui {i}tá{/i} difícil de conversar com todo esse barulho."
    
    show rafaela standing at noghost
    
    p "Sim. Caramba. Foi bem emocionante!"
    
    "Estou mais perto da saída, viro para começar a andar e, por algum motivo inconsciente, estendo a mão para trás. Não sei no que eu estava pensando. Mas algo dentro de mim tinha a esperança de que ela segurasse a mão que estendi."
    
    "E ela segura!" with Shake((0, 0, 0, 0), 0.3, dist=3)
    
    "O coração bate um pouco mais forte, não tenho coragem de olhar para trás. Apenas aperto um pouco mais forte a mão, como se confirmasse para ela que eu estava segurando a mão dela. E continuamos andando até a saída..."
    
    scene black with Fade(0.7,0.2,0.7)

    "-{i}Na saída...{/i}-"
    
    scene bg stadium
    with Fade(0.7,0.2,0.7)
    
    p "Ufa. Saímos! Por um momento achei que íamos ficar presos até a próxima partida começar."
    
    show rafaela happy at noghost
    
    r "*risos*. Seu exagerado!"
    
    "Eu precisava aproveitar o clima descontraído para perguntar sobre o beijo. Era agora ou nunca. Juntei toda a minha coragem e perguntei:"
    
    p "Então... Sobre o que rolou no último gol... aahn... foi alguma coisa no calor do momento? É algo que posso levar a sério? Você gosta de mim? Desculpa perguntar assim do nada. Mas eu fui pego um pouco de surpresa..."
    
    show rafaela shy at noghost
    
    r "Ah... Aquilo... Bem... Acho que pode dizer que foi um pouco de tudo. O momento ajudou, mas eu te acho um cara legal, simpático e bonito. Então meio que rolou."
    
    show rafaela evasive at noghost
    
    r "Mas... Assim... Não sei como dizer isso de um jeito menos direto, mas eu não quero que você também leve tão à sério o que rolou." 
    
    r "Eu não posso dizer que realmente gosto de você, a gente nem se conhece a tanto tempo... Acho que ainda precisamos de um tempo pra se conhecer melhor..."
    
    show rafaela shy at noghost
    
    r "Mas não estou dizendo que não foi bom! Eu gostei e queria continuar isso que tá rolando!"
    
    show rafaela standing at noghost
       
    r "Mas só {i}tô{/i} falando que eu queria levar isso com calma e sem compromisso por enquanto. Claro, se você não se importar em sermos só {i}peguetes{/i}, pelo menos por enquanto."
    
    "Uau. Um turbilhão de informações saiu da Rafa quando perguntei. Ela estava nervosa e falou tudo muito rápido. E agora preciso processar tudo... Ok, ela não gosta de mim, mas quer ficar comigo."
    
    "Caramba. Meu coração está disparado. Mas tudo bem. Preciso pensar. Eu quero um relacionamento casual assim com alguém? Não sei. É difícil pensar sobre." 
    
    "Mas eu entendo ela não querer algo sério agora. A gente realmente mal se conhece. Mas eu acho que gosto dela... Mas não adianta nada se ela não gosta de mim de volta."
    
    "Mas se eu aceitar e continuar gostando dela e ela não gostar de mim, quem vai se machucar sou eu... Mas também se eu não aceitar talvez nunca avance nosso relacionamento e as coisas nunca possam progredir para algo mais sério..."
    
    "AAAAAAAAAAAAAH"
    
    "Eu estava claramente em um conflito interno. Mas eu não tinha todo o tempo do mundo para pensar sobre isso. E mesmo se tivesse, eu duvido que chegaria numa resposta 100\% segura sobre o que fazer." 
    
    "Foi então que deixei meus instintos falarem mais alto e respondi o que meu \"coração\" sugeriu:"
    
    p "Claro! Tudo bem por mim. É meio cedo ainda para assumirmos algo sério, mas eu gostei bastante também do que rolou. E você é uma pessoa linda e alegre e apaixonada pelo que faz. Eu gosto muito da sua companhia. Vamos ver o que rola!"
    
    show rafaela happy at noghost
    
    r "{i}Topzera{/i} então! Fico feliz que você tenha entendido e esteja na mesma {i}vibe{/i}... Mas aí, eu preciso ir indo. Valeu por vir. Foi bem {i}daora{/i}. E {i}tô{/i} muito feliz que as {i}minas{/i} ganharam."
    
    r "Bem, até mais..."
    
    "E então nos beijamos de novo..."
        
    show rafaela shy at noghost

    p "Até! Foi bem {i}daora{/i} mesmo. {i}Bora{/i} marcar mais {i}rolês{/i}."
    
    hide rafaela
    
    "E então ela se foi. E eu fiquei com um sorriso de orelha a orelha e preso nos meus próprios pensamentos."
    
    "Eu estou com uma garota. Não é algo sério (ainda, pelo menos... quem sabe...) mas é alguma coisa. Caramba. Que dia louco. Fui ver um jogo e saí com um beijo. Nada mal..."
    
    "Bem... vou para casa. Não adianta ficar parado que nem um idiota aqui pensando na vida."
    
    # This ends the game.

    return
