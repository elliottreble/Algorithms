##BubbleSort is terrible

def BubbleSort(list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0,len(list) - 1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
                print(list)
                i+=1
            else:
                i+=1


list = [1,6,0,8,12,22,45,7,99,100,11,10,20,26,38,201,13,4,3]
BubbleSort(list)
