# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
My initial UML design focused on modeling the main parts of a pet care system using simple classes that represent real-world objects like pets and tasks.

- What classes did you include, and what responsibilities did you assign to each?
3 core actions identified: 
1) add and manage pet info 
2) create and manage care tasks 
3) generate and view daily care schedule 

Classes: 

Pet 
- represents an animal and keeps track of tasks related to that pet 
Attributes: name, species, list of tasks 
Methods: add_task(), get_tasks()

Task  
The Task represents a care activity such as feeding, walking, or medication.  
Attributes: title, duration, priority, time (optional), recurring (optional)  
Methods: is_due_today(), conflicts_with()

Scheduler  
The Scheduler is responsible for organizing tasks into a daily plan. It applies logic like sorting and conflict detection.  
Attributes: list of tasks  
Methods: sort_tasks(), detect_conflicts(), generate_schedule()

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

No, my design did not change during implementation. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
My scheduler considers task time and priority when organizing tasks.

- How did you decide which constraints mattered most?
I chose time and priority because they are the most important factors for organizing daily tasks in a realistic way for a pet owner.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

- Conflict detection only checks exact matching times.
- Does not handle overlapping task durations.
- Simpler and more readable, but less accurate for real-world scheduling.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI to help brainstorm my class design, generate method implementations, and debug errors when my code did not work.

- What kinds of prompts or questions were most helpful?
Specific prompts like asking how to fix an error, how to implement a method, or how to structure a class were the most helpful.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
There were times when AI gave code that was too complicated or added extra features I did not need.

- How did you evaluate or verify what the AI suggested?
I checked if the code matched the assignment requirements and tested it by running my program to make sure it worked correctly.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested sorting tasks by time, filtering tasks by completion, recurring task behavior, and conflict detection.

- Why were these tests important?
These tests were important to make sure the scheduler worked correctly and handled both normal and edge cases.

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am fairly confident that my scheduler works correctly for basic scenarios.

- What edge cases would you test next if you had more time?
I would test overlapping task durations, multiple conflicts, and different time formats.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am most satisfied with building the scheduler logic and connecting it to the Streamlit UI.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would improve the scheduler by handling overlapping tasks and making the scheduling logic more advanced.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
I learned that AI is a helpful tool, but I still need to understand the code and make decisions to keep the system clean and correct.
