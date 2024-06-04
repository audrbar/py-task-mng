from manager import Manager
from assignee import Assignee
from project import Project
from task import Task

is_executing = False

print('\n------------------1 step. The managers----------------------')
mng_1 = Manager('Julija', 'Roberts', 'julijaro@pyt.com')
mng_2 = Manager( 'John', 'Dep', 'johndep@dep.com')
print(mng_1.get_person_details())
print(mng_2.get_person_details())
print(mng_1.get_managers())
print('\n-----------------2 step. The assignees--------------------')
ass_1 = Assignee( 'Warren', 'Buffett', 'warbuf@buf.com')
ass_2 = Assignee( 'Bernard', 'Shaw', 'bernsho@ber.com')
print(ass_1.get_person_details())
print(ass_2.get_person_details())
print(ass_1.get_assignees())
print('\n-----------------3 step. The projects---------------------')
proj_1 = Project('001', 'Wind blowing farm', 'Create wind blow', 3000)
proj_2 = Project('002', 'Sun energies', 'Create sun shine', 5000)
print(proj_1.get_project_details())
print(proj_2.get_project_details())
print('\n-----------------4 step. The tasks-----------------------')
task_1 = Task('001', 'Purchase big fan', '2024-07-12', '2024-12-12')
task_2 = Task('002', 'Make big fire', '2024-07-12', '2024-12-12')
print(task_1.get_task_details())
print(task_2.get_task_details())
print('\n----------------5 step. The magic begins------------------')
task_1.add_assignee(ass_1)
print(task_1.get_task_details())
proj_1.add_manager(mng_1)
proj_1.add_manager(mng_2)
proj_1.add_task(task_1)
proj_1.add_task(task_2)
print(proj_1.get_project_details())
print(f"Projects: {proj_1.get_projects()}")
print(f"Tasks: {task_1.get_tasks()}")
