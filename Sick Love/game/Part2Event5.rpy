label part2fifthevent:

scene bg room

"Finalmente acabou o semestre, sem mais provas, sem mais trablhos, agora é só curtir as férias!"

"Mas antes disso..."

show garota cell at celltransform

p "E aí, tudo certo pra hoje?"

g "Claro, daqui a pouco estarei pronta, já estou terminando de me arrumar."

p "Maravilha, acho que na volta podemos passar aqui em casa, quero conversar contigo num lugar mais privado."

g "Eu ultra apoio, podemos aproveitar pra nos despedir de verdade antes das férias."

hide garota

"Bem agora é esperar, ainda bem que consegui adiar a passagem, aconteceu um imprevisto na minha cidade e meus pais nem estariam em casa pra me buscar de qualquer forma."

"Ao menos com isso sobrou um ultimo dia pra sair com a [g.name]."

"Eu quero aproveitar esse dia com ela, mas não posso mais ignorar tudo que nós vivemos nesses meses de namoro."

"Precisamos colocar um ponto final nisso, não quero seguir com esse problema férias adentro."

"Sem contar que é melhor resolver isso presencialmente do que por mensagem ou ligação e definitivamente esperar para depois das férias seria o pior pra nós dois."

"Espero que ela aceite me dar mais espaço e aceite mudar, ainda gosto muito dela, mas ela não pode continuar agindo como está, só queria que ela voltasse a ser como era no começo..."

"Bem, melhor eu ir antes que eu me atrase."

scene metro

show garota happy at arantesnoghost

if garota == mariana:

    g "Nossa, que filme, fazia tempo que eu não não me animava tanto com um filme de super-herói, esse foi um dos melhores plot-twists que eu já vi."

if garota == rafaela:

    g "Que jogo! Eu não achava que uma virada dessas era possível, jogaram muito."

if garota == sophia:

    g "Essa exposição foi muito legal, ainda mais tendo uma sala interativa no fim."

#end

p "Né? o final foi muito bom mesmo."

p "Que sorte que tivemos tempo pra sair mais uma vez."

show garota standing

g "Sim, mas no fim das contas, o que você queria falar comigo?"

p "Bem, é que... Tem certeza que quer falar aqui?"

g "Qual o problema?"

p "Bem... Então tá bom."

p "Eu gosto muito de você, gosto de sair contigo e falar contigo, mas você tem feito coisas que não acho que façam bem pra nossa relação."

p "Ficar se vitimizando, não deixar eu sair com meus amigos, ficar me seguindo escondida, não me deixar estudar o tanto que eu acho necessário, esse tipo de coisa."

show garota evasive at arantesnoghost

g "Calma, não é bem assim, eu só quero passar mais tempo contigo e quero que você passe mais tempo comigo, afinal das contas nós estamos namorando."

g "É assim que se passa uma vida em um relacionamento, tem que se viver a dois."

p "Esse é o problema, nós não temos que viver a dois, somos duas pessoas, estamos juntas por gostarmos uma da outra, mas isso não muda o fato que somos duas pessoas."

p "É claro que vamos passar muito tempo juntos e eu vou mudar meus hábitos pra me adaptar melhor a ti e você também se adapta a mim."

p "Mas eu ainda sou eu, com meus amigos, meus deveres, meus gostos e minha forma de viver."

p "Pra mim não está sendo fácil ter que lidar com isso pra conseguir manter os bons momentos que tenho contigo."

g "Acho que o problema então é que nós temos que aprender a lidar com a forma que cada um percebe um relacionamento."

p "Eu tentei, eu realmente tentei, por isso tenho suportado essas coisas que você faz."

show garota sad at arantesnoghost

g "Você tem que entender que eu faço essas coisas porque eu gosto de você."

p "Esse é a questão, eu entendo que você faz isso por gostar de mim e eu não acho certo."

menu:

    "Pedir pra dar um tempo":

        jump Part2Event5Passive

    "Terminar o namoro":

        jump Part2Event5Active

label Part2Event5Active:

p "Eu realmente tentei aceitar a forma com que você lida com o relacionamento, tentei pensar que só era uma prova de amor distorcida por uma percepção deturpada."

p "Mas pra mim não dá mais, acho que o melhor seria findar esse relacionamento, eu sinto saudade de quando éramos apenas amigos, as coisas desandaram de uma forma que eu não esperava."

show garota mad at arantesnoghost

g "Pera, oi?!?"

g "Como assim??"

g "Por que você está terminando comigo? O que você está fazendo com a gente? Nós fomos feitos um para o outro! Eu fazia tudo por você."

g "Você vai se arrepender do que você está fazendo, é sério."

p "Eu não sei, talvez eu me arrependa, mas por agora eu acho que é a coisa certa a ser feita para nós dois."

p "Da mesma forma que eu acho que esse namoro não está fazendo bem pra mim não acho que ele esteja fazendo bem pra você."

p "A forma como você está lidando com tudo isso eu acho que não é normal, e é por isso que acho que o melhor é seguirmos cada um o seu caminho."

p "Não estou dizendo que não poderemos ser amigos no futuro ou algo do tipo, mas acho que por hora o melhor é nos afastarmos para nos resolvermos com nós mesmos."

show garota sad at arantesnoghost

g "Eu não tô acreditando que isso está acontecendo..."

g "Bem... então vai lá, teu metrô está chegando, acho que vou dar uma volta sozinha então..."

p "Ok, se cuida..."

scene black with Fade(0.7,0.2,0.7)

scene bg room

"Ainda tenho algum tempo para arrumar minhas malas."

"Poderei fazer tudo sem pressa..."

"Eu ainda não acredito que eu terminei com ela..."

"É estranho que mesmo eu me sentido mal com isso, também foi algo um pouco libertador."

"No fim acho que só não tinha como dar certo nós dois, não nesse momento de nossas vidas, espero que ela fique bem, mas o mais importante agora é eu ficar bem comigo mesmo."

return

label Part2Event5Passive:

p "Acho que podemos usar essas férias pra pensar melhor em como estamos lidando com tudo isso, sabe?"

p "Eu quero continuar com você, mas é evidente que temos problemas."

p "Com esse tempo afastados acho que poderemos perceber o que de melhor vemos um no outro pra voltarmos ainda mais próximos."

show garota evasive at arantesnoghost

g "Tudo bem... Eu também acho que temos algumas coisinhas aqui e ali que podemos melhorar, acho que isso é verdade para os dois lados."

p "Ainda bem que você aceitou sem problemas, achei que você não iria aceitar bem a ideia."

g "Por que eu faria isso? Se isso é algo que te incomoda, é algo que me incomoda, eu me preocupo com você."

p "Bem, obrigado por isso. Acho que vou seguindo meu caminho então."

g "Espera, nós não vamos pra sua casa?"

p "Bem, imagino que não, né?"

show garota standing at arantesnoghost

g "Por que? Olha, vamos fazer assim, nós começamos esse 'tempo' que vamos dar a partir de amanha, que tal? Vamos aproveitar nosso ultimo dia, querido."

p "Mas isso meio que não é contra a ideia de 'dar um tempo'?"

g "Ah, vamos lá, só mais hoje. Vai dizer que você também não quer se despedir propriamente?"

p "Bem..."

g "Vamos logo, o metrô está pra partir."

scene black with Fade(0.7,0.2,0.7)

"-{i}Na manhã seguinte{/i}-"

scene bg room

show garota standing at arantesnoghost

p "Bem, tchau tchau, passar bem."

g "Até mais, nos vemos no próximo semestre."

hide garota

"Eu tenho a leve impressão que ela vai tentar falar comigo durante as férias..."

"Talvez nada vá mudar de fato, mas ao menos eu tentei. Nada me impede de continuar tentando também, só por que dessa vez nada mudou não quer dizer que sempre vai ser assim."

"Bem, melhor eu correr ou não conseguirei fazer minha mala a tempo."

return
