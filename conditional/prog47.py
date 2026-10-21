def prog47():
    print("1. Python  2. Java  3. C  4. C++  5. JavaScript")
    choice = int(input("Choose your favourite language (1-5): "))
    match choice:
        case 1:
            print("You chose Python - great for AI, data science and scripting")
        case 2:
            print("You chose Java - great for enterprise and Android apps")
        case 3:
            print("You chose C - great for system programming")
        case 4:
            print("You chose C++ - great for games and performance-critical apps")
        case 5:
            print("You chose JavaScript - great for web development")
        case _:
            print("Invalid choice")

prog47()