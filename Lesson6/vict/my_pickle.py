import pickle, datetime

q1 = input("Как вас зовут?")
q2 = input("Ваш возраст?")
q3 = input("Ваш пол?")

date = datetime.datetime.now().strftime("%H:%M:%S")
my_dict = {"date": date, "q1": q1, "q2": q2, "q3": q3}

with open('answer.pickle', 'wb') as file:
    pickle.dump(my_dict, file)

with open('answer.pickle', 'rb') as file:
    t = pickle.load(file)
    if q1 == "Катя":
        score = 1
    else:
        score = 0
    if q2 == "30":
        score1 = 1
    else:
        score1 = 0
    if q3 == "Женский":
        score2 = 1
    else:
        score2 = 0
    score_sum = score + score1 + score2
    print(f"Ваш результат: {score_sum} балла")