label part2firstevent:

scene bg room

#sfx despertador

"Nossa, mesmo depois de dormir ainda estou cansado, ontem foi um dia longo."

"Acabei pegando uma matéria optativa que {i}tá{/i} dando muitos trabalhos."

"Ao menos consegui terminar, agora é só imprimir e já era."

"Não checo meu celular desde ontem à tarde. Eu realmente precisava me focar... O que será que rolou? Deve ter algumas centenas de mensagens acumuladas."

#pegar celular
#TODO celular fora do chat(layout basico de uma tela inicial)

"Olha aí, dito e feito."

"Ah não, a [garota] mandou mensagens. Isso é um mal sinal, ela se irrita muito quando eu demoro a responder."

"Esses dias ela tem estado muito em cima de mim."

"O que será que ela queria?"

# abrir chat com garota
#g seria a garota, n sei como definiremos ela futuramente

g "Onde você está?"

g "Já está em casa?"

g "Me responde logo!"

g "Você saiu sem me avisar mais uma vez?"

"Agora duas ligações perdidas dela..."

g "Me atende, por que você não está me respondendo?"

"Mais três ligações perdidas..."

g "Nossa [povname], que merda! Para de me ignorar!"

"E agora... Como eu respondo pra ela?"

"Nossa, pior que eu já estou um pouco atrasado, ainda tenho que imprimir o trabalho... Eu lido com isso depois, não estou com cabeça pra isso agora."

#troca de cena para hambiente externo

"Finalmente acabaram as aulas, esse dia foi longo, ao menos agora posso voltar pro meu quarto e descansar."

"Pera. Aquela ali não é a [garota]?"

#mostrar garota

p "Oi [garota], tudo bem, eu queria falar contigo."

g "Tudo bem. Podemos ir pro teu quarto?"

p "Ok. Pode ser."

scene bg room

#show garota

g "O que aconteceu ontem? você me ignorou a noite toda."

p "Então, eu tinha que fazer um trabalho, passei a noite toda ocupado com isso."

g "Mas poxa, você não poderia responder? Eu me preocupo contigo, por isso queria saber onde você estava e se você estava bem, só isso."

g "Tem vezes que você só some e isso me tira do sério. Sem falar que uma das vezes que isso aconteceu você tinha saído com seus amigos, e eu não sei quem foi com vocês."

g "Nós estamos namorando, não quero que você saia andando com outras meninas. Entende o meu lado, eu fico sozinha esperando sua resposta sendo que você poderia estar na farra."

p "Calma, primeiro: eu só fiquei sem te responder porque eu não estava usando o meu celular, eu deixei ele de lado no modo silencioso."

p "Era isso ou eu não conseguiria terminar o trabalho a tempo."

g "Mas poxa, o que custa me responder? Você pode silenciar os outros e ver só as minhas mensagens."

p "Mas aí perderia parte do propósito: eu precisava me focar, não podia ter distrações."

g "Agora eu sou só uma distração pra ti? Poxa, você é tão importante pra mim e eu me preocupo tanto e é assim que você me trata?"

    menu:
        "Espera, não foi isso que eu quis dizer":

            jump Part2Event1Active

        "Desculpa":

            jump Part2Event1Passive


Part2Event1Passive:

p "Desculpa, não foi isso que eu quis dizer."

p "Eu prometo que vou tentar olhar mais o celular e ser mais atento. Desculpa."

g "Tudo bem, obrigado por se importar, eu me preocupo com você."

p "Eu sei, obrigado por cuidar de mim."

g "Posso dormir aqui hoje?"

p "Claro."

"Eu sei que é difícil lidar com ela ficando em cima de mim, mas acho que relacionamentos são assim, não é?"

"Cada um cede um pouco e assim nós lidamos com isso."

return

Part2Event1Active:

p "Você entendeu o que eu quis dizer, não precisa ficar distorcendo."

p "Olha, eu entendo que você está irritada, mas eu às vezes vou acabar ficando na minha. Eu não estarei com outra. Eu nunca te trai ou algo do tipo."

p "Acho que por agora você deve refletir um pouco consigo. Não acho que essa possessividade vá fazer bem pra nenhum nós dois."

g "Bem... se for pra ser assim, acho que já vou indo então..."

p "Olha, eu gosto de você. Eu quero que esse relacionamento dê certo, então por favor repense isso."

p "Depois nós nos falamos."

#transição pro quarto/pequeno time skip

"Nossa... Espero que termine tudo bem entre nós dois. Eu ainda gosto dela, mas ela ficando assim em cima de mim não acho que vá dar certo."

"Depois chamo ela pra fazer algo no fim de semana, acho que ela deve passar a me entender melhor."

return
