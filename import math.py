N = int(input())

if 1<= N <= 1000:
    for _ in range(N):
        question = input() 
        if question == "P=NP":
            #TODO add to list and print list at end
        else:
            a, b = map(int, question.split('+'))
            if 0 <= a <= 1000 and 0 <= b <= 1000:
                print(a+b)