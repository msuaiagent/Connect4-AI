# Week 6: Improving Your AI Through Strategy

Last week, you built your very first AI agent.

Although your AI can now play complete games of Connect 4, it still makes very simple decisions.

This week, you'll begin improving your AI by teaching it to recognise better moves.

Rather than copying a predefined algorithm, you'll improve your AI step by step using strategic thinking.

After every improvement, you'll test your AI and observe how its behaviour changes.

---

# Learning Objectives

By the end of this week, you should be able to:

- Identify weaknesses in your AI.
- Improve your AI using simple strategies.
- Test whether your improvements actually help.
- Explain why one strategy performs better than another.
- Experiment with different approaches to decision-making.
- Begin thinking like an AI developer.

---

# What You'll Modify

```text
agents/
└── student_agent.py
```

Unlike previous weeks, you'll spend the entire session improving a single file.

---

# Why Improve an AI?

Imagine teaching somebody to play Connect 4.

You probably wouldn't start by explaining advanced strategies.

Instead, you'd teach simple ideas first.

For example:

- If you can win, take the win.
- If your opponent is about to win, stop them.

Although these ideas seem obvious to humans, your AI must be taught how to recognise them.

By combining many small improvements, your AI can gradually become better at making decisions.

The important part is not simply adding more code.

It's learning how to identify a weakness, make a change, and test whether that change actually helped.

---

# Improvement 1 – Winning Comes First

Imagine a simplified row of the board looks like this:

```text
🟡 🟡 🟡 ⚪
```

Your AI can win immediately by playing in the empty space.

Should it choose another move?

Of course not.

Winning should be the highest priority whenever a winning move is available.

---

## TODO

Modify your AI so that before making its normal move, it checks whether there is a move that wins the game immediately.

Hints:

- Loop through every legal move.
- Create a copy of the board.
- Play the move on the copied board.
- Use the `Rules` class to check whether that move wins.
- If it does, return that move immediately.

You can use the `Rules` class you created in Week 3:

```python
from connect4.rules import Rules
```

Try implementing this yourself before continuing.

---

## Solution

There isn't a complete solution to copy for this task.

Instead, compare your implementation against the following checklist:

- Did you test every legal move?
- Did you use a copy of the board?
- Did you place the current player's piece on the copied board?
- Did you check whether that move creates a win?
- Did you immediately return the winning move?

If you answered "yes" to each question, your implementation is on the right track.

---

# Why Does This Help?

Previously, your AI could ignore a winning move because it had no way of recognising that the move would immediately end the game.

Now, your AI can identify an important situation and respond to it.

This demonstrates an important idea in AI development:

> A better decision-making process can come from teaching an AI to recognise important situations.

---

# Improvement 2 – Don't Ignore Your Opponent

Now imagine a simplified row looks like this:

```text
🔴 🔴 🔴 ⚪
```

If your opponent plays in the empty space next turn, they will win.

A stronger AI should recognise this danger and block it.

---

## TODO

Before making your normal move, check whether your opponent has an immediate winning move.

If they do, play in that column to block them.

Hints:

- Think about what your opponent could do on their next turn.
- Test each possible opponent move.
- Use a copy of the board when testing.
- Check whether the opponent would win after making that move.
- If you find an immediate winning move for the opponent, block that column.

Try implementing this yourself before continuing.

---

## Solution

There isn't a complete solution to copy for this task.

The logic is similar to the previous improvement, but there is an important difference:

**You are now testing the opponent's possible moves instead of your own.**

Think carefully about:

- Which player is currently making the move.
- Which player is the opponent.
- Which piece should be placed on the copied board.
- Which player you should check for a win.

Look for opportunities to reuse parts of your previous solution rather than writing completely new code.

---

# Testing Your Changes

After completing these improvements, run several games.

Ask yourself:

- Does your AI miss fewer winning opportunities?
- Does it defend itself better?
- Does it still make legal moves?
- Does the game still correctly detect wins and draws?
- Did the changes actually improve its performance?

Don't assume that a change made your AI better just because it sounds like a good idea.

Test it.

---

# Improvement 3 – Develop Your Own Strategy

Your AI can now:

- Take immediate winning moves.
- Block your opponent's immediate winning moves.

However, there are still many situations where multiple legal moves are available.

How should your AI decide between them?

Unlike the previous improvements, there isn't a single correct answer.

This is your opportunity to design your own strategy.

---

## Your Goal

Think about how you would play Connect 4.

What kinds of moves do you naturally prefer?

Could your AI do something similar?

Some ideas to explore include:

- Prefer moves near the centre of the board.
- Avoid creating opportunities for your opponent.
- Create multiple possible winning opportunities.
- Build longer chains of connected pieces.
- Consider how a move changes the board.
- Develop your own original strategy.

These are only suggestions.

You're encouraged to experiment and come up with your own ideas.

---

## TODO

Choose **at least one** improvement and add it to your AI.

Remember:

- Keep your code readable.
- Add comments where appropriate.
- Test your changes before moving on.
- Make sure your AI always returns a legal move.

There is no single correct solution.

Different strategies may perform better or worse depending on how they are implemented.

---

# Testing Your AI

Improving an AI isn't just about writing code.

You also need to test whether your ideas actually work.

After every improvement:

1. Run several games.
2. Watch how your AI behaves.
3. Look for repeated mistakes.
4. Record your results.
5. Decide whether your new strategy actually helped.

Sometimes an idea that sounds good doesn't improve the AI at all.

Testing allows you to measure the effect of every change you make.

---

# Comparing Different Versions

As you experiment, try keeping track of your results.

For example:

| Version | Games Played | Wins | Losses | Draws |
|---------|--------------|------|--------|-------|
| Original AI | 10 | — | — | — |
| Improvement 1 | 10 | — | — | — |
| Improvement 2 | 10 | — | — | — |
| Final Version | 10 | — | — | — |

The exact results will depend on your implementation.

The important part is learning how to compare different versions of your AI.

---

# Thinking Like an AI Developer

Professional AI development rarely involves writing the perfect solution on the first attempt.

Instead, developers repeat the same process many times.

```text
Observe
   │
   ▼
Identify a weakness
   │
   ▼
Improve one small part
   │
   ▼
Test the improvement
   │
   ▼
Repeat
```

This process is called **iteration**.

Rather than trying to solve everything at once, you improve the AI one step at a time.

This is an important skill you'll use throughout the rest of the project.

---

# Knowledge Check

Before moving on, make sure you can answer the following questions.

1. Why should a winning move have the highest priority?

2. Why is blocking your opponent important?

3. Why do we use a copy of the board when testing possible moves?

4. Why should you test your AI after every improvement?

5. Why isn't there a single "best" strategy for your AI?

6. What does it mean to iterate on an AI?

If you can answer these questions confidently, you've completed the main objectives of this week's lesson.

---

# Optional Challenge

Think about your AI's behaviour during testing.

Can you identify one situation where it still makes a poor decision?

Try designing a small improvement to solve that specific problem.

Don't worry if your first idea doesn't work perfectly.

AI development is all about experimenting, testing, and refining your ideas.

---

# Week 6 Summary

Congratulations! 🎉

This week you've taken your AI beyond simply making legal moves.

You taught it to:

- Recognise immediate winning opportunities.
- Block dangerous opponent moves.
- Apply your own strategic ideas.
- Test different approaches.
- Improve through iteration and experimentation.

More importantly, you've learned an important lesson about Artificial Intelligence:

> Strong AI systems are rarely built all at once.

Instead, they improve through many small changes, careful testing, and continuous refinement.

This approach is useful throughout software engineering and AI development, from simple games like Connect 4 to much larger systems.

---

# Looking Ahead

Next week, you'll submit your AI for the class tournament.

Your AI will compete against other student submissions, and you'll analyse the strengths and weaknesses of different approaches.

Remember, there isn't a single "correct" way to build your AI.

Every student will make different design decisions, and that's exactly what makes the final tournament interesting.

Before the tournament, make sure your AI:

- Always returns a legal move.
- Works correctly with the provided `GameState`.
- Does not modify the original game state.
- Can play a complete game without crashing.
- Has been tested against the `RandomAgent`.

See you in **Week 7!** 🏆
