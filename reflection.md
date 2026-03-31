# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
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
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
