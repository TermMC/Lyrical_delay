# this is a program to add 'lyrical' delay to poems (or any text)



def lyrical_delay(poem, amount):

    jones = poem.split()
    print(len(jones))
    for i in range(len(jones)):
        n = 1
        while True:
                try:
                    y = i % amount
                    x = i+y+amount*n
                    jones[x]
                    jones = jones[0:x]+[jones[i]]+jones[x:]  #this inserts the word at the point
                    n = n+1  # this moves the pointer to the next point
                except IndexError:
                    jones = jones +[jones[i]]
                    #print(str(i) + '\n' + str(jones) + '\n')
                    break
                blank_list = jones
    new_poem = ' '.join(blank_list)
    return(new_poem)

file = open(r'C:\Users\JubJubRubALugs\Desktop\shorterdelaypoem.txt', 'r')
content = file.read()
file.close()

new_poem = lyrical_delay(content, 10)
0
#print(new_poem)
second_file = open(r'C:\Users\JubJubRubALugs\Desktop\roundtwo.txt', 'w')
second_file.write(new_poem)
second_file.close()
