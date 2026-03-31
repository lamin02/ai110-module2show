from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create owner
    owner = Owner("Alex")

    # Create pets
    dog = Pet("Buddy", "Dog")
    cat = Pet("Whiskers", "Cat")

    # Add pets to owner
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Create tasks
    task1 = Task("Morning Walk", duration=30, priority="high", time="14:00")
    task2 = Task("Feed Cat", duration=10, priority="medium", time="08:00")
    task3 = Task("Vet Appointment", duration=60, priority="high", time="12:00")
        
        # Assign tasks to pets
    dog.add_task(task1)
    cat.add_task(task2)
    dog.add_task(task3)

    # Create scheduler
    scheduler = Scheduler()

    # Load all tasks from owner
    scheduler.load_tasks_from_owner(owner)

    # Generate schedule
    schedule = scheduler.generate_daily_schedule()

    # Print schedule
    scheduler.load_tasks_from_owner(owner)

    print("\n=== Sorted by Time ===")
    for task in scheduler.sort_by_time():
        print(f"{task.time} - {task.title}")

    print("\n=== Incomplete Tasks ===")
    for task in scheduler.filter_tasks(completed=False):
        print(f"{task.title} (completed: {task.completed})")

    # Add conflicting task FIRST
    task4 = Task("Second Walk", duration=20, priority="low", time="08:00")
    dog.add_task(task4)

    # Reload tasks
    scheduler.load_tasks_from_owner(owner)

    # THEN check conflicts
    print("\n=== Conflicts ===")
    conflicts = scheduler.detect_conflicts()

    if conflicts:
        for c in conflicts:
            print(c)
    else:
        print("No conflicts.")
        
if __name__ == "__main__":
    main()

   

