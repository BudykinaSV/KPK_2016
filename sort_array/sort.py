#сортировка  (fail - перевод НЕУДАЧА)
def sort_test(my_sort):
    import random
    A=[1,2,3,4,5,6]
    A_ans=[1,2,3,4,5,6]
    my_sort(A)
    print('test 1:'+('OK' if A==A_ans else 'Fail'))

    A=[-1,-2,-3,-4,-5,-6]
    A_ans=[-6,-5,-4,-3,-2,-1]
    my_sort(A)
    print('test 2:'+('OK' if A==A_ans else 'Fail'))

    A=[-1,4,-3,2,-5,6]
    A_ans=[-5,-3,-1,2,4,6]
    my_sort(A)
    print('test 3:'+('OK' if A==A_ans else 'Fail'))

    A=[100]
    A_ans=[100]
    my_sort(A)
    print('test 4:'+('OK' if A==A_ans else 'Fail'))

    A=[]
    A_ans=[]
    my_sort(A)
    print('test 5:'+('OK' if A==A_ans else 'Fail'))

    A=[1]*100
    A_ans=[1]*100
    my_sort(A)
    print('test 6:'+('OK' if A==A_ans else 'Fail'))

    A=[random.randint(1,100) for i in range(1000)]
    A_ans=sorted(A) #сортирует массив и не портит исходный
    my_sort(A)
    print('test 7:'+('OK' if A==A_ans else 'Fail'))


def noting(A): #для проверки текстинга
    pass

def sort_puzyrek(A): #сортировка пузырьком
    N=len(A)
    for prohod in range (1,N):
        for i in range(N-prohod):
            if A[i]>A[i+1]:
                x=A[i]
                A[i]=A[i+1]
                A[i+1]=x

def sort_wybor(A): #сортировка выбором
    N=len(A)
    for pos in range (0,N-1):
        min=pos
        for i in range(pos+1,N):
            if A[i]<A[min]:
                min=i
        A[pos],A[min]=A[min],A[pos]


if __name__=='__main__':
    sort_test(sort_puzyrek)
    print("\n")
    sort_test(sort_wybor)

