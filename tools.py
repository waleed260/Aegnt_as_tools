from agents import function_tool

@function_tool
def plus (n1:int , n2:int)-> str:
     """ This is plus function
     arg:
     n1:int
     n2:int
     return str
     """
     print("plus tool is running")
     return f"your answer is {n1+n2}"
    
@function_tool
async def subtract (n1:int , n2:int)-> str:
     """ This is plus subtract
     arg:
     n1:int
     n2:int
     return str
     """
     print("subtract tool is running")
     return f"your answer is {n1-n2}"
    