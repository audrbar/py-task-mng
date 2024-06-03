from manager import Manager
from assignee import Assignee
from project import Project
from task import Task

is_executing = False

mng_1 = Manager('001', 'Julija', 'Roberts', 'julijaro@pyt.com')
mng_2 = Manager('002', 'John', 'Dep', 'johndep@dep.com')
ass_1 = Assignee('001', 'Warren', 'Buffett', 'warbuf@buf.com')
ass_2 = Assignee('002', 'Bernard', 'Shaw', 'bernsho@ber.com')
print(mng_1.get_manager_details())
print(mng_2.get_manager_details())
print(ass_1.get_assignee_details())
print(ass_2.get_assignee_details())

proj_1 = Project('001', 'Wind blowing farm', 'Create wind blow', 3000)
proj_2 = Project('002', 'Sun energies', 'Create sun shine', 5000)
print(proj_1.get_project_details())
print(proj_2.get_project_details())

task_1 = Task('001', 'Purchase big fan', '2024-07-12', '2024-12-12')
task_2 = Task('002', 'Make big fire', '2024-07-12', '2024-12-12')
print(task_1.get_task_details())
print(task_2.get_task_details())

proj_1.add_manager(mng_1)
proj_1.add_task(task_1)
print(proj_1.get_project_details())


while is_executing:
    print("Project Management Program")
    print("2. Hire a Managers")
    print("3. Hire an Employs")
    print("4. Define a projects")
    print("5. Assign an assignees")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    else:
        print("Your have to choose between 1 to 4.")
        is_executing = False

