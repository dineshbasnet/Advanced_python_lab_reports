
# def mul(fx,value):
#     return fx(value) + 4 


# print(mul(lambda x:x*x,4))


# bowl = {
#     "Apple":5,
#     "Banana":7,
#     "Mango":5,
#     "Kiwi":10
# }

# for fruit in bowl:
#     print(f"Fruits are:{fruit.upper()}")
    
    
# Genrators are those function, when required something it gives only that required part only , doesn't stored the whole things in memory , this ensures effient memroy management , save times, reduces complexity

# def my_generator():
#     for i in range(1000000000):
#         return i
        
        
# gen = my_generator()

# print(next(gen))

# for j in gen:
#     print(j)

# Decorators

def greet(fx):
    def mfx(*args,**kwargs): 
        print("Good morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx



def hello():
    print("hello world")
    
def add(a,b):
    print(a+b)
    
    


greet(add)(3,4)
    

