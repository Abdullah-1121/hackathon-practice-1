---
id: 007
title: Create Loops Doc for Beginners
stage: general
date_iso: 2025-11-26
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-living-book-rag
user: |
  Generate the content for '03-loops.md' in `frontend/docs/`. This file should explain loops in programming for absolute beginners. Include a frontmatter with id: 'loops', title: 'Loops', and sidebar_position: 3. Provide a simple Python code example with a `for` loop.
command: |
  print(default_api.Write(content = "---\\nid: loops\\ntitle: Loops\\nsidebar_position: 3\\n---\\n\\n# Loops: Doing Things Many Times!\\n\\nImagine you have a task you need to do over and over again. For example, maybe you want to print \\"Hello!\\" five times, or maybe you want to count from 1 to 10. Doing these tasks manually would be a bit boring, right?\\n\\nIn programming, we have something called **loops** that help us repeat actions easily. A loop is like a magical machine that keeps doing something until a certain condition is met.\\n\\n## The `for` Loop: Counting Through Collections\\n\\nOne very common type of loop is the `for` loop. Think of it like a friend who helps you go through a list of items, one by one, and do something with each item.\\n\\nLet\\'s say you have a list of fruits and you want to say \\"I love [fruit]!\\" for each one. Without a loop, you\\'d have to write:\\n\\n```python\\nprint(\\"I love apple!\\")\\nprint(\\"I love banana!\\")\\nprint(\\"I love cherry!\\")\\n```\\n\\nBut with a `for` loop, it\\'s much simpler and neater!\\n\\n### Example: Our Fruit Loop!\\n\\nHere\\'s how you can use a `for` loop in Python to go through a list of fruits:\\n\\n```python\\n# Here\\'s our list of fruits\\nfruits = [\\"apple\\", \\"banana\\", \\"cherry\\"]\\n\\n# This is our \\'for\\' loop!\\n# It says: \\"For each \\'fruit\\' in our \\'fruits\\' list, do the following:\\"\\nfor fruit in fruits:\\n    # This line will run once for \\'apple\\', then once for \\'banana\\', and so on.\\n    print(f\\"I love {fruit}!\\")\\n```\\n\\n**What\\'s happening here?**\\n\\n1.\\n`fruits = [\\"apple\\", \\"banana\\", \\"cherry\\"]`: We first create a \\"list\\" of fruits. You can think of a list as a collection of items, like a shopping list.\\n2.\\n`for fruit in fruits:`: This is the start of our loop.\\n*\\n`for`: This keyword tells Python we\\'re starting a `for` loop.\\n*\\n`fruit`: This is a temporary \\"label\\" we give to each item as we go through the list. In the first round, `fruit` will be \\"apple\\". In the second, it will be \\"banana\\", and so on.\\n*\\n`in fruits`: This tells the loop which collection of items (our `fruits` list) to go through.\\n3.\\n`print(f\\"I love {fruit}!\\")`: This is the action that gets repeated. Notice how we use our temporary `fruit` label inside the `print` statement.\\n\\nWhen you run this code, you\\'ll see:\\n\\n```\\nI love apple!\\nI love banana!\\nI love cherry!\\n```\\n\\nIsn\\'t that neat? Loops save us a lot of typing and make our programs much more powerful when we need to do repetitive tasks!", file_path = "D:\\abdullah\\claude_1\\hackathon-book\\frontend\\docs\\03-loops.md"))
labels:
  - documentation
  - docusaurus
  - loops
  - python
  - beginner
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - D:\abdullah\claude_1\hackathon-book\frontend\docs\03-loops.md
tests_yaml: null
response_text: |
  {"Write_response": {"result": "File created successfully at: D:\\abdullah\\claude_1\\hackathon-book\\frontend\\docs\\03-loops.md"}}
outcome: ""
evaluation: ""
---