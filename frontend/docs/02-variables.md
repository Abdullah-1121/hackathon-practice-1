---
id: 'variables'
title: 'Variables'
sidebar_position: 2
---

## What are Variables?

Imagine you have a bunch of boxes, and you want to store different things in them. To remember what's inside each box, you'd probably put a label on it, right? Maybe one box says "My Favorite Books," and another says "Snacks for the Movie."

In programming, **variables** are just like those labeled boxes! They are containers that hold information, and you give them a name (the label) so you can easily find and use that information later.

This information can be many different things: numbers, text, true/false values, and more.

### Why Do We Need Variables?

Variables are super useful because they help us:
*   **Store data:** Keep track of things like a user's name, a score in a game, or the price of an item.
*   **Make our code flexible:** If a value changes (like a user's age next year), we only need to update it in one place (the variable), and every part of our program that uses that variable will automatically get the new value.
*   **Understand our code better:** Giving meaningful names to variables makes your code easier to read and understand, both for you and for others.

### How Do We Use Variables? (A Python Example!)

Let's see variables in action with a simple Python example. Python is a friendly programming language, perfect for beginners!

To create a variable in Python, you simply choose a name, use an equals sign (`=`), and then put the value you want to store.

```python
# Here, 'greeting' is our variable (the labeled box)
# And "Hello, world!" is the information we're storing inside it (the content)
greeting = "Hello, world!"

# 'lucky_number' is another variable, holding a number
lucky_number = 7

# We can then use these variables
print(greeting) # This will "open the box" named 'greeting' and show its content
print("My lucky number is:", lucky_number) # We can also combine text with our variable

# We can even change the content of a variable!
lucky_number = 10 # Now, our 'lucky_number' box holds a new value

print("My new lucky number is:", lucky_number)
```

**Explanation of the Code:**

1.  `greeting = "Hello, world!"`: We create a variable named `greeting` and store the text "Hello, world!" inside it. Text in programming is often called a "string" (because it's a string of characters).
2.  `lucky_number = 7`: We create another variable called `lucky_number` and store the number `7` in it.
3.  `print(greeting)`: The `print()` command is like asking Python to show you what's inside the `greeting` box.
4.  `print("My lucky number is:", lucky_number)`: Here, we're printing some fixed text along with the value from our `lucky_number` variable.
5.  `lucky_number = 10`: We can change what's inside our `lucky_number` box. Now, instead of `7`, it holds `10`.

See? Variables are just helpful labels for the information your program needs to remember. As you continue your coding journey, you'll find them everywhere!
