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
    task1 = Task("Morning Walk", duration=30, priority="high", time="08:00")
    task2 = Task("Feed Cat", duration=10, priority="medium", time="09:00")
    task3 = Task("Vet Appointment", duration=60, priority="high", time="14:00")

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
    print("\n=== Today's Schedule ===")
    for task in schedule:
        print(f"- {task.time} | {task.title} ({task.priority})")


if __name__ == "__main__":
    main()