---
id: loops
title: Loops
sidebar_position: 3
---

# Loops: Doing Things Many Times!

Imagine you have a task you need to do over and over again. For example, maybe you want to print "Hello!" five times, or maybe you want to count from 1 to 10. Doing these tasks manually would be a bit boring, right?

In programming, we have something called **loops** that help us repeat actions easily. A loop is like a magical machine that keeps doing something until a certain condition is met.

## The `for` Loop: Counting Through Collections

One very common type of loop is the `for` loop. Think of it like a friend who helps you go through a list of items, one by one, and do something with each item.

Let's say you have a list of fruits and you want to say "I love [fruit]!" for each one. Without a loop, you'd have to write:

```python
print("I love apple!")
print("I love banana!")
print("I love cherry!")
```

But with a `for` loop, it's much simpler and neater!

### Example: Our Fruit Loop!

Here's how you can use a `for` loop in Python to go through a list of fruits:

```python
# Here's our list of fruits
fruits = ["apple", "banana", "cherry"]

# This is our 'for' loop!
# It says: "For each 'fruit' in our 'fruits' list, do the following:"
for fruit in fruits:
    # This line will run once for 'apple', then once for 'banana', and so on.
    print(f"I love {fruit}!")
```

**What's happening here?**

1.  `fruits = ["apple", "banana", "cherry"]`: We first create a "list" of fruits. You can think of a list as a collection of items, like a shopping list.
2.  `for fruit in fruits:`: This is the start of our loop.
    *   `for`: This keyword tells Python we're starting a `for` loop.
    *   `fruit`: This is a temporary "label" we give to each item as we go through the list. In the first round, `fruit` will be "apple". In the second, it will be "banana", and so on.
    *   `in fruits`: This tells the loop which collection of items (our `fruits` list) to go through.
3.  `print(f"I love {fruit}!")`: This is the action that gets repeated. Notice how we use our temporary `fruit` label inside the `print` statement.

When you run this code, you'll see:

```
I love apple!
I love banana!
I love cherry!
```

Isn't that neat? Loops save us a lot of typing and make our programs much more powerful when we need to do repetitive tasks!