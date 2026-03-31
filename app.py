import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Default Owner")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.tasks.append(
        {"title": task_title, "duration_minutes": int(duration), "priority": priority}
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.header("Add a Pet")

# ✅ FIX: added missing input for species
pet_species = st.text_input("Pet species")

if st.button("Add Pet"):
    if pet_name and pet_species:
        new_pet = Pet(pet_name, pet_species)
        st.session_state.owner.add_pet(new_pet)
        st.success(f"{pet_name} added!")
    else:
        st.warning("Please enter both name and species.")

# ✅ Show pets
st.header("Your Pets")

pets = st.session_state.owner.get_pets()

for pet in pets:
    st.write(f"- {pet.name} ({pet.species})")


# ✅ Add Task (CONNECTED to your backend)
st.header("Add Task to a Pet")

if pets:
    pet_names = [pet.name for pet in pets]
    selected_pet_name = st.selectbox("Select a pet", pet_names)

    task_title_input = st.text_input("Task title")
    task_duration_input = st.number_input("Duration (minutes)", min_value=1, value=10)
    task_priority_input = st.selectbox("Priority", ["low", "medium", "high"])

    if st.button("Add Task to Pet"):
        if task_title_input:
            selected_pet = next(p for p in pets if p.name == selected_pet_name)

            new_task = Task(
                title=task_title_input,
                duration=task_duration_input,
                priority=task_priority_input
            )

            selected_pet.add_task(new_task)
            st.success(f"Task '{task_title_input}' added to {selected_pet.name}!")
        else:
            st.warning("Enter a task title.")
else:
    st.info("Add a pet first.")


# ✅ Display tasks
st.header("Tasks by Pet")

for pet in pets:
    st.subheader(f"{pet.name}'s Tasks")

    tasks = pet.get_tasks()

    if tasks:
        for task in tasks:
            st.write(f"- {task.title} ({task.priority}, {task.duration} min)")
    else:
        st.write("No tasks yet.")


st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    st.warning(
        "Not implemented yet. Next step: create your scheduling logic (classes/functions) and call it here."
    )
    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )