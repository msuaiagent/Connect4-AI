# Week 7: Testing, Benchmarking & Tournament

Over the past six weeks, you've built a complete Connect 4 AI from the ground up.

You've learned how to:

- Build a game board.
- Create a game engine.
- Display the game using Pygame.
- Design your own AI.
- Improve it through testing and experimentation.

Now it's time to put your work to the test.

This week, you'll prepare your AI for the tournament, learn why benchmarking is important, and reflect on the decisions you made throughout the project.

---

# Learning Objectives

By the end of this week, you should be able to:

- Test your AI before submission.
- Explain why benchmarking is important.
- Understand how the class tournament works.
- Prepare your AI for evaluation.
- Identify the strengths and weaknesses of your AI.
- Reflect on how your AI developed throughout the project.

---

# What You'll Submit

This week, you'll submit just one file:

```text
agents/
└── student_agent.py
```

The instructor will place your AI into the tournament environment.

Your `student_agent.py` must work with the provided project as submitted.

Do not modify other project files unless your instructor specifically allows you to.

---

# Why Test an AI?

Imagine spending weeks improving your AI, only to discover during the tournament that it crashes after a few moves.

Testing helps prevent problems like this.

Before submitting your work, you should always make sure that:

- Your AI runs without errors.
- Your AI always returns a legal move.
- Your AI behaves as expected.
- Your AI can play a complete game.
- Your latest changes didn't accidentally make it worse.

Testing is just as important as writing the AI itself.

---

# Task 1 – Play Test Your AI

Run your project several times.

```bash
python run.py
```

Watch complete games rather than stopping after the first few moves.

As you watch, ask yourself:

- Does my AI always make legal moves?
- Does it recognise winning opportunities?
- Does it block dangerous situations?
- Does it still make repeated mistakes?
- Does it ever behave unexpectedly?

If you notice problems, try improving your AI before submitting it.

---

# Final Technical Check

Before submitting your AI, make sure that:

- `StudentAgent` inherits from `BaseAgent`.
- `choose_move()` accepts the provided `GameState` and uses it to decide which legal move to play.
- `choose_move()` always returns a legal move.
- Your AI does not modify the game engine.
- Your AI does not depend on files that will not be included in the tournament.
- Your AI can play an entire game without crashing.

If something doesn't work, fix it before submitting.

---

# What is Benchmarking?

Imagine two students both say:

> "My AI is really good."

How could we find out?

Instead of guessing, we compare results.

This process is called **benchmarking**.

Benchmarking means evaluating how well your AI performs under consistent conditions.

Using the same rules and evaluation process allows different AI agents to be compared fairly.

Benchmarking isn't only about finding a winner.

It also helps us understand how well different approaches perform.

---

# Task 2 – Preparing Your Submission

Before submitting your AI, make sure:

- Your code is complete.
- Your AI never crashes.
- Your AI always returns a legal move.
- Your code is easy to read.
- You've tested it several times.
- Your final changes are saved in `student_agent.py`.

The only file you need to submit is:

```text
agents/
└── student_agent.py
```

I will handle the tournament environment, so you can send me the file through discord.

---

# How the Tournament Works

After everyone has submitted their AI, the instructor will run the tournament using the provided tournament environment.

The general process will be:

- Each student's AI will compete against the other submitted AIs.
- Each matchup will be played over multiple games.
- Players will alternate who goes first.
- The results from the matches will be combined into a final leaderboard.

Playing multiple games helps reduce the effect of luck and first-move advantage.

Every student competes under the same conditions.

---

# Tournament Scoring

Each match contributes points toward the final leaderboard.

The scoring system is:

| Result | Points |
|--------|--------:|
| Win | 3 |
| Draw | 1 |
| Loss | 0 |

At the end of the tournament, every student's points are added together.

The AI with the highest total score finishes at the top of the leaderboard.

Remember that the goal isn't simply to win one game.

A strong AI should perform consistently well across many different matches.

---

# Why Play Multiple Games?

A single game doesn't always tell us how strong an AI really is.

For example, an AI might win one game because of:

- Going first.
- A particular board position.
- An unusual mistake by its opponent.
- Randomness in decision-making.

By playing multiple games and alternating who moves first, we get a better picture of how the AI performs overall.

This is one reason consistent testing is important in AI development.

---

# Analysing Your AI

After the tournament, take some time to reflect on your AI's performance.

Consider questions such as:

- What situations did your AI handle well?
- What types of positions caused it problems?
- Did it miss any obvious winning moves?
- Did it successfully defend against strong attacks?
- Did your strategy work as expected?
- If you had another week, what would you improve?

There isn't a perfect AI.

Every improvement you make teaches you something new.

---

# What You've Learned

Over the past seven weeks, you've developed much more than a Connect 4 AI.

You've also practised important software engineering skills, including:

- Breaking large problems into smaller tasks.
- Designing reusable classes.
- Separating responsibilities between different parts of a program.
- Testing and debugging code.
- Improving software through iteration.
- Evaluating the performance of your own work.
- Working with an existing codebase.

These are valuable skills that apply to many areas of programming—not just Artificial Intelligence.

---

# Knowledge Check

Before finishing the project, make sure you can answer the following questions.

1. Why is testing important before submitting your AI?

2. Why should tournament matches be played multiple times instead of just once?

3. Why do players alternate who moves first?

4. Why is benchmarking useful when comparing different AI agents?

5. Why is it important for every AI to be evaluated under the same conditions?

6. What was the most effective improvement you made to your AI?

7. What is one weakness your AI still has?

If you can answer these questions confidently, you've completed the learning objectives for this project.

---

# Course Summary

Congratulations! 🎉

Over the past seven weeks, you've built a complete Connect 4 AI project from the ground up.

You have:

- Set up a professional Python development environment.
- Learned the basics of Git and GitHub.
- Built the Connect 4 board.
- Created a complete game engine.
- Added a graphical interface using Pygame.
- Designed your own AI agent.
- Improved your AI through testing and experimentation.
- Prepared your AI for tournament play.

Along the way, you've also developed valuable programming skills, including:

- Object-oriented programming
- Software design
- Debugging
- Testing
- Problem solving
- Iterative development

Most importantly, you've learned that building AI isn't about finding a single "perfect" solution.

It's about observing, experimenting, improving, and testing your ideas.

That mindset is used throughout software engineering and Artificial Intelligence.

---

# Thank You

Thank you for taking part in this **MSU AI Club Guided AI Project**.

Whether your AI finishes first or last in the tournament, you've successfully designed, built, tested, and improved your own intelligent game-playing agent.

That's an achievement you should be proud of.

Good luck, and happy coding! 🚀
