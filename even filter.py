
def check_even(number):
    if number % 2 == 0:
          return True 
    else: 

     return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=list(filter(check_even,numbers))
print(result)