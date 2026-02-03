# function with no args no return
def arc():
  print("archana")
arc()

#function with args but no return
def arc(name,age):
  print("hello",name)
  print("im",age,"years old")
arc("archana",17)

#function with args and return val
def arc(a,b):
 return a+b
sum=arc(10,13)
print(sum)

#sample example of finding average 
def avrg(marks):
 a=sum(marks)
 b=len(marks)
 avg=a//b
 return avg
marks=[78,67,89,56,90]
print("average:",avrg(marks))
