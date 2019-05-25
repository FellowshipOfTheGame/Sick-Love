label marianaseconddate:

$ nDatesMariana+=1

scene bg room
with Fade(0.7,0.2,0.7)

# TODO sfx videogame

p "{i}Vamo{/i}, agora vai."

# sfx videogame

"Tá quase... Tá quase..."

"Beleza, agora tá no ultimo estágio."

"Vai... Vai!"

# sfx derrota

p "NÃÃÃOO!!"

"Droga, dessa vez eu realmente achei que ia dar certo. Eu não consigo mais jogar esse jogo."

p "..."

p "..."

"Ok, só mais uma tentativa, vamos fazer a {i}saideira{/i}."

scene bg room
with Fade(0.7,0.2,0.7)

#sfx videogame

"Quase lá... Quase lá..."

# sfx vitória

p "BOOOAAAAAA!!"

"Finalmente consegui terminar o jogo, a Mariana não {i}tava{/i} de brincadeira quando falou que o jogo era difícil."

"Falando nela, deixa eu me gabar um pouco do meu feito, ela não estava botando fé que eu conseguiria terminar hoje."

#pega o celular

p "Oi, e aí, como você está?"

p "Antes que pergunte, eu estou ótimo, consegui terminar {i}Sekido{/i}, mesmo desacreditado."

m "Caramba, parabéns. Eu não acreditava que você conseguiria ganhar hoje mesmo, mas isso foi porque eu achava que você pretendia ir na primeira aula pela manhã."

p "Ué, eu vou."

m "Espero que esteja preparado, você tem 2 horas pra estar pronto e animado pra aula."

p "Como assim?"

"-{i}Checa o relógio{/i}-"

p "JÁ SÃO 5 DA MANHÃ?!?" with Shake((0, 0, 0, 0), 0.7, dist=20)

m "Alguém se meteu em maus lençois e esse alguém não sou eu."

p "{i}Pera{/i}, por que você {i}tá{/i} acordada a essa hora também?"

m "Insônia."

m "Talvez causada por eu estar jogando {i}Demon May Cry 5{/i}, mas não acho que os fatos são relacionados."

p "Bom saber que eu não estou no {i}sal{/i} sozinho."

m "Aí é que você se engana."

m "Tenho uma longa experiência virando noites e indo pra aula, na verdade isso pra mim já é coisa de rotina."

m "Amanhã vou só tomar um café e estarei 100\%."

p "{i}Ata{/i}, quero ver então. Até amanhã, eu acho."

m "Até. Espero que sobreviva até lá."

scene bg classroom
with Fade(0.7,0.2,0.7)

show professor at noghost

t "E aqui encerraremos por hoje, até a próxima aula."

hide professor

"Meu Deus, por que eu fiz isso comigo?"

"Não absorvi nada da aula. Na verdade passei mais tempo tentando não dormir do que qualquer outra coisa."

"Como será que a Mariana aguenta isso? Deixe-me ver como ela {i}tá{/i}."

show mariana sad at noghost

p "Então, você se sente bem?"

m "..."

"Ela continua encarando o caderno, ela parece determida, só não sei para que."

p "Mariana, você tá bem?"

show mariana standing at noghost

m "Oi, {i}tô{/i} bem, e você?"

p "Talvez melhor que você."

p "Acho que não foi uma boa ideia virar a noite pelo dia, acho que vou voltar pro quarto e ir dormir mais cedo."

m "É, talvez não foi minha ideia mais brilhante, mas faltava tão pouco pra terminar o jogo..."

p "Eu sei... Eu sei..."

scene bg room
with Fade(0.7,0.2,0.7)

"Nossa, eu dormi como uma pedra, mas não era de se esperar menos, virar a noite nunca é uma boa ideia."

"O que será que aconteceu enquanto eu dormia? Deixa eu dar uma olhada no celular."

"Tem uma mensagem da Mariana, o que será que ela quer?"

"Nossa, ela mandou isso faz muito tempo, deve ter mandado ainda antes de ir dormir."

m "Ei, ouvi dizer que abriu um fliperama aqui perto da faculdade, na página deles {i}tá{/i} falando que tem vários jogos clássicos."

m "Tá afim de ir comigo no fim de semana? Não queria ir sozinha."

"Nossa, quem poderia imaginar que ainda teria gente comercializando essas máquinas."

p "Claro! Bora ver quem ganha no {i}Street Kombat{/i}."

"Mal sabe ela que eu era o melhor jogador de {i}Street Kombat{/i} do meu prédio."

"Espera um pouco, ela não comentou nada sobre chamar os meninos, será que seremos só nós dois?"

"Seria isso um encontro?!?" with Shake((0, 0, 0, 0), 0.7, dist=10)

"Calma, vai dar tudo certo, eu devo estar complicando as coisas, ela só deve estar me chamando porque os outros dois estão ocupados."

"Deve ser isso..."

#Trocar para o fliperama

scene bg arcade
with Fade(0.7,0.2,0.7)

"Será que ela já chegou? Eu acabei saindo de casa muito mais cedo, já que não sabia onde era o lugar, mas ele consegue ser bem chamativo."

m "[povname] ? Oi!"

show mariana standing at noghost

p "E aí? Tranquilo? Quer jogar o que primeiro?"

m "Hum... não sei. Que tal começarmos pelos clássicos?"

p "Bem, tem {i}Pac Boy{/i}. Lembro que jogava muito em {i}sites{/i}, mas nunca joguei o original."

m "Então {i}bora{/i}."

scene bg arcade
with Fade(0.7,0.2,0.7)
show mariana standing at noghost

m "Nossa, que jogo legal! Não sei o que é, mas jogar na máquina quase faz o jogo ficar mais divertido."

p "Né? Eu me vejo facilmente gastando pilhas de dinheiro nisso se ainda tivesse que pagar por {i}run{/i}."

m "É incrível como eles conseguiam fazer jogos tão diferentes com uma tecnologia tão limitada."

p "Espera um pouco, meus ouvidos me enganam ou eu ouço Betris?"

m "Definitivamente hahaha, quer jogar?"

p "Claro!"

scene bg arcade
with Fade(0.7,0.2,0.7)
show mariana standing at noghost

m "Aqui também tem outros jogos mais comuns. Quer tentar ir no jogo de arremesso à cesta?"

p "Vamos, mas já deixo avisado que você que chamou."

scene bg arcade
with Fade(0.7,0.2,0.7)
show mariana sad at noghost

m "Como você consegue fazer tantos pontos?"

p "Bem, talvez eu tenha um jeito pra coisa, quem sabe?"

p "Quer jogar outra coisa? Podemos jogar {i}Street Kombat{/i}, mas já deixo avisado que eu não vou pegar leve."

show mariana standing at noghost

m "Opa, desculpa aí, vamos ver se você joga do mesmo tanto que você fala."

scene bg arcade
with Fade(0.7,0.2,0.7)

show mariana excited at noghost

#sfx de controle
m "E.... Pronto!"

p "A tela branca do {i}Akomo{/i} de novo não!"

m "Com isso ficamos como? 8x0? Eu perdi a conta."

p "Mas... Como você é tão boa?"

show mariana happy at noghost

m "Bem, talvez eu tenha um jeito pra coisa, quem sabe? Hahaha."

"Caramba, eu nunca vi alguém jogar assim. Só sei que não foi algum {i}hack{/i} porque ela está do meu lado."

show mariana standing at noghost

m "Pra ser sincera eu participava de campeonatos, até ganhei alguns menores."

p "..."

m "Não precisa ficar boquiaberto, meninas também podem jogar em nível competitivo."

p "Eu sei, mas eu nunca tinha me encontrado pessoalmente com um jogador profissional. Me dá um autógrafo?"

show mariana happy at noghost

m "Hahaha deixa de se fazer de bobo, eu não dou autógrafo pra perdedor."

p "Então é assim? Beleza, vamos então fazer uma revanche, tudo ou nada!"

scene bg room
with Fade(0.7,0.2,0.7)
show mariana excited at noghost

m "Não sei se me sinto boba por não ter apostado dinheiro ou se me sinto mal por ficar pisando em você."

p "Ok... Eu aceito minha derrota."

"Se eu não tinha me feito de idiota antes agora eu consegui fazer isso com toda a classe e maestria de um bobo da corte."

show mariana standing at noghost

m "Não precisa ficar com essa cara, você joga bem, só não é nivel competitivo. Eu só estava zoando com a sua cara."

m "Na verdade talvez já seja a hora de voltarmos pra casa, já estão fechando o fliperama."

p "Mas já?!? Nossa, nem vi o tempo passar."

m "Eu também não."

m "Pra falar a verdade eu estava com muito sono quando te mandei a mensagem e eu estava morrendo de vergonha."

m "Mas que bom que você aceitou, hoje foi um dia muito legal, espero podermos sair mais vezes."

p "Eu também me diverti muito, vamos procurar mais coisas pra fazer. Vamos desbravar essa cidade."

show mariana happy

m "{i}Wow{/i}, calma ai bandeirante. Vai com calma hahaha. Mas, bem, já vou indo. Tchau tchau."

scene bg room
with Fade(0.7,0.2,0.7)

"Hoje foi muito legal, acabou que não rolou nada entre nós dois, mas quando fomos nos despedir, acho que ela estava um pouco vermelha."

"Será que ela gosta de mim?"

"Assim, eu me divirto bastante ao lado dela e nossos gostos são bem parecidos, sem contar que ela é bem bonita..."

"Não sei com que cara eu vou olhar pra ela segunda..."

"Acho que vou aproveitar o resto do fim de semana pra lidar melhor com as ideias."

"Já que não tem nada pra..."

"{i}PERA{/i}" with Shake((0, 0, 0, 0), 0.7, dist=20)

"essa segunda já é dia 15?!?"

"Eu tenho que ler um capítulo inteiro até lá!"

"Droga, acho que não tenho tempo pra parar e refletir, os estudos me chamam!"

return
