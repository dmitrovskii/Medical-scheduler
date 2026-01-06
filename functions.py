# lto - list to output 
def youinput(lto, text, limit):

    # Зациклює якщо юзер ввів якусь фігню
    ending = True
    while ending == True:

        output = []
        test = input(text).split()

        # змінна для while
        problem = 0

        for item in test: 
            
            # перетворення даних ліста на інт та прохід фільтрів
            try: 

                index = int(item)

                if 1 <= index <= len(test): # Свідомий баг, зроблений як короткочасна заміна джсон
                    output.append(index - 1)
                else: 
                    print(ertext(item))
                    problem += 1
                    continue

            except ValueError: 
                print(ertext(item))
        
        # умова яка вирішує зациклювати чи ні
        if problem == 0:
            ending = False
        else: 
            ending = True
            clear(1)

    clear(0)
    return output, limit


# Це лишень тест
blablacar = youinput(0, "Please enter numbers:\n", 1)
print(blablacar)

