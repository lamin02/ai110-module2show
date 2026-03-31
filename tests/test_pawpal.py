from pawpal_system import Task, Pet, Owner, Scheduler


def test_sort_by_time():
    scheduler = Scheduler()

    t1 = Task("A", 10, "low", time="14:00")
    t2 = Task("B", 10, "low", time="08:00")
    t3 = Task("C", 10, "low", time="12:00")

    scheduler.tasks = [t1, t2, t3]

    sorted_tasks = scheduler.sort_by_time()

    assert [t.time for t in sorted_tasks] == ["08:00", "12:00", "14:00"]


def test_filter_completed():
    scheduler = Scheduler()

    t1 = Task("A", 10, "low")
    t2 = Task("B", 10, "low")

    t1.completed = True

    scheduler.tasks = [t1, t2]

    filtered = scheduler.filter_tasks(completed=True)

    assert len(filtered) == 1
    assert filtered[0].title == "A"


def test_recurring_task():
    scheduler = Scheduler()

    t1 = Task("Daily Walk", 30, "high", recurring=True)

    scheduler.tasks = [t1]

    scheduler.complete_task(t1)

    # Should create a new task
    assert len(scheduler.tasks) == 2
    assert scheduler.tasks[1].title == "Daily Walk"


def test_conflict_detection():
    scheduler = Scheduler()

    t1 = Task("Task 1", 10, "low", time="08:00")
    t2 = Task("Task 2", 10, "low", time="08:00")

    scheduler.tasks = [t1, t2]

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "08:00" in conflicts[0]


def test_pet_with_no_tasks():
    pet = Pet("Buddy", "Dog")

    tasks = pet.get_tasks()

    assert tasks == []