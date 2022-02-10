#Desenvolvedores do jogo: João Pedro e Beatriz.
#Roteiristas do jogo: João Pedro e Beatriz.
#Idealizadores do jogo: João Pedro e Beatriz.
#Integrantes do grupo: João Pedro e Beatriz.
print("║░░░░░░░░░░░░░░░░░░░░░░░░░░░ RISE OF THE AVENGERS ░░░░░░░░░░░░░░░░░░░░░░░░░░░║")
print("Regras:\n»»Você escolherá um vingador para ser.\n»»O objetivo é conseguir mais joias do infinito que Thanos\n"
      "»» Para tomar decisões, digite o número ou letra que corresponderá à alternativa.\n"
      "»» exemplo:(1) alternativa x (2) alternativa y: vocé deve digitar 1 ou 2.\n"
      "»» A cada erro cometido no jogo você dará ao Thanos uma chance de conseguir uma joia.\n»»-Escolha com cuidado, o universo esta em suas mãos.")
print("║░░░░░░░░░░░░░░░░░░░░░░░░░ ESCOLHA SEU VINGADOR ░░░░░░░░░░░░░░░░░░░░░░░░░░░░║")
v = int(input("1-Homem de Ferro\n2-Hulk\n3-Thor\n4-Viúva Negra\n5-Gavião Arqueiro\n6-Capitão América\n Digite Aqui:"))
falha = 0
if v == 1:
    print("Você escolheu o Homem de Ferro.")
    v = "Homem De Ferro"
elif v == 2:
    print("Você escolheu o Hulk")
    v= "Hulk"
elif v == 3:
    print("Você escolheu o Thor")
    v = "Thor"
elif v == 4:
    print("Você escolheu o Viúva Negra")
    v = "Viúva Negra"
elif v == 5:
    print("Você escolheu o Gavião Arqueiro")
    v = "Gavião Arqueiro"
else:
    print("Você escolheu o Capitão América")
    v = "Capitão América"
print(" ███████████████████████████████ PRÓLOGO ███████████████████████████████████\n")
print("Os súditos de Thanos Transmitem um recado à todo planeta Terra.\n SÚDITOS DE THANOS: Salvem o todo poderoso Thanos. Alegrem-se por poderem morrer"
      " para esta grande causa. Thanos pretende aniquilar metade de todas as criaturas vivas no Universo para manter o equilíbrio."
      "\n O plano de Thanos consiste em juntar as 6 joias do infinito e obter poder ilimitado. Rendam-se e nos entreguem as joias que estão na Terra.")
print("Ao ouvir essa notícia você decide contactar o restante dos Vingadores, vocês devem tomar uma decisão a cerca do ocorrido. O primeiro passo é a joia do tempo "
      "que esta com Doutor Estranho.\n")


print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » FASE1 « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
print("APERTE ENTER PARA CONTINUAR")
input()
esc1 = str(input("Ao chegarem no QG do Doutor Estranho, para entrar é necessário descriptografar a senha dos vingadores que se da pelo enigma:\n"
                 "A verdade esta na casa anterior.\n DECIFRE: OJDL GVSZ \n"))

if esc1 == "NICK FURY" or esc1 == "Nick Fury" or esc1 == "nick fury":
    print("A porta se abriu")
    print("Ao entrarem, se deparam com uma grande escadaria. Doutor estranho está logo à porta e parece aflito \n"
          "DOUTOR ESTRANHO: Eu preciso proteger a JOIA DO TEMPO, antes que Thanos a leve, porém, não confio na capacidade de vocês de protege-la. \n")
    print(v,": Nós podemos protege-la tanto quanto você. Podemos provar. \n"
          "DOUTOR ESTRANHO: Tudo bem, se conseguirem decifrar este feitiço de proteção à joia, a deixo com vocês. \n"
          "Se atende às instruções: A combinação de poções deve gerar uma única poção com a cor da VITALIDADE. Sendo assim, quais porções devem ser misturadas? \n"
          "(A)Amor (Poção vermelha)\n"
          "(B)Energia (Poção Amarela)\n"
          "(C)Harmonnia (Poção Azul)\n"
          "As poções a serem misturadas são:" )
    esc11= str(input())
    if esc11=="bc" or esc11=="BC" or esc11=="cb" or esc11=="CB":
        print("Você criou a poção da vitalidade de cor verde e agora, possui mais conhecimentos para guardar a joia do tempo. O doutor estranho conta com sua ajuda")
    else:
        print("Você não conseguiu criar a poção e o Doutor estranho não pode deixar a Joia do Tempo em suas mãos")
        falha= falha +1        
else:
    falha = falha + 1
    print("Resposta errada.")
    print("Demorou demais! Thanos conseguiu a joia do Tempo.")

    
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » FASE 2 « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
print("APERTE ENTER PARA CONTINUAR")
input()
print("Fase 2: Achar a joia com o visão.")
print("Vião e Feiticeira Escarlate se afastaram dos vingadores pois temiam os perigos em que sempre estavam submetidos."
      "É necessário convencer Visão à se juntar aos vingadores, pois é a unica maneira de proteger a Joia das mãos de Thanos.\n"
      "FEITICEIRA ESCARLATE: Nós não podemos nos juntar à vocês, é muito perigoso!\n")
esc2= str(input("ESCOLHA SUA RESPOSTA:\n"
          "(A) Tem razão, não vale a pena colocar a vida de vocês em risco\n"
          "(B) É mais perigoso ainda se vocês continuarem aqui.\n"))
esc3 = 0
f = 0
if esc2=="B" or esc2=="b":
    esc3=str(input("FEITICEIRA ESCARLATE: Vou me juntar a vocês só se prometerem que protegerá o visão com a sua vida \n"
                "(A)Eu prometo\n"
                "(B)Não posso prometer algo do tipo\n"))
    if esc3 == "a"  or esc3 == "A":
        print("Agora feiticeira e visão confiam em você. Voce está com a joia.")
    else:
        print("Visão e feiticeira não se juntam a você e Thanos os acha e pega a joia.")
        falha = falha + 1
else:
    print("Agora a Feiticeira e Visão estão vúlneráveis e Thanos pode atacá-los em qualquer momento")
    falha = falha + 1


print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » FASE 3 « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ \n")
print("APERTE ENTER PARA CONTINUAR")
input()
print("Fase 3: Achar a joia da realidade no museu do colecionador.")
print("Você descobre que a joia esta em um museu, numa parte secreta com itens cósmicos raros\n O primeiro desafio é passar pelo guardião."
      "GUARDIÃO: Saudações, a senha por favor.")
esc4 = str(input("Digite a resposta certa da pergunta para entrar.\n Qual um dos itens mais colecionado do mundo?\n A)Figurinhas\n B)Selos de carta\n C)Canetas\n"))
f2 = 0
if esc4 == "B" or esc4 == "b":
    print("Resposta correta, entre.")
    esc5 = str(input("Ao entrar na sala encontram a joia em uma caixa que se abre apenas com uma senha. A senha possui um padrão tal que::3,6,10,15,21,28,36,x,y,z"
                     " \n(DIGITE A SEQUÊNCIA INTEIRA COMPLETANDO AS INCOGNITAS X,Y E Z)\n SENHA:"))
    if esc5 == '361015212836455566' or esc5 == '3,6,10,15,21,28,36,45,55,66':
        print("Resposta correta a caixa se abriu. Agora você possui a joia da realidade.")
    else:
        print("Resposta errada.")
        f2 = f2 + 1
else:
    print("Resposta errada. Thanos conseguiu a joia.")
    falha= falha+1
    f2 = f2 + 1
if f2 == 2 or f == 1:
    falha = falha + 1
else:
    falha = falha + 0
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » FASE 4 « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")


print("APERTE ENTER PARA CONTINUAR")
input()
print("A próxima joia (Joia do espaço) se encontra com Loki, filho de Odin, porém ele não quer entregar aos Vingadores e por isso você deve escolher uma forma de derrota-lo\n"
      "e obter a joia\n SELECIONE DUAS HABILIDADES sabendo que: Loki tem uma incrivel habilidade mágica, porém possui muitas inseguranças e fraquezas pessoais.")
esc8 = str(input("(1)Força. (2)Vitalidade. (3)Persuasão. (4)Resistência mágica.\n"))
if esc8 == '34' or esc8 == '43' or esc8=='3 e 4' or esc8=='4 e 3':
    print(v,"persuadiu Loki com o diálogo fazendo-o se sentir inseguro e inferior, e quando ele resolveu atacar você possuia resistência\n"
          "necessária para lutar contra ele.")
    esc81= str(input("Loki está com VITALIDADE em 100 e com PODER ARCANO em 180. Escolha as habilidades a serem utilizadas:\n"
                 "(A)160 FORÇA\n(B)130 DESTREZA\n(C)170 INTELIGÊNCIA\nHabilidade 2:\n(A)80 VITALIDADE\n(B)100 ARMADURA \n ESCOLHA A COMBINAÇÃO DE HABILIDADE(EX: AB):"))
    if esc81=='AA' or esc81=='aa':
        print('Com Força e Vitalidade, Loki não conseguiu resistir por muito tempo, o que fez com que você conseguisse a joia')
    elif esc81=='AB' or esc81=='ab':
        print('As investidas em Loki causaram dano, porém a Armadura não lhe garantiu resistência mágica')
        falha= falha+1
    elif esc81=='ba' or esc81=='BA':
        print('Você conseguiu destrair loki por bastante tempo, mas apenas a vitalidade não lhe garante a vitória na luta')
        falha= falha+1
    elif esc81=='bb' or esc81=='BB':
        print('Sua destreza distraiu Loki por um bom tempo, porém a Armadura não lhe garantiu resistência mágica')
        falha= falha+1
    elif esc81=='ca' or esc81=='CA':
        print('Com inteligência e vitalidade você consegue derrotar loki e obter a joia do espaço')
    else:
        print('Com inteligência e armadura foi possivel resistir aos ataques mágicos de Loki, fazendo com que você ganhasse tempo e conseguisse a joia do Espaço')
        
else:
    print("Você escolheu as habilidades erradas e não foi páreo para o duelo contra Loki.")
    falha = falha + 1

    
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » FASE 5 « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")


print("APERTE ENTER PARA CONTINUAR")
input()
print("Fase 4: Achar a joia do Poder no planeta Xandar.")
print("A joia do poder esta localizada no planeta Xandar com a organização Nova Corps.\nÉ necessário que viaje até lá "
      "e a busque com urgência.")
esc6 = int(input("Xandar por ser um planeta ligado à música possui sua cordenadas referentes às notas musicais em sua ordem.\n"
                 "Sendo fá =49, dó = 125, sol = 320, mi = 33, lá = 440, si = 5,ré = 4. Digite a ordem das coordenadas:"))
f3 = 0
if esc6 == 125433493204405:
    print("Coordenadas corretas, partindo!.")
    esc7 = str(input("Ao chegarem no planeta se encontram com os líderes da Nova Corps, porém eles só entregarão a joia à vocês se desvendarem o segredo:\n"
                 "Qual o instrumento que pode ser ouvido mas não tocado?:."))
    if esc7 == "voz" or esc7 == "Voz" or esc7 == "VOZ":
        print("LIDER DA NOVA CORPS: Você acertou, agora confiaremos a joia à você.")
    else:
        print("Você não conseguiu pegar a joia e Thanos a pegou.")
        f3 = f3 + 1
else:
    print("Coordenadas incorretas.Vocês não foram capazes de chegar a Xandar antes de Thanos")
    f3 = f3 + 1
if f3 == 2 or f3== 1:
    falha = falha + 1
else:
    falha = falha + 0


print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » FASE 6 « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")


print("Agora é a hora de encontrar a última joia do infinito (joia da Alma), e ela se encontra com Adam Warlock na Terra, Ilha Shard(Oceano Atlântico)\n"
      "Adam esta em seu casulo artificial quando você chega para o perguntar sobre a joia, é necessário abrir casulo o qual ele se encontra\n"
      "decifrando o código:")
esc8 = int(input(" 1\n 11\n 21\n 1211\n 111221\n 312211\n Qual o próximo número da sequência?"))
if esc8 == 13112221:
    print("Casulo se abriu e Adam Warlock despertou.")
    print("ADAM: Como ousam me despertar, digam agora o que querem ou serão aniquilados pelo meu poder.")
    print(v,"Precisamos da joia que você guarda, para impedir Thanos de consegui-la e destruir metade do Universo.")
    esc9 = int(input("Adam Warlock parece desconfiado e tende a não aceitar a proposta, você tem duas opções:\n (1)Lutar contra Adam.\n (2)Convence-lo a se juntar aos vingadores.\n"))
    if esc9 == 1:
        falha = falha + 1
        print("Você perde a Joia pois Adam utilizou seus poderes de manipulação da realidade e energia para neutralizar você e sua equipe."
              "Agora o universo não contará mais com você. Thanos consequentemente pega a joia.")
    else:
        print(v,":conta o plano de Thanos e Adam decide ajudar os vingadores.\n")
else:
    print("Você errou e thanos o achou e conseguiu a joia.")
    falha = falha + 1
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » FASE FINAL « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
print("Nesse momento do jogo, você poderá ter três finais diferentes:\n"
      "Se falhou muitas vezes, Thanos possui mais joias do que os Vingadores, e por isso, não poderão fazer nada contra ele.\n"
      "Se está com mais joias que Thanos, ele não poderá lutar contra os Vingadores, já que estará em uma desvantagem muito grande.\n"
      "Se está com a mesma quantidade de joias que Thanos, você e os Vingadores travarão a batalha final\n."
      "APERTE ENTER PARA ANALISAR O DESEMPENHO NO JOGO:")
input()
j= 6-falha
print('Vingador escolhido',v)
print("Joias coletadas:" ,j)
print("Joias com Thanos:", falha)
if j>=4:
    print("Parabéns", v ,"Você liderou sabiamente a equipe dos Vingadores e juntos conseguiram", j, "joias do infinito; o suficiente para deter Thanos e impedir que\n"
          "ele concretize seu plano. Agora as joias estarão devidamente proteginar na torre dos Avengers.")
    print("Aperte ENTER para finalizar o jogo")
    input()
elif falha>=4:
    print(v,", você não foi capaz de liderar a equipe dos Vingadores nessa missão. Thanos está com mais joias e lutar contra ele é inútil. VOCÊ PERDEU")
    print("Aperte ENTER para finalizar o jogo")
    input()
else:
    print("Os Vingadores e Thanos possuem a mesma quantidade de Joias. Vocês agora travarão a batalha final!!!")
    print("████████████████████████████████████ FASE EXTRA ████████████████████████████████████\n")
    print("Thanos vai até a torre dos vingadores para tentar pegar as últimas joias e concluir seu objetivo.")
    print("A melhor opção agora é frentar Thanos, porém ainda há escolhas a se fazer.\n Você pode pedir reforços do Adam ou dos Vingadores.\n"
          "Adam pode evacuar a torre dos Vingadores rápido e proteger as pessoas, mas não seria uma ajuda tão útil contra Thanos.\n"
          "Mas os Vingadores poderiam o ajudar a derrotar Thanos de uma forma mais eficiente. Porém algum deles pode acabar não saindo vivo.")
    esc9 = int(input("(1) Para pedir ajuda de Adam.\n(2) Para pedir ajuda dos Vingadores.\n"))
    if esc9 == 1:
        print("Adam não salva as pessoas da torre pois você solicitou ajuda na luta contra Thanos.\n"
              "Thanos ativa uma das joias na sua direção mas Adam o protege com a sua energia.")
        esc10 = int(input("(1)Você escolhe canalizar a energia para adquirir mais poder +180 resistência mágica.\n"
                          "(2)Ou imobilizar Thanos e tentar pegar as joias que com ele estão. +150 de força -70 de resistência mágica."))
        if esc10 == 1:
            print("Aperte enter para dar uma investida em Thanos. +150 de força -90 de Vitalidade.")
            input()
            print("Thanos esta atordoado, Adam aproveita seu ataque golpeando Thanos que cai no chão. \n() finalizar")
            input()
            print("Parabén você venceu o Thanos, recuperou as joias e salvou o Universo!")
        else:
            print("Thanos resiste e revida. Adam manipula a realidade para confundir Thanos e então você da o golpe final.\n"
            "() finalizar")
            input()
            print("Parabén você venceu o Thanos, recuperou as joias. Salvou o Universo!")
    else:
        print(v," e o Restante dos Vingadores decidem iniciar os ataques a Thanos.")
        esc11 = int(input("(1)Sequência de combos individuais +100 de força +50 de inteligência\n"
                          "(2)Ataque simultâneo, todos juntos, +100 de destreza -50 de vitalidade."))
        if esc11 == 1:
            print("Vocês executam uma série de golpes combinados em Thanos. no entanto por ser muito poderoso e resistente, ele canaliza todo o poder das joias que possui\n"
                  "e realiza um ataque de energia que cai sobre os vingadores com muita força, finalmente os derrotando. Perdeu o jogo!")
        else:
            print("A equipe dos Vingadores desfere golpes conjuntos contra Thanos, ele não consegue absorver tantos golpes de uma vez e acaba sendo atordoado\n",v,
                  "então finaliza Thanos com um último poderoso golpe, trazendo paz ao universo de novo.\n"
                  "PARABÉNS, VOCÊ GANHOU!")
print("Aperte ENTER para finalizar o jogo")
input()


        

            

