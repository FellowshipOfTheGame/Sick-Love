# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label rafaelafirstdate:

    $ nDatesRafaela+=1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg campus with Fade(0.7,0.2,0.7)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Ok, depois dessas aulas pesadíssimas eu cheguei à grande conclusão que preciso fazer algo longe dos livros e das salas de aula pra relaxar."
    
    "Disseram que a universidade tem um ginásio de esportes com várias quadras, e a gente pode praticar vários esportes."
     
    "Acho que vou dar uma olhada e ver se tem algo que me agrada. Não é como se eu fosse um grande atleta, mas vai ver eu acho alguma coisa aleatória interessante."
    
    "E é sempre bom fazer alguma atividade física pra não sofrer um infarto antes dos 30... Especialmente com tanta comida boa nessa cidade. Aquela pizza que comi ontem estava maravilhosa!"
    
    "E não podemos esquecer que estamos na universidade. Quem sabe se eu ficar em forma e atlético consigo chamar a atenção de alguma garota."
    
    "...Ok, foi fácil achar o ginásio. Talvez por ele ficar exatamente no centro da universidade e ter uma quadra gigante chamativa o suficiente pra se ver de longe. Mas ainda assim estou surpreso."
    
    if nDatesSofia > 0:
        "Achei que eu ia ficar perdido lendo placas e andando em círculos de novo..."
    
    "Mas, caramba! Isso é bem maior do que eu pensava! Achei que ia ter uma miniquadra de {i}handball{/i}, outra de vôlei de praia e no máximo uma piscina nem semi-olímpica... Mas {i}UAU{/i}!"
    
    "Tem um campo de futebol, pista de corrida, quadra de vôlei de praia, uma piscina semi-olímpica, uma quadra fechada bem grande, e um prédio ali que eu não sei o que tem dentro..." 
    
    "Tem tanta coisa que por um momento eu achei que ia ter um campo de {i}golf{/i}!"

    "Acho que vou dar uma olhada naquela quadra fechada. Talvez tenha alguma informação sobre as atividades e os horários..."
    
    scene bg gym
    with Fade(0.7,0.2,0.7)
    
    "Huum. Que legal, tem um pessoal jogando {i}handball{/i}. Eles até que jogam bem. Especialmente aquela garota loira... E ela é bem bonita... Enfim, foco. Não era isso que eu estava procurando."
    
    "Tem um quadro com uns papéis pregados ali, deixa eu ver... Huuum, ok, parecem ser convites de clubes para treinar... Galera do futebol, natação, judô, kendô... Uau, kendô, que legal!"
    
    "Parece divertido. Apesar de eu pressentir que vão me chamar de {i}nerd{/i} ou algo assim se eu fizer... Não que isso mude muita coisa na minha vida. Qual o horário?"
    
    u "Hey! Cuidado! ABAIXA!"
    
    #Som de bola acertando a cabeça do jogador
    
    "-BAM!-" with Shake((0, 0, 0, 0), 0.7, dist=20)
    
    #Som de algo caindo no chão
    
    p "Ouch!" with Shake((0, 0, 0, 0), 0.3, dist=5)
    
    u "Você {i}tá{/i} bem? Desculpa! Caramba... deve ter doído. {i}Tá{/i} tudo bem com você?"
    
    p "Ouch... Eu acho que sim? Não sei. Preciso refletir... Ok, acho que {i}tô{/i} bem."
    
    show rafaela sad at noghost
    
    r "Desculpa, de verdade. A gente estava animado com o jogo de {i}hand{/i} e a bola meio que escorregou da minha mão quando joguei em direção ao gol e acabou te acertando."
    
    r "Deixa eu te ajudar a levantar. Vai com calma... {i}Tá{/i} tudo bem, mesmo? Quer que eu te leve pra enfermaria? Coloque um gelo?"
    
    p "Não, relaxa, {i}tô{/i} bem. Eu só fui pego desprevenido e perdi o equilíbrio e caí. Mas, nossa, você é bem forte. Foi uma bolada das boas."
    
    "Caramba! É aquela garota bonita que {i}tava{/i} jogando {i}handball{/i}... Mas nossa, sinto minha cabeça latejando. E definitivamente não posso nem usar a desculpa que é o amor florescendo."
    
    show rafaela standing at noghost
    
    r "Ah... eu jogo faz um tempo. E eu faço uma ou outra atividade física que talvez ajude... Que bom que você está bem. Eu ia ficar meio {i}bad{/i} se tivesse quebrado seu nariz ou algo assim."
    
    p "Você costuma quebrar o nariz das pessoas jogando? Ou é só do pessoal que está passando aleatoriamente pela quadra? *risos*"
    
    show rafaela happy at noghost
    
    r "Acho que você realmente {i}tá{/i} bem, já que {i}tá{/i} fazendo piada. Aliás, senhor piadista, o que você estava fazendo parado aí no canto?"
    
    show rafaela standing at noghost
    
    p "Eu estava dando uma olhada nos esportes e atividades que tem aqui no ginásio." 
    
    p "Sou novo por aqui, e aí pensei que talvez fosse legal fazer algo pra não virar sedentário e morrer antes dos 30... E nem entrar em simbiose com minha cadeira."

    show rafaela happy at noghost
    
    r "Ok, gostei do seu senso de humor. Um pouco {i}dark{/i}, mas foi {i}top{/i}."
    
    show rafaela standing at noghost
    
    r "Eu {i}tô{/i} aqui na {i}facul{/i} faz um tempo já. E gosto bastante de esportes. Então, se quiser, posso te ajudar a escolher algo, senhor piadista. Algo como um pedido de desculpas pela tentativa de homicídio."
    
    p "Poxa, eu acho que vou aceitar a ajuda. Aliás, o nome do piadista é [povname]. Acho que, apesar de tudo, posso dizer que é um prazer te conhecer... aaaahn..."
    
    show rafaela happy at noghost
    
    r "Opa, verdade, não me apresentei. Eu sou a..."
    
    u "OU, RAFA, SE FOR PRA FICAR {i}XAVECANDO{/i}, PELO MENOS DEVOLVE A BOLA! A GENTE QUER TREINAR." with Shake((0, 0, 0, 0), 0.3, dist=5)
    
    show rafaela upset at noghost
    
    r "TOMA ESSA BOLA ENTÃO! E PAREM DE ME ZOAR NA FRENTE DO CALOURO. O QUE ELE VAI PENSAR DE MIM?"
    
    show rafaela shy at noghost
    
    r "Desculpa, meus amigos são meio {i}sem noção{/i} às vezes. Mas eles são legais... Onde que eu tava?"
    
    show rafaela happy at noghost
    
    r "AH, É! Meu nome é Rafaela. Mas acho que você já deduziu isso depois do {i}berro{/i} deles." 
    
    r "Eu participo do time de {i}hand{/i}, mas também faço um pouco de natação, corrida, muay thai, e umas outras coisas... quando sobra tempo, claro."
    
    p "Caramba! Quanta coisa. Como você arruma tempo pra tudo isso?"
    
    show rafaela shy at noghost
    
    r "Ah... eu gosto bastante de esportes. É meu refúgio do {i}stress{/i} e da correria da vida. E onde eu posso extravazar a raiva do período de provas." 
    
    show rafaela sad at noghost
    
    r "Mas eu confesso que às vezes eu acabo estudando menos do que deveria... Especialmente quando tem alguma festa {i}top{/i} pra ir... Acontece."
    
    show rafaela standing at noghost
    
    r "Mas e aí, do que você gosta? Tem bastante atividade na universidade. Todos os esportes mais comuns que você consegue pensar. Várias lutas e artes marciais."
    
    r "Tem a galera da natação, da corrida, do tênis... Tem até um pessoal que pratica danças... E aí?"
    
    p "Olha, antes de eu ser alvejado pela bola, eu tinha ficado interessado em kendô. Mas não sei se é tão legal quanto parece nos filmes e animes..."
    
    show rafaela evasive at noghost
    
    r "Nossa, que coisa de {i}nerd{/i}!"
    
    "Como eu suspeitei..."
    
    show rafaela standing at noghost
    
    r "Mas a galera do kendô é legal. Já pratiquei umas vezes. Não é muito do meu gosto, mas posso te apresentar depois pro capitão do clube. Tem uma galera que pratica esgrima medieval também."
    
    r "Pelos seus gostos de {i}nerd{/i}, talvez você goste também. Mas essa galera eu não tenho tanto contato. Vou ficar devendo."
    
    p "Caramba... tem realmente muita coisa aqui. Nunca ia imaginar que teria esgrima medieval. Mas acho que por enquanto vou aceitar o contato do capitão de kendô. E vou tentar ir conhecendo as coisas aos poucos."
    
    p "Se eu fizer coisa demais também eu acho que vou acabar infartando. Melhor ir com calma. Mas também não me importo de experimentar novas atividades."
    
    show rafaela happy at noghost
    
    r "{i}Belê{/i}! Vou te mandar o contato do capitão então. Você tem {i}insta{/i}?"
    
    p "{i}Instapound{/i}? Eu tenho, mas quase nunca {i}posto{/i} nada. Não estranhe."
    
    show rafaela standing at noghost
    
    "-{i}Após a troca de contatos...{/i}-"
    
    u "E AÍ? NÃO VAI TREINAR MAIS NÃO, CAPITÃ? VAI ABANDONAR O TIME?"
    
    r "Eita. Te passo o contato dele depois. E a gente vai se falando. A galera {i}tá{/i} nervosa. Desculpa de novo pela bolada. Até!"
    
    p "Tranquilo. Volta lá, capitã. Até mais!"

    # This ends the game.

    return
