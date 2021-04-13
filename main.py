import random

def play():
    words = ['Apricot', 'Avocado', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant', 'Blueberry', 'Currant', 'Cherry', 'Cherimoya', 'Clementine', 'Date', 'Damson', 'Durian', 'Eggplant', 'Elderberry', 'Feijoa', 'Gooseberry', 'Grape', 'Grapefruit', 'Guava', 'Huckleberry', 'Jackfruit', 'Jambul', 'Kiwi fruit', 'Kumquat', 'Legume', 'Lemon', 'Lime', 'Lychee', 'Mango', 'Mangostine', 'Melon', 'Cantaloupe',  'Watermelon', 'Rock melon', 'Nectarine', 'Orange', 'Peach', 'Pear', 'Pitaya', 'Physalis', 'Pineapple', 'Pomegranate', 'Raisin', 'Raspberry', 'Rambutan', 'Redcurrant', 'Satsuma', 'Strawberry', 'Tangerine', 'Tomato', 'Watermelon']
    guess = 3
    n = random.randint(0, len(words) - 1)
    w = words[n]
    marker = {}

    for l in w:
        if l in marker:
            marker[l] += 1
        else:
            marker[l] = 1
    visible = [random.randint(0,int(len(w)/2)-1),random.randint(int(len(w)/2),len(w) - 1)]
    marker[w[visible[0]]] = marker[w[visible[0]]] - 1

    def show_letter(w, to_show):
        s = ""
        c = 0
        for i in range(len(w)):
            if i in to_show:
                s += w[i] + " "
            else:
                s += "_ "
                c = c + 1
        return [s, c]

    print("Welcome to Fruit Hangman, Though we will not hang anyone\n")
    print("You got only three wrong guess to make the word")

    while True:
        print("Guess remaining: %s" % (guess))
        if guess == 0:
            print("You lost ")
            print("Correct Answer   :%s" % (w))
            break
        shown = show_letter(w, visible)
        print(shown[0])
        if shown[1] == 0:
            print("Well Played")
            print("You are master %s " % (str.upper(w)))
            return n
            break
        player = input("Your letter: ")
        if player in marker and marker[player] > 0:
            print("correct letter\n")
            marker[player]-=1
            for i in range(len(w)):
                if i not in visible:
                    if w[i] == player:
                        visible.append(i)
                        break
        else:
            print("Incorrect Guess :")
            guess = guess - 1

if __name__=="__main__" :
    play()



