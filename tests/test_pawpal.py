from pawpal_system import Task, Pet


def test_task_completion():
    task = Task("Feed Dog", duration=10, priority="high")
    
    task.mark_complete()
    
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Buddy", "Dog")
    task = Task("Walk", duration=30, priority="medium")
    
    pet.add_task(task)
    
    assert len(pet.tasks) == 1