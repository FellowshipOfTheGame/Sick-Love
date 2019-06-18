label part2secondevent:

scene bg classroom

"Finalmente em casa, tudo que eu preciso é de um pouco de descanso."

"Esse semestre está começando a apertar, tenho que estruturar melhor minha grade de estudos ou não vou conseguir passar em tudo."

#sfx mensagem no celular

"Opa, o que será que está rolando?"

#mostrar celular

"É o grupo da panelinha, o que será que aqueles dois estão aprontando? Será que é algum meme?"

"Ah, é só mensagem do Bruno."

b "Galera, eu não estou me sentido muito bem, não está sendo facil lidar com esse semestre pesado."

b "E ainda rolaram  mais problemas com a minha família..."

d "Cara, estamos aqui pra você, quer sair pra falar sobre isso?"

b "Acho que pode ser uma boa ideia, que tal esse sábado? Podemos ir naquele pub que abriu mês passado."

d "Por mim já é. [povname], você está livre?"

p "Estou sim, podemos confirmar o rolê."

d "Já é."

b "Até."

#tirar o celular

"Nossa, o que será que rolou com o Bruno? Espero que não seja nada muito sério..."

"Mas e se for..."

"Sábado eu iria sair com a [garota], mas acho que esse caso é mais emergencial."

#mostrar celular falando com a garota

p "Oi [garota], então, apareceu um imprevisto e não vai rolar de sair contigo esse sábado. :/"

g "Ué, o que aconteceu?"

p "Vou ter que sair com os meninos, o Bruno aparenta estar meio mal, então nos chamou pra desabafar."

g "Bem, acontece, onde nós vamos?"

p "Então, desculpa, acho que me expressei mal, no caso eu me referia a mim e ao Diego, pelo que eu entendi ele queria reunir apenas conosco, já que temos mais intimidade."

g "Poxa, queria ir contigo... Onde vocês irão?"

p "Ah, vamos naquele pub que abriu mês pasado."

g "Pera, o que vocês vão fazer no pub? Quem vai com vocês, [povname]?"

p "Só nos três ué, vamos só conversar, ouvir o que estiver tocando e talvez beber um pouco."

p "No fim o objetivo é deixar o Bruno falar o que ele quiser ou precisar falar e depois descontrair."

g "Mas por que em um pub? Será que na casa de um de vocês não seria melhor?"

p "Bem, posso ver com eles, perai."

#trocar para as mensagens do grupo

p "Galera, será que não seria melhor fazer isso na casa de alguém?"

d "Por que? Se formos no pub podemos matar dois coelhos numa cajadada só. Já faz um tempo que não saímos só nós três."

b "Né, e eu acho melhor ser no pub pra n acabar virando um rolê muito baixo astral"

p "Ah, se preferem assim, tudo bem."

#trocar para as mensagens da menina

p "É, eles não curtiram muito a ideia, mas não faz mal, vamos só bater papo mesmo."

g "Você realmente precisa ir? O Diego conhece o Bruno a muito mais tempo, será que não seria melhor ir só os dois?"

p "Bem, acho que se o Bruno quisesse chamar só o Diego ele teria mandado pra ele no privado, e não no grupo que só tem nós três."

g "É que... Eu não quero que você vá."

p "Por que?"

g "Bem, eu não posso ir com você, e aqueles dois são muito festeiros, provavelmente vai ter um monte de garotas lá com vocês e eu não gosto disso."

    menu:
        "Ficar com [garota]."

            jump Part2Event2Passive

        "Sair com amigos."

            jump Part2Event2Active


Part2Event2Passive:

p "Calma, não é pra tanto, eu só quero dar apoio pro Bruno."

g "Mas o Diego já vai, você não precisa ir também, por favor, fica comigo."

g "No domingo você pode perguntar pro Diego sobre o que eles conversaram e ele te repassa tudo. Se tiver algo sério você vai poder ir atrás disso depois."

p "Tudo bem... Vou avisá-los."

g "Obrigada querido <3."

#trocar para a conversa com a galera

p "Galera, não vou poder ir sábado."

b "Poxa, o que rolou?"

p "A [garota] ficou bolada porque eu iria sem ela, então vou passar esse fim de semana com ela."

d "Poxa mano, mais uma vez ela n deixa você sair? Quando vocês começaram a namorar ela era mais tranquila com isso."

p "Ah mano, é o jeito dela, mas nós vamos nos ajeitando."

"Preciso Mandar mensagem no privado para o Diego."

#trasação e mostrar o celular novamente

p "E aí cara, tudo bem?"

p "Então, já que eu não vou sábado me avisa se rolar alguma coisa ou se o Bruno estiver com algum problema maior, por favor."

d "Tranquilo mano, mas assim acho que você tem que tomar cuidado com a [garota], ela está muito em cima de você."

d "Você tem certeza que está tudo bem entre vocês dois? Ela parece estar sendo muito controladora."

p "Relaxa, está tudo sobre controle, nós nos damos muito bem."

d "Bem... se você está dizendo..."

return

Part2Event2Active:

p "Espera, é sério? Primeiro, nós não vamos lá pra ficar \"festando\", vamos só conversar."

p "Segundo, não vai ter \"um monte de garotas\" conosco, e mesmo que tivesse isso não importa. Eu nunca te traí e nem pretendo."

p "Não sou nenhum descontrolado que sai ficando com qualquer garota que aparece pela frente."

p "Eu estou namorando contigo, não vou ficar com nenhuma outra."

g "Eu sei disso mas isso não me impede de ter ciúmes."

p "Eu entendo, mas aqui a prioridade é ajudar o meu amigo, em outras situações eu já deixei de sair com eles por você, mas esse não é o caso."

p "Façamos assim, eu vou com eles pro pub, se não sairmos muito tarde eu passo no teu apê, se terminar tarde eu te mando mensagem e tentamos fazer algo domingo a tarde."

p "O que acha?"

g "Essa história toda não me agrada nem um pouco... Eu sou sua namorada, deveria ser prioridade."

p "E normalmente é, mas nesse caso a saúde mental do meu amigo pode estar em jogo, não posso deixar ele na mão só pra sair contigo ou por causa dos seus ciúmes."

p "Bem, minha proposta está feita ali em cima, se mudar de ideia me avise, mas esse sabado eu já estou ocupado."

return
