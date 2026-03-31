from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    """Represents a single care task assigned to a pet."""

    title: str
    duration: int
    priority: str
    time: Optional[str] = None
    recurring: bool = False
    completed: bool = False

    def is_high_priority(self) -> bool:
        """Return True if the task priority is 'high' (case insensitive)."""
        return self.priority.lower() == "high"

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True


@dataclass
class Pet:
    """Represents a pet belonging to an owner."""

    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet's task list if it exists."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks assigned to this pet."""
        return self.tasks


class Owner:
    """Represents a pet owner who manages one or more pets."""

    def __init__(self, name: str) -> None:
        """Initialize an owner with a name and an empty pet list."""
        self.name: str = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's pet list."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from this owner's pet list if it exists."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_pets(self) -> List[Pet]:
        """Return all pets belonging to this owner."""
        return self.pets

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all of this owner's pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    """Manages and schedules tasks for a daily pet care routine."""

    def __init__(self) -> None:
        """Initialize the scheduler with an empty task list."""
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the scheduler."""
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from the scheduler if it exists."""
        if task in self.tasks:
            self.tasks.remove(task)

    def generate_daily_schedule(self) -> List[Task]:
        """Return tasks sorted by priority, with high-priority tasks first."""
        return sorted(
            self.tasks,
            key=lambda task: task.priority.lower() != "high"
        )

    def get_tasks_by_priority(self) -> List[Task]:
        """Return all tasks ordered by priority."""
        return self.generate_daily_schedule()

    def load_tasks_from_owner(self, owner: Owner) -> None:
        """Load all tasks from an owner's pets into the scheduler."""
        self.tasks = owner.get_all_tasks()
