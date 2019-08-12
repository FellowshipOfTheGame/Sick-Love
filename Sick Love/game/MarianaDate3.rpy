label marianathirddate:

$ nDatesMariana+=1

scene bg room
with Fade(0.7,0.2,0.7)

"Finalmente em casa. O que será que eu jogo agora? Já terminei o {i}Sekido{/i}."

"Pra ser sincero não tem nada em específico que eu queira jogar..."

"Queria falar com a Mariana. Acho que ela deve ter algum jogo legal pra me recomendar."

"Será que ela está online no Telegraph?"

#TODO mostrar o celular

show mariana cell at celltransform

p "Oi Mariana, tudo bem?"

m "Opa, tudo tranquilo aqui. Como você {i}tá{/i}?"

p "Então, história engraçada: mesmo com mais de 200 jogos pra jogar eu {i}tô{/i} meio entediado. Alguma recomendação?"

m "Humm, não sei se tem algo de novo pra te passar. Se bem que..."

m "[povname], você já jogou {i}Undercooked{/i}? Saiu o 2 recentemente."

p "Nunca joguei, mas já vi uns vídeos de pessoas jogando. Parece ser bom, mas acho que jogar sozinho não deve ser tão legal."

m "Não seja por isso, eu posso ir aí. Qual é o número do teu quarto mesmo?"

p "Ah, bem, pode ser também. Eu estou no quarto 1-214."

m "Tranquilo. Já já chego ai, beleza?"

p "Sem problemas."

#Sai do celular
hide mariana

"Quem diria que ela viria aqui, espero que corra tudo bem."

"..."

"ELA VEM AQUI?!?" with Shake((0, 0, 0, 0), 0.7, dist=30)

"Esse quarto {i}tá{/i} uma bagunça! tenho que arrumar isso rápido. Pelo menos tirar as cuecas do chão."

scene bg room
with Fade(0.7,0.2,0.7)

" -{i}Pouco tempo depois{/i}- "

"*knock* *knock*"

p "É acho que o grosso deu pra organizar."

show mariana excited3 at arantesnoghost

m "Oolá meu jovem, preparado para jogatina desta noite maravilhosa?"

p "Mais que preparado. Você realmente consegue se passar muito bem por uma {i}NPC{/i} que me daria algumas {i}quests{/i}, parabéns pelo bom trabalho."

show mariana happy3 at arantesnoghost

m "*risos* Eu tento. E aí? tudo pronto? Eu trouxe meus controles caso você não tivesse."

p "Ah, boa, pra falar a verdade eu só tenho um controle."

show mariana standing3 at arantesnoghost

p "Por sorte um amigo que tem conta compartilhada comigo tem o jogo, então já está terminando de baixar."

m "Menos mal, se precisasse eu poderia só entrar na minha conta pelo seu computador. Uma coisa a menos a ser feita."

m "Pra ser sincera eu estou impressionada, seu quarto até que está bem arrumado. Talvez isso seja por falta de base de comparação, já que aqueles dois não são nenhuma referência de organização."

m "Mas, de qualquer forma, bom trabalho."

p "Bem, eu tento *riso nervoso*."

m "E então, {i}bora{/i} jogar?"

scene bg room
with Fade(0.7,0.2,0.7)

#TODO add sfx videogame

"Nossa, mesmo com esses gráficos que fazem o jogo parecer simples, ele consegue ser bem difícil. Mas, mais importante que isso, que bom que estou conseguindo passar mais tempo com a Mariana."

"Ela também parece estar bem animada jogando, até me deu uns abraços no fim de algumas fases difíceis, mas até ai eu também já fiz isso com amigos. Não devo ficar imaginando coisas."

"Droga, perdemos."

show mariana evasive3 at arantesnoghost

m "Poxa, [povname], você parece estar um pouco desligado, {i}tá{/i} tudo bem?"

p "Foi mal, esse jogo é mais dificil do que parece *riso nervoso*."

show mariana standing3 at arantesnoghost

"Ela até está apoiando a cabeça no meu ombro, acho que nunca estivemos tão próximos."

m "Relaxa, só estou enchendo teu saco *risos*."

"Ela parece muito confortável comigo, será que ela gosta mesmo de mim?"

p "Mariana, por acaso..."

"Esse sorriso... Esse olhar... Acho que ela gosta de mim."

"{i}[povname] aproxima seu rosto do de Mariana, que segura sua nuca e o puxa em um beijo.{/i}"

show mariana blushed3 at arantesnoghost

m "Desculpa, o que você ia dizer?"

p "Nada não, você já me respondeu."

"{i}[povname] junta seu rosto ao dela em mais um beijo{/i}."

m "Acho que entendi."

"{i}Mariana abraça [povname] e...{/i}"

#TODO add sfx toque polifonico

"*ring**ring*"

m "É o meu celular, desculpa."

m "Nossa, já ta muito tarde, eu preciso voltar pro meu dormitório, amanhã eu tenho que me encontrar com meu grupo pra fazer um trabalho."

p "{i}Ah, tá{/i}. Sem problemas, vai lá."

m "Olha [povname], eu realmente gostei do que rolou hoje e eu não quero que seja só uma ocorrência perdida."

p "Eu também, queria poder passar mais tempo contigo."

m "Então... Quer namorar comigo?"

p "Bem..."

p "Roubou minhas palavras."

p "Tchau tchau, amanhã nos falamos mais."

m "Sim. Até mais, boa noite."

scene bg room
with Fade(0.7,0.2,0.7)

"Droga, não consigo dormir."

"Como eu consegui uma namorada assim? Acho que se eu contasse pra mim mesmo eu não acreditaria."

"Sempre tem a possibilidade de eu estar delirando. Será que finalmente eu fiquei maluco?"

"..."

"Não tem como, aquilo foi real. A Mariana está namorando comigo!"

"Eu sempre ouvi dizer que na faculdade eu me sentiria realizado, mas nunca imaginei que aconteceria tão cedo."

"Acho que as coisas finalmente estão começando a dar certo pra mim."

scene black with Fade(0.7,1,1)

#Finish
return
