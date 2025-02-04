def cube_volume(side):
    return(side * side * side)
def main():
    sideask = float(input("What is the length of one side of the cube?: "))
    cube_result = cube_volume(sideask)
    print(f"The cube's volume is {cube_result}")
if __name__ == '__main__':
    main()









