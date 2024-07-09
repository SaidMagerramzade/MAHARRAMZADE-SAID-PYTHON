# MAHARRAMZADE SAID
# PYTHON
"""Задание
Составьте алгоритм
Если введенное число больше 7, то вывести “Привет”
Если введенное имя совпадает с “Вячеслав”, то вывести “Привет, Вячеслав”, если нет, то вывести
'Нет такого имени'
На входе есть числовой массив, необходимо вывести элементы массива кратные 3"""


def entered_number(number):
    if number > 7:
        print("“Привет”")

number = int(input("Enter a number: "))


def entered_name(name):
    if name == "Вячеслав":
        print("Привет, Вячеслав")
    else:
        print("Нет такого имени")

name = input("Enter a name: ")

def check_list(numbers):
    for num in numbers:
        if num % 3 == 0:
            print(num)

elements_input = input("Enter the list of numbers separated by spaces: ").split()
elements = [int(x) for x in elements_input]

entered_number(number)
entered_name(name)
check_list(elements)



"""Дана скобочная последовательность: [((())()(())]]
Можно ли считать эту последовательность правильной?
Если ответ на предыдущий вопрос “нет”, то что необходимо в ней изменить, чтобы она стала правильной?
"""

def check_balanced(expr):
    stack = []
    for char in expr:
        if char in ['[','(','{']:
            stack.append(char)
        else:
            if not stack:
                return False
            curreny_char = stack.pop()
            if curreny_char == '(':
                if char != ')':
                    return False
                
            if curreny_char == '{':
                if char != '}':
                    return False
                
            if curreny_char == '[':
                if char != ']':
                    return False

    if stack:
        return False
    else:
        return True
sequence = "[((())()(())]]"
print(f"Is the sequence '{sequence}' balanced? {'Yes' if check_balanced(sequence) else 'No'}")

check_balanced(sequence)