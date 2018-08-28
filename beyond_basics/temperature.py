# my solution
# temperatures = [10, -20, -289, 100]
# def c_to_f(c):
#     if c < -273.15:
#         return "That temperature doesn't make sense!"
#     else:
#         f = c* 9/5 + 32
#         return f
# with open("temperature.txt", "w") as myfile:
#     for t in temperatures:
#         myfile.write(str(c_to_f(t)) + "\n")
        #print(c_to_f(t))

# better solution
temperatures = [10,-20,-289,100]

def writer(temperatures, filepath):
    with open(filepath, 'w') as file:
        for c in temperatures:
            if c > -273.15:
                f = c* 9/5 + 32
                file.write(str(f) + "\n")

writer(temperatures, "temps.txt") #Here we're calling the function, otherwise no output will be generated
