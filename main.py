import random

def play():
    words = ['Sudama Potli', 'Avocado', 'Banana', 'apple',  'Guava',  'Lemon', 'Lime', 'Lychee', 'Mango', 'Melon', 'Cantaloupe',  'Watermelon', 'Orange', 'Peach', 'Pineapple', 'Pomegranate', 'Strawberry', 'Tomato', 'Watermelon']
    guess = 3
    for i in range(len(words)):
       words[i]=words[i].lower()
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
    marker[w[visible[1]]]-=1

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
        print("HANGMAN\n")
        if guess==0:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
        elif guess==1:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |         \n"
                  "__|__\n")
        else:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")



if __name__=="__main__" :
    play()




