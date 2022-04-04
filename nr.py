from numpy import exp, array, random, dot

ans1 = input("Легко ли Вам заводить новые знакомства?")

if ans1 == "Да":
    count1 = 1
else:
    count1 = 0

ans2 = input("Вы стремитесь придумать что-то новое?")

if ans2 == "Да":

    count3 = 1
else:
    count3 = 0

ans3 = input("Часто ли Вам бывает одиноко?")

if ans3 == "Нет":
    count2 = 1
else:
    count2 = 0

sarray = [0] * 4

ans4 = input("Часто ли Вы задумываетесь о будущем?")

if ans4 == "Да":
    count0 = 1

    sarray[1] = 1
else:
    count0 = 0

    sarray[1] = 0

ans5 = input("Вы креативный человек?")

if ans5 == "Да":
    sarray[0] = 1
else:
    sarray[0] = 0

ans7 = input("Обладаете ли вы упорностью и настойчивостью в достижении определённой цели?")

if ans7 == "Да":
    sarray[2] = 1
else:
    sarray[2] = 0

ans8 = input("Принимаете ли вы разнообразные мнения и факты?")

if ans8 == "Да":
    sarray[3] = 1
else:
    sarray[3] = 0

training_set_inputs = array(
    [[0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1], [1, 0, 1, 0]])
training_set_outputs = array([[0, 1, 1, 1, 0, 1, 1]]).T
random.seed(1)

myarray = [0] * 4

myarray[0] = count0
myarray[1] = count1
myarray[2] = count2
myarray[3] = count3

synaptic_weights = 1 * random.random((4, 1)) - 1
for iteration in range(11000):
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
    # rec1 = 5 / (1 + exp(-(dot(array([1, 1, 1, 1]), synaptic_weights))))
    rec1 = 1 / (1 + exp(-(dot((myarray), synaptic_weights))))
print(rec1)

if rec1 >= 0.998:
    m1 = "ESFP"
    a = [1, 1, 0]
    color = "жёлтый"
    codek = "yellow"
if rec1 >= 0.7 and rec1 < 0.998:
    m1 = "ISTP"
    a = [1, 1, 1]
    color = "оранжевый"
    codek = "orange"
if rec1 >= 0.5 and rec1 < 0.7:
    m1 = "ENTP"
    a = [0, 1, 1]
    color = "фиолетовый"
    codek = "purple"

if rec1 >= 0.4 and rec1 < 0.5:
    m1 = "ESFJ"
    a = [0, 1, 0]
    color = "светло-розовый"
    codek = "bp"

if rec1 > 0.3 and rec1 < 0.4:
    m1 = "INTJ"
    color = "чёрный"
    codek = "black"

if rec1 > 0.2 and rec1 < 0.3:
    m1 = "INFP"
    a = [1, 1, 1]
    color = "светло-голубой"
    codek = "lblue"

if rec1 > 0 and rec1 < 0.2:
    m1 = "ISFJ"
    a = [0, 0, 1]

    color = "белый"
    codek = "white"

print("Ваш тип личности:")
print(m1)
print("Приятный для вас цвет", color)


def ans01():
    ansr1 = input("Принимаете ли Вы мир таким, какой он есть?")

    return ansr1


def ans02():
    ansr2 = input("Часто ли Вы ищите смысл в происходящем?")
    return ansr2


if m1 == "ESFP":
    ans01()
    ans02

f = ans01()
h = ans02()

if f == "Да":
    print("Чаще всего Вы ведёте себя спокойно. Вас трудно разозлить")
else:
    print("Вы крайне импульсивны. Внутри Вас постоянно пылают эмоции")

if ans5 == "Да" and m1 == "ENTP" or m1 == "ISFJ":
    print(
        "Предположительно Вы мыслите рассудительно и умеете быстро выходить из конфликтных ситуаций. Вы достаточно чувстивительны")
else:
    print("Предположительно Вы достаточно решительный человек")

if ans7 == "Да" and m1 == "ESFP" or m1 == "ENTJ":
    print(
        "Предположительно Вы достаточно импульсивны и умеете быстро переключаться между различными видами деятельности. Вы обладаете лидерскими качествами. Вы мыслите аналитично")
else:
    print("Предположительно Вы креативный и предприимчивый человек")

training_set_inputs = array([[1, 1, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0]])
training_set_outputs = array([[1, 0, 1, 0]]).T
random.seed(1)

synaptic_weights = 2 * random.random((4, 1)) - 1
for iteration in range(11000):
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
    # rec1 = 5 / (1 + exp(-(dot(array([1, 1, 1, 1]), synaptic_weights))))
    rec3 = 1 / (1 + exp(-(dot((sarray), synaptic_weights))))

print(rec3)

if rec3 >= 0.99:
    space = "Вы креативный, ориентированный на будущее человек. Самое главное для Вас - достижение своей цели. Для вас важны мнения других людей"

if rec3 >= 0.7 and rec3 < 0.99:
    space = "Вы мыслите стандартно. Для вас приятен обыкновенный, спокойный подход. Иногда случается так, что Вы быстро теряете интерес к какому-либо делу. Для вас важно мнение любого человека"

if rec3 >= 0.4 and rec3 < 0.7:
    space = "Для вас привычен стандартный, шаблонный подход. Вы живёте завтрашним днем, часто ориентируясь на будущее. Достижение цели - главна ямотивация для вас. Но при этом Вы достатоно эгоистичны."

if rec3 >= 0 and rec3 < 0.4:
    space = "Вы креативный человек. Часто вы задумываетесь о том, что произошло с вами в прошлом. Вы ставите себе много целей и достигаете их. Вы эгоистичны, часто думаете только о себе, не смотря на других"

print("Новый результат")
print(space)

training_set_inputs = array([[1, 1, 0], [1, 1, 1], [0, 1, 1], [0, 1, 0]])
training_set_outputs = array([[1, 2, 3, 4]]).T
random.seed(1)

synaptic_weights = 2 * random.random((3, 1)) - 1
for iteration in range(10000):
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))

rec2 = 4 / (1 + exp(-(dot((a), synaptic_weights))))
print(rec2)

f = open('log.txt', 'w')
f.write(ans1 + " " + ans2 + " " + ans3 + " " + ans4 + " " + ans5 + " " + ans4 + " " + ans7 + " " + ans8 + " ")
f.write(m1)
f.close()

