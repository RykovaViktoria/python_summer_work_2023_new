# def deco_title(func):
#     def wrapper():
#         res = func()
#         new_res = res.capitalize()
#         return new_res
#     return wrapper
# @deco_title
# def tit():
#     return 'HelLo World'
# print(tit())

def deco_title(func):
    def wrapper(text):
       res=func(text)
       return res.title()
    return wrapper
@deco_title
def hello(text):
    return text
print(hello('sdfsfdfaf asf'))
