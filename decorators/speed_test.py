from functools import wraps
def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        from time import time
        init = time()
        result = fn(*args, **kwargs)
        finish = time() - init
        print(f"{fn.__name__} runs in: {finish}s")
        return result
    
    return wrapper


@speed_test
def avg(gen_e):
    sum_e = 0
    len_e = 0
    for x in gen_e:
        sum_e += x
        len_e +=1
    
    return sum_e / len_e
    

@speed_test
def avg_list(list_n):
    sum_l = 0
    len_l = 0
    for x in list_n:
        sum_l += x
        len_l +=1
    
    return sum_l / len_l

result = avg(i for i in range(1,80055550))
print(f"The average is : {result}")	

result2 = avg_list([i for i in range(1,80055550)])
print(f"The average is : {result2}")	
