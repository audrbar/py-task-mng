"""Dummy Data to Feed Database Tables for Testing Purposes."""

projects_list_full = [
    {
        'project_name': 'Wind Factory Project',
        'project_aim': 'To create Wind Factory for energy self sufficiency',
        'project_budget': 500000,
        'manager': {
            'firstname': 'Bernard',
            'lastname': 'Shaw',
            'salary': 111000,
            'email': 'bernard.shaw@ber.com'
        },
        'tasks': [
            {
                'task_name': 'Organize Tech World',
                'start_date': '2024-01-01',
                'due_date': '2024-03-01',
                'status': 'in_progres',
                'assignees': [
                    {
                        'firstname': 'Alice',
                        'lastname': 'Brown',
                        'salary': 56000,
                        'email': 'alice.brown@example.com'
                    },
                ]
            },
            {
                'task_name': 'Make Fashion Fiesta',
                'start_date': '2024-01-01',
                'due_date': '2024-03-01',
                'status': 'not_started',
                'assignees': [
                    {
                        'firstname': 'Bob',
                        'lastname': 'Smith',
                        'salary': 63000,
                        'email': 'bob.smith@example.com'
                    },
                ]
            },
            {
                'task_name': 'Participate in the Fashion Fiesta',
                'start_date': '2024-03-01',
                'due_date': '2024-05-01',
                'status': 'not_started',
                'assignees': [
                    {
                        'firstname': 'Charlie',
                        'lastname': 'Davis',
                        'salary': 58000,
                        'email': 'charlie.davis@example.com'
                    },
                ]
            },
        ]
    },
    {
        'project_name': 'Sun Energy Project',
        'project_aim': 'To create Sun Energy Factory for energy self sufficiency',
        'project_budget': 600900,
        'manager': {
            'firstname': 'Warren',
            'lastname': 'Buffett',
            'salary': 121000,
            'email': 'warren.buffett@buf.com'
        },
        'tasks': [
            {
                'task_name': 'Create Grocery Hub',
                'start_date': '2024-01-01',
                'due_date': '2024-03-01',
                'status': 'in_progres',
                'assignees': [
                    {
                        'firstname': 'Alice',
                        'lastname': 'Brown',
                        'salary': 56000,
                        'email': 'alice.brown@example.com'
                    },
                    {
                        'firstname': 'Charlie',
                        'lastname': 'Davis',
                        'salary': 58000,
                        'email': 'charlie.davis@example.com'
                    },
                ]
            },
            {
                'task_name': 'Visit Grocery Hub',
                'start_date': '2024-03-01',
                'due_date': '2024-05-01',
                'status': 'not_started',
                'assignees': [
                    {
                        'firstname': 'Julia',
                        'lastname': 'Roberts',
                        'salary': 73000,
                        'email': 'julia.roberts@rob.com'
                    },
                ]
            },
            {
                'task_name': 'Raise Morning Sun',
                'start_date': '2024-01-01',
                'due_date': '2024-03-01',
                'status': 'not_started',
                'assignees': [
                    {
                        'firstname': 'Bob',
                        'lastname': 'Smith',
                        'salary': 63000,
                        'email': 'bob.smith@example.com'
                    },
                ]
            },
        ]
    },
    {
        'project_name': 'Moon Surface Project',
        'project_aim': 'To send Dream Team to the Moon for minerals',
        'project_budget': 450000,
        'manager': {
            'firstname': 'Johnny',
            'lastname': 'Depp',
            'salary': 81000,
            'email': 'johnny.dep@dep.com'
        },
        'tasks': [
            {
                'task_name': 'Make a Moon Rocket',
                'start_date': '2024-01-01',
                'due_date': '2024-03-01',
                'status': 'in_progres',
                'assignees': [
                    {
                        'firstname': 'Julia',
                        'lastname': 'Roberts',
                        'salary': 73000,
                        'email': 'julia.roberts@rob.com'
                    },
                ]
            },
            {
                'task_name': 'Start Journey to the Moon',
                'start_date': '2024-03-01',
                'due_date': '2024-05-01',
                'status': 'not_started',
                'assignees': [
                    {
                        'firstname': 'Alice',
                        'lastname': 'Brown',
                        'salary': 56000,
                        'email': 'alice.brown@example.com'
                    },                    {
                        'firstname': 'Bob',
                        'lastname': 'Smith',
                        'salary': 63000,
                        'email': 'bob.smith@example.com'
                    },
                ]
            },
            {
                'task_name': 'Bring Some Minerals',
                'start_date': '2024-05-01',
                'due_date': '2024-06-01',
                'status': 'not_started',
                'assignees': [
                    {
                        'firstname': 'Bob',
                        'lastname': 'Smith',
                        'salary': 63000,
                        'email': 'bob.smith@example.com'
                    },                    {
                        'firstname': 'Julia',
                        'lastname': 'Roberts',
                        'salary': 73000,
                        'email': 'julia.roberts@rob.com'
                    },
                ]
            }
        ]
    }
]

persons_list = [
    {
        'firstname': 'Alice',
        'lastname': 'Brown',
        'salary': 56000,
        'email': 'alice.brown@example.com'
    },
    {
        'firstname': 'Bob',
        'lastname': 'Smith',
        'salary': 63000,
        'email': 'bob.smith@example.com'
    },
    {
        'firstname': 'Charlie',
        'lastname': 'Davis',
        'salary': 58000,
        'email': 'charlie.davis@example.com'
    },
    {
        'firstname': 'Julia',
        'lastname': 'Roberts',
        'salary': 73000,
        'email': 'julia.roberts@rob.com'
    },
    {
        'firstname': 'Johnny',
        'lastname': 'Depp',
        'salary': 81000,
        'email': 'johnny.dep@dep.com'
    },
    {
        'firstname': 'Warren',
        'lastname': 'Buffett',
        'salary': 121000,
        'email': 'warren.buffett@buf.com'
    },
    {
        'firstname': 'Bernard',
        'lastname': 'Shaw',
        'salary': 111000,
        'email': 'bernard.shaw@ber.com'
    }
]

projects_list = [
    {
        'project_name': 'Wind Factory Project',
        'project_aim': 'To create Wind Factory for energy self sufficiency',
        'project_budget': 500000
    },
    {
        'project_name': 'Sun Energy Project',
        'project_aim': 'To create Sun Energy Factory for energy self sufficiency',
        'project_budget': 600900
    },
    {
        'project_name': 'Moon Surface Project',
        'project_aim': 'To send Dream Team to the Moon for minerals',
        'project_budget': 450000
    }
]

tasks_list = [
    {
        'task_name': 'Organize Tech World',
        'start_date': '2024-01-01',
        'due_date': '2024-03-01',
        'status': 'in_progres'
    },
    {
        'task_name': 'Make Fashion Fiesta',
        'start_date': '2024-01-01',
        'due_date': '2024-03-01',
        'status': 'not_started'
    },
    {
        'task_name': 'Participate in the Fashion Fiesta',
        'start_date': '2024-03-01',
        'due_date': '2024-05-01',
        'status': 'not_started'
    },
    {
        'task_name': 'Create Grocery Hub',
        'start_date': '2024-01-01',
        'due_date': '2024-03-01',
        'status': 'in_progres'
    },
    {
        'task_name': 'Visit Grocery Hub',
        'start_date': '2024-03-01',
        'due_date': '2024-05-01',
        'status': 'not_started'
    },
    {
        'task_name': 'Raise Morning Sun',
        'start_date': '2024-01-01',
        'due_date': '2024-03-01',
        'status': 'not_started'
    },
    {
        'task_name': 'Make Rocket for the Journey to the Moon',
        'start_date': '2024-01-01',
        'due_date': '2024-03-01',
        'status': 'in_progres'
    },
    {
        'task_name': 'Start Journey to the Moon',
        'start_date': '2024-03-01',
        'due_date': '2024-05-01',
        'status': 'not_started'
    },
    {
        'task_name': 'Bring Some Minerals',
        'start_date': '2024-05-01',
        'due_date': '2024-06-01',
        'status': 'not_started'
    }
]

person_tasks_list = [
    {'person_id': 1, 'task_id': 1},
    {'person_id': 2, 'task_id': 2},
    {'person_id': 3, 'task_id': 3},
    {'person_id': 1, 'task_id': 4},
    {'person_id': 4, 'task_id': 5},
    {'person_id': 1, 'task_id': 6},
    {'person_id': 4, 'task_id': 6},
    {'person_id': 5, 'task_id': 7},
    {'person_id': 5, 'task_id': 8},
    {'person_id': 2, 'task_id': 9}
]
