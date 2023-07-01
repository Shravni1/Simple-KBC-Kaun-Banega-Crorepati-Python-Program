questions = [
    [
        "Which data structure was used to create Facebook?",
        "Array",
        "Linked list",
        "Stack",
        "Graph",
        "None",
        4
    ],
    [
        "What is the time complexity of inserting an element at the end of an array?",
        "O(1)",
        "O(log n)",
        "O(n)",
        "O(n^2)",
        "None",
        1
    ],
    [
        "Which data structure follows the Last-In-First-Out (LIFO) principle?",
        "Array",
        "Queue",
        "Stack",
        "Linked list",
        "None",
        3
    ],
    [
        "What is the worst-case time complexity of searching in a binary search tree?",
        "O(1)",
        "O(log n)",
        "O(n)",
        "O(n^2)",
        "None",
        2
    ],
    [
        "Which data structure is used in Depth-First Search (DFS) algorithm?",
        "Queue",
        "Stack",
        "Heap",
        "Graph",
        "None",
        2
    ],
    [
        "What is the time complexity of the Bubble Sort algorithm?",
        "O(n)",
        "O(n^2)",
        "O(log n)",
        "O(1)",
        "None",
        2
    ],
    [
        "Which algorithm is used to find the shortest path in a weighted graph?",
        "Dijkstra's algorithm",
        "Breadth-First Search (BFS)",
        "Depth-First Search (DFS)",
        "Binary Search",
        "None",
        1
    ],
    [
        "What is the primary key in a database table?",
        "A key that uniquely identifies a record",
        "A key used for foreign key constraints",
        "A key used for indexing purposes",
        "A key that is commonly used for sorting",
        "None",
        1
    ],
    [
        "What is the purpose of a database index?",
        "To improve data integrity",
        "To provide backup and recovery",
        "To enforce data constraints",
        "To improve query performance",
        "None",
        4
    ],
    [
        "What is the syntax to declare and initialize a list in Python?",
        "list = []",
        "list = {}",
        "list = ()",
        "list = [1, 2, 3]",
        "None",
        4
    ],
    [
        "Which keyword is used to define a function in Python?",
        "function",
        "def",
        "define",
        "fun",
        "None",
        2
    ],
    [
        "What is the output of the following code snippet?\nprint(3 * 'abc')",
        "abcabcabc",
        "abc",
        "3abc",
        "Syntax Error",
        "None",
        1
    ],
    [
        "Which programming language is often used for system programming and embedded systems?",
        "Java",
        "Python",
        "C",
        "JavaScript",
        "None",
        3
    ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 6400000, 125000, 500000, 10000000]
money = 0

for i in range(len(questions)):
    q = questions[i]
    print(f"\n\nQuestion for Rs.{levels[i]}:")
    print(q[0])  # Display the question
    print(f"a. {q[1]}       b. {q[2]}")
    print(f"c. {q[3]}       d. {q[4]}")
    reply = input("Select your answer from the given options (a, b, c, d) or enter '0' to quit: ")

    if reply == '0':#for quit 
        money = levels[i-1]
        break

    if reply == 'a':#for choose an option 
        answer = 1
    elif reply == 'b':
        answer = 2
    elif reply == 'c':
        answer = 3
    elif reply == 'd':
        answer = 4
    else:
        print("Invalid input! Please select a valid option.")
        continue

    if answer == q[6]:
        print(f"Absolutely Correct answer! Congratulations! You won Rs.{levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 13:
            money = 10000000
    else:
        print("Oops! Wrong answer!")
        break

print(f"Your take home money is {money}")
