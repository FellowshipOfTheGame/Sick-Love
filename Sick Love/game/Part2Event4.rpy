label part2fourthevent:

scene bg room

"Esse semestre parece não ter fim!"

"Já fiz 3 provas essa semana e ainda tem mais 3 semana que vem, ao menos eu não preciso de muita nota, mas a matéria é dificil, vou ter que estudar de qualquer jeito."

"Também tem o agravante que o professor aparenta estar irritado com a turma, acho bom eu não bobear."

"Mas olhando pelo lado positivo, ao menos essa é a ultima semana, daqui a 7 dias já estarei voltando para casa pra curtir as férias."

#som de notificação no celular

"Será que são os caras chamando pra estudar juntos esse fim de semana também?"

show garota cell at celltransform

g "Oi, já decidiu o que faremos esse fim de semana?"

"Nossa, tinha esquecido de avisá-la que vou ter q ficar estudando, que triste, queria sair com ela."

p "Então, esse semana não vai rolar também, tenho que estudar."

g "Poxa mas semana passada também nós não saimos!"

p "Desculpa, coisas do fim do semestre, não tem muito o que eu possa fazer."

g "Bem nós podemos sair, voce já tirou boas notas nas primeiras provas, não te falta muito pra passar."

p "Eu sei que falta pouco, mas se eu não estudar talvez eu não tire nem o suficiente."

g "Você não precisa de tanto assim, sem falar que por que pra essas provas você estuda mas pras outras não?"

p "Mas eu estudei pras provas dessa semana também."

g "Ué, você não passou o fim de semana com os meninos?"

p "Sim, estudando, o Bruno me ajudou com uma matéria, nós ajudamos o Diego com outra e assim conseguimos até que ir bem em geral."

g "Estudando? A tá, conta outra."

p "Sim, estávamos estudando. Nós não vamos começar com isso mais uma vez vamos?"

g "..."

g "Mas vamos sair poxa, sem contar que esse é nosso ultimo fim de semana, logo depois já vamos voltar pra ver nossas famílias."

"Verdade não vamos conseguir sair pra nos despedir direito, eu deveria ter pensado nisso quando comprei as passagens..."

"Mas eu ainda preciso ir bem nas provas, no próximo semestre já vão começar as oportunidade de intercâmbio, e eu preciso ter boas notas pra ser aceito."

"No primeiro semestre eu até consegui, em geral, iir melhoor que a maioria do pessoal, mas esse semestre está dificil manter as notas."

"Me falaram que é dificil conciliar namoro e estudo, mas eu não esperava que fosse tanto."

"Bem, acho que não tem motivo pra ficar escondendo as coisas, também seria hipocrisia minha combrar dela honestidade não sendo honesto também."

p "Eu sei, eu queria sair também, mas preciso estudar, se minhas notas cairem mais talvez eu não consiga um intercâmbio legal."

g "Intercâmbio? Eu não sabia que você queria fazer um, nunca me falou nada sobre."

p "Não faz muito tempo que eu percebi que com minhas notas eu poderia tentar algo, acho que pode ser algo bem positivo pra mim."

g "Mas poxa, vamos então sair só um dia, o que acha? Com isso também sobre tempo pra você estudar."

p "Eu não sei se um dia vai ser o suficiente..."

g "Vamos, por favor... Eu queria poder me despedir de você melhor, já que não vamos nos ver direito nessa ultima semana..."

menu:
    "Tudo bem, acho que talvez eu consiga revisar toda a materia em um dia":

        jump Part2Event4Passive

    "Eu queria sair, mas tenho que estudar, desculpa":

        jump Part2Event4Active


label Part2Event4Active:

p "Desculpa, mas eu realmente preciso estudar, podemos ver se conseguimos sair pra tomar um sorvete antes da viagem ou algo do tipo."

g "Tudo bem... Entendi... Eu achei que eu, nós, esse relacionamento, tivesse alguma prioridade pra você, mas eu estava errada."

p "Não é isso, é mais pelo fato que as vezes eu tenho que ver o que vai ser melhor pro meu futuro."

g "Bem, aparentemente é só o seu futuro, não o nosso..."

p "De onde você tirou isso?"

g "Não se faça de bobo [povname], você está tentando fugir de mim. Não quer sair comigo, agora esse papo de intercâmbio... O que está acontecendo?"

p "Eu não estou fugindo nem nada do tipo, eu só não vivo em função de você, nós namoramos mas ainda somos duas pessoas, não uma."

g "Entendi... Então assim que são as coisas, não é? Você entende o tanto que eu me sacrifiquei por nós dois?"

p "Esse é parte do problema, não era pra você precisar se sacrificar por um relacionamento."

p "Claro que vão ter algumas inconveniências, mas não precisa chegar ao ponto de ser sacrificante."

g "Então tá bom. Bons estudos, vou seguir minha vida aqui também."

"Isso terminou pior do que eu imaginava... Bem não otem muito o que ser feito, ela está brava comigo e vai ficar assim por um tempo."

"Melhor eu ir estudar."

return

label Part2Event4Passive:

p "Bem, acho que podemos fazer isso funcionar..."

g "Yeay. O que acha de ir naquela loja de waffles no shopping, ouvi dizer que eles atualizaram o cardápio recentemente."

p "Por mim tudo bem, vamos depois do almoço?"

g "Pode ser, você passa aqui e vamos lá."

g "Obrigada [povname], te amo."

p "Também te amo S2."

scene black with Fade(0.7,0.2,0.7)

"{i}Alguns dias depois{\i}"

scene bg room

"Beleza, agora só falta uma prova e acabou o semestre."

#som de notificação do celular

show group cell at celltransform

b "Sairam as notas da prova de segunda."

d "Já? Isso foi rápido."

b "Caramba [povname], o que rolou? Tua nota foi muito baixa."

d "Você vai conseguir passar na matéria?"

p "Espera um pouco que nem eu vi minha nota ainda."

"Meu Deus! Eu quase zerei a prova, vou ter que falar com o professor, se ele não me der alguns décimos terei que fazer a prova de recuperação."

p "É... Vou ter que ver com o professor, mas as chances de fazer uma prova de recuperação são altas."

d "O que rolou cara? Normalmente suas notas são boas, não conseguiu estudar?"

p "Então, acabou que eu tive de sair com a [g.name], então me sobrou pouco tempo pra estudar, tentei passar por tudo correndo, mas acho que isso só me fez confundir os conceitos."

b "Poxa cara, fim de semestre você deveria estar focado nos estudos..."

p "Eu sei, vacilei e a vida cobrou, bem... Lá se foi meu descanço das férias."

d "Boa sorte cara!"

return
