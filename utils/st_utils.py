"""Functions that renders Streamlit Page's elements."""
from typing import List

import streamlit as st
from datetime import datetime
from src.base import db_engine, session
from src.models import Assignee, Project, Task, Manager, AssigneeTask
from utils.utilities import (find_project_id, make_assignees_list, make_managers_list, load_lottie_url,
                             assignees_to_chart, make_projects_list, make_tasks_list, find_task_id,
                             find_manager_id, find_assignee_id)


def page_config() -> None:
    """Configures the Streamlit page settings.

    This function sets the configuration for the entire Streamlit page, including the page title, icon, layout,
    and initial sidebar state. It uses Streamlit's `st.set_page_config` method to apply these settings globally
    to the app.

    The following configurations are applied:
    - `page_title`: Sets the title of the web page to "Project Management App".
    - `page_icon`: Sets the page icon to a globe emoji (🌐).
    - `layout`: Defines the layout as wide, allowing the app to take up the full width of the browser window.
    - `initial_sidebar_state`: Sets the initial state of the sidebar to "auto", which allows it to be expanded
       or collapsed automatically.
    - `menu_items`: No custom menu items are specified (defaults to `None`).

    :return: None
    """
    st.set_page_config(
        page_title="Project Management App",
        page_icon=":globe_with_meridians:",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items=None
    )


def hide_st_style() -> None:
    """Hides Streamlit's default interface elements from the page view.

    This function uses Streamlit's `st.markdown` method to inject custom CSS into the page. It hides the main menu,
    footer, and header typically provided by Streamlit's default interface, making the page cleaner and less cluttered
    for visitors.

    The following elements are hidden:
    - `#MainMenu`: The hamburger menu that typically appears in the top-right corner.
    - `footer`: The footer that usually contains "Made with Streamlit".
    - `header`: The header that might contain additional controls or branding.

    :return: None
    """
    st.markdown("""
            <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
            </style>
            """,
                unsafe_allow_html=True)


def hero_section() -> None:
    """Renders the hero section of the Streamlit page.

    This function creates a visually engaging hero section at the top of the Streamlit page using a combination of
    text and animation. It uses Streamlit's container, columns, title, and write methods to display key information
    about the Team Workflow Manager application, including its technological stack and hosting details.
    The hero section is split into two columns:
    - The left column contains descriptive text about the application, highlighting its use of Python, hosting on
      Streamlit Community Cloud, and data storage on a PostgreSQL database managed by Supabase.
    - The right column loads and displays a Lottie animation via the `load_lottie_url` function, adding a dynamic
      visual element to the page.

    The section is separated from the rest of the content by a horizontal line rendered using the `st.write("---")`
    method.

    :return: None
    """
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2, gap="small")
        with left_column:
            st.subheader("Main Features")
            st.write("Built with _Python_, *Team Workflow Manager* may be hosted on *Streamlit Community Cloud*, "
                     "offering seamless access and real-time updates. All project data, including task details, budget "
                     "allocations, and team information, may be securely stored in a *PostgreSQL* database hosted on "
                     "*Supabase*, ensuring reliability and scalability for your project management needs.")
        with right_column:
            load_lottie_url("https://lottie.host/5b073eca-e11c-4391-8593-b28f39ce0870/q0fz2A3kuN.json")


def chart_section(all_assignees_: List[Assignee]) -> None:
    """Displays a bar chart of tasks per assignee in the Streamlit application.

    This function creates a section in the Streamlit app that visualizes the distribution
    of tasks assigned to each assignee. It receives all assignees, processes the data to calculate
    the number of tasks per assignee, and displays this information in a bar chart.

    assignees_from_query : list[Assignee]
        A list of assignee objects or names obtained from a database query. This list populates the dropdown
        menu where the user selects the assignee to be assigned to the selected task.

    Returns: None: This function does not return any value; it directly modifies the Streamlit UI.
    """
    st.divider()
    st.write("Tasks per assignee:")
    df = assignees_to_chart(all_assignees_)
    df['full_name'] = df['firstname'] + ' ' + df['lastname']
    df.set_index('full_name', inplace=True)
    tasks_per_assignee = df['tasks']
    st.bar_chart(tasks_per_assignee)


def footer_section() -> None:
    """Renders the footer section of the Streamlit page.

    This function creates a footer at the bottom of the Streamlit page, providing a clear separation from the rest
    of the content with a horizontal line. The footer includes a copyright notice with the current year and the
    name "audrbar".

    The footer section includes:
    - A horizontal line rendered using `st.write("---")` to visually separate the footer from the main content.
    - A dynamically generated copyright notice that uses the current year (retrieved from `datetime.now().year`).

    :return: None
    """
    with st.container():
        st.write("---")
        st.write(f"© {datetime.now().year} audrbar. All rights reserved.")


def header_section(section_title: str, section_description: str) -> None:
    """Renders the header section of the Streamlit page.

    This function uses Streamlit's container, title, and write methods to display the main title and a brief
    description of the Team Workflow Manager application. The header provides users with an overview of
    the application's purpose and functionality.

    :return: None
    """
    with st.container():
        st.header(section_title)
        st.write(section_description)


def edit_project_budget(projects_from_query: list[Project]) -> None:
    """Creates a form in the Streamlit application to edit the budget of a selected project.

    This function generates a form within a Streamlit app that allows users to update the budget of an existing project.
    Users can select a project from a dropdown menu, provide a new budget amount, and submit the form to save the
    changes. Once submitted, the project's budget is updated in the database.

    Parameters:
    projects_from_query : list[Project]
        A list of project objects or names obtained from a database query. This list populates the dropdown
        menu where the user selects the project they want to update.

    Returns: None : This function does not return any value. It directly modifies the Streamlit UI and updates the
    project's budget in the database upon form submission.
    """
    with st.form('project_budget', clear_on_submit=True):
        st.write("Edit Project Budget:")
        selected_project = st.selectbox('Select a Project task is for:', make_projects_list(projects_from_query),
                                        index=None, placeholder="Select a project...", label_visibility="collapsed")
        provided_budget = st.number_input('Provide budget value, $')
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            session.query(Project).filter(Project.project_name == selected_project).update(
                {Project.project_budget: provided_budget}, synchronize_session=False)
            session.commit()
            db_engine.close_session()
            st.write(f"The project _'{selected_project}'_ budget was set to {provided_budget}$.")
        else:
            st.write('To succeed please select and fill inputs and smash a Submit button.')


def assign_task_assignee(tasks_from_query: list[Task], assignees_from_query: list[Assignee]) -> None:
    """Creates a form in the Streamlit application to assign an assignee to a selected task.

    This function generates a form within a Streamlit app that allows users to assign an existing task to an assignee.
    Users can select a task from a dropdown menu, choose an assignee, and submit the form to update the task assignment.
    Upon submission, the selected task is assigned to the selected assignee, and the relationship is saved in the
    database.

    Parameters:
    tasks_from_query : list[Task]
        A list of task objects or names obtained from a database query. This list populates the dropdown
        menu where the user selects the task to be assigned to an assignee.
    assignees_from_query : list[Assignee]
        A list of assignee objects or names obtained from a database query. This list populates the dropdown
        menu where the user selects the assignee to be assigned to the selected task.

    Returns: None : This function does not return any value. It directly modifies the Streamlit UI and updates the task
        assignment in the database upon form submission.
    """
    with st.form('assign_assignee', clear_on_submit=True):
        st.write('Assign Task Assignee:')
        selected_task = st.selectbox('Select a task to edit:', make_tasks_list(tasks_from_query),
                                     index=None, placeholder="Select a task...")
        selected_assignee = st.selectbox('Select a Assignee to assign:', make_assignees_list(assignees_from_query),
                                         index=None, placeholder="Select a Assignee...")
        selected_assignee_id = find_assignee_id(assignees_from_query, selected_assignee)
        selected_task_id = find_task_id(tasks_from_query, selected_task)
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            assignee_task_to_add = AssigneeTask(task_id=selected_task_id, assignee_id=selected_assignee_id)
            session.add(assignee_task_to_add)
            session.commit()
            db_engine.close_session()
            st.write(f"The task _'{selected_task}'_ was assigned to _'{selected_assignee}'_.")
        else:
            st.write('To succeed please select and fill inputs and smash a Submit button.')


def change_task_status(tasks_from_query: list[Task]) -> None:
    """Creates a form in the Streamlit application to change the status of a selected task.

    This function generates a form within a Streamlit app that allows users to update the status of an existing task.
    Users can select a task from a dropdown menu, choose a new status from predefined options, and submit the form
    to apply the changes. Upon submission, the selected task's status is updated in the database.

    Parameters:
    tasks_from_query : list[Task]
        A list of task objects or names obtained from a database query. This list populates the dropdown
        menu where the user selects the task whose status they want to change.

    Returns: None : This function does not return any value. It directly modifies the Streamlit UI and updates
    the task's status in the database upon form submission.
    """
    with st.form('change_status', clear_on_submit=True):
        st.write('Change Task status:')
        selected_task = st.selectbox('Select a task to edit:', make_tasks_list(tasks_from_query),
                                     index=None, placeholder="Select task...")
        selected_status = st.selectbox('Select a Task status to set', ['not_started', 'in_progres', 'done'],
                                       index=None, placeholder="Select status...")
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            session.query(Task).filter(Task.task_name == selected_task).update(
                {Task.status: selected_status}, synchronize_session=False)
            session.commit()
            db_engine.close_session()
            st.write(f"The task _'{selected_task}'_ status was changed to _'{selected_status}'_.")
        else:
            st.write('To succeed please select input and smash a Submit button.')


def set_salary(assignees_from_query: list[Assignee]) -> None:
    """Creates a form in the Streamlit application to set or update the salary of a selected assignee.

    This function generates a form within a Streamlit app that allows users to set or update the salary of an existing
    assignee. Users can select an assignee from a dropdown menu, input a new salary value, and submit the form to apply
    the changes. Upon submission, the selected assignee's salary is updated in the database.

    Parameters:
    assignees_from_query : list[Any]
        A list of assignee objects or names obtained from a database query. This list populates the dropdown
        menu where the user selects the assignee whose salary they want to set or update.

    Returns: None : This function does not return any value. It directly modifies the Streamlit UI and updates
    the assignee's salary in the database upon form submission.
    """
    with st.form('set_salary', clear_on_submit=True):
        st.write('Set Assignee salary:')
        selected_assignee = st.selectbox('Select a Assignee to assign:', make_assignees_list(assignees_from_query),
                                         index=None, placeholder="Select a assignee...")
        provided_salary = st.number_input('Provide salary value, $')
        selected_assignee_id = find_assignee_id(assignees_from_query, selected_assignee)
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            session.query(Assignee).filter(Assignee.id == selected_assignee_id).update(
                {Assignee.salary: provided_salary}, synchronize_session=False)
            session.commit()
            db_engine.close_session()
            st.write(f"The _{selected_assignee}\'s_ salary was set to _{provided_salary}$_.")
        else:
            st.write('To succeed please select and fill inputs and smash a Submit button.')


def add_new_project() -> None:
    """Creates a form in the Streamlit application to add a new project along with its manager.

    This function generates a form within a Streamlit app that allows users to input details for creating a new project.
    Users can provide the project's name, aim, budget, and details about the manager (first name, last name, email,
    and salary). Upon submission, the function adds the new manager and project to the database.

    Returns: None : This function does not return any value. It directly modifies the Streamlit UI and updates
    the database by adding the new project and assigning the specified manager to it.
    """
    with st.form('add project', clear_on_submit=True):
        st.write("Add New Project:")
        project_name = st.text_input('Provide project name:')
        project_aim = st.text_area('Describe project aim:')
        project_budget = st.number_input('Provide budget value, $:', min_value=0.0,
                                         max_value=1000000.0,
                                         step=1.0, value=0.0)
        provided_firstname = st.text_input('Provide manager first name:')
        provided_lastname = st.text_input('Provide manager last name:')
        provided_email = st.text_input('Provide manager email:')
        provided_salary = st.number_input('Provide manager salary value, $:', min_value=40000.0,
                                          max_value=100000.0, step=10.0, value=50000.0)
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            manager_to_add = Manager(firstname=provided_firstname, lastname=provided_lastname,
                                     salary=provided_salary, email=provided_email)
            session.add(manager_to_add)
            session.commit()
            project_to_add = Project(project_name=project_name, project_aim=project_aim,
                                     project_budget=project_budget, manager=manager_to_add)
            session.add(project_to_add)
            session.commit()
            db_engine.close_session()
            st.write(f"The project _'{project_name}'_ was created and manager "
                     f"was _'{provided_firstname} {provided_lastname}'_ assigned to.")
        else:
            st.write('To succeed please fill and select inputs and smash a Submit button.')


def add_new_task(assignees_from_query: list[Assignee], projects_from_query: list[Project]) -> None:
    """Creates a form in the Streamlit application to add a new task and assign it to a project and assignee.

    This function generates a form within a Streamlit app that allows users to input details for creating a new task.
    Users can provide the task name, start date, due date, and select an assignee and a project from dropdown menus.
    Upon submission, the function adds the new task to the database, associates it with the selected project, and
    assigns it to the selected assignee.

    Parameters:
    assignees_from_query : list[Assignee]
        A list of assignee objects or names obtained from a database query. This list populates the dropdown menu where
        the user selects the assignee to whom the task will be assigned.
    projects_from_query : list[Project]
        A list of project objects or names obtained from a database query. This list populates the dropdown menu where
        the user selects the project to which the task will be associated.

    Returns: None : This function does not return any value. It directly modifies the Streamlit UI and updates
    the database by adding the new task, associating it with the selected project, and assigning it to the selected
    assignee.
    """
    with st.form('add task', clear_on_submit=True):
        st.write("Add New Task:")
        provided_task = st.text_input('Provide task name:')
        provided_start_date = st.date_input('Provide start date:', value=None, format="YYYY/MM/DD")
        provided_due_date = st.date_input('Provide due date:', value=None, format="YYYY/MM/DD")
        selected_project = st.selectbox('Select a Project task is for:', make_projects_list(projects_from_query),
                                        index=None, placeholder="Select a project...")
        selected_project_id = find_project_id(projects_from_query, selected_project)
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            task_to_add = Task(task_name=provided_task, start_date=provided_start_date,
                               due_date=provided_due_date, status="not_started",
                               project_id=selected_project_id)

            session.add(task_to_add)
            session.commit()
            db_engine.close_session()
            st.write(f"The task _'{provided_task}'_ to the project {selected_project} was created.")
        else:
            st.write('To succeed please select and fill inputs and smash a Submit button.')


def add_new_assignee() -> None:
    """Creates a form in the Streamlit application to add a new assignee to the system.

    This function generates a form within a Streamlit app that allows users to input details for creating a new
    assignee. Users can provide the assignee's first name, last name, email, and salary. Upon submission,
    the function adds the new assignee to the database.

    Returns: None : This function does not return any value. It directly modifies the Streamlit UI and updates
    the database by adding the new assignee to the system upon form submission.
    """
    with st.form('add assignee', clear_on_submit=True):
        st.write("Add New Assignee:")
        provided_firstname = st.text_input('Provide first name:')
        provided_lastname = st.text_input('Provide last name:')
        provided_email = st.text_input('Provide email:')
        provided_salary = st.number_input('Provide salary value, $:', min_value=40000.0,
                                          max_value=100000.0, step=10.0, value=50000.0)
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            assignee_to_add = Assignee(firstname=provided_firstname, lastname=provided_lastname,
                                       salary=provided_salary, email=provided_email)
            session.add(assignee_to_add)
            session.commit()
            db_engine.close_session()
            st.write(f"The assignee _'{provided_firstname} {provided_lastname}'_ was added.")
        else:
            st.write('To succeed please fill inputs and smash a Submit button.')


def delete_project(projects_from_query: list[Project]) -> None:
    """Creates a form in the Streamlit application to delete an existing project from the system.

    This function generates a form within a Streamlit app that allows users to delete an existing project.
    Users can select a project from a dropdown menu and submit the form to remove the project from the database.
    The function handles the deletion process, including error handling in case the project cannot be found or if
    an issue occurs during deletion.

    Parameters:
    projects_from_query : list[Project]
        A list of project objects or names obtained from a database query. This list populates the dropdown
        menu where the user selects the project they want to delete.

    Returns: None : This function does not return any value. It directly modifies the Streamlit UI and updates
    the database by deleting the selected project upon form submission.
    """
    with st.form('delete_project', clear_on_submit=True):
        st.write("Delete Project:")
        selected_project = st.selectbox('Select a Project to delete', make_projects_list(projects_from_query),
                                        index=None, placeholder="Select a project...")
        selected_project_id = find_project_id(projects_from_query, selected_project)
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            project_to_delete = session.query(Project).filter(Project.id == selected_project_id).first()
            if project_to_delete:
                try:
                    # Delete the project from the session and commit the transaction
                    session.query(Project).filter(Project.id == selected_project_id).delete(synchronize_session='fetch')
                    session.commit()
                    st.write(f"The project _'{selected_project}'_ was successfully deleted.")
                except Exception as e:
                    session.rollback()
                    st.write(f"An error occurred: {e}")
                finally:
                    db_engine.close_session()
            else:
                st.write(f"The project _'{selected_project}'_ could not be found.")
        else:
            st.write('To succeed please select input and smash a Submit button.')


def delete_manager(managers_from_query: list[Manager]) -> None:
    """Creates a form in the Streamlit application to delete an existing manager from the system.

    This function generates a form within a Streamlit app that allows users to delete an existing manager.
    Users can select a manager from a dropdown menu and submit the form to remove the manager from the database.
    The function handles the deletion process, including error handling in case the manager cannot be found or if
    an issue occurs during deletion.

    Parameters:
    managers_from_query : list[Manager]
        A list of manager objects or names obtained from a database query. This list populates the dropdown
        menu where the user selects the manager they want to delete.

    Returns: None : This function does not return any value. It directly modifies the Streamlit UI and updates
    the database by deleting the selected manager upon form submission.
    """
    with st.form('delete_manager', clear_on_submit=True):
        st.write("Delete manager:")
        selected_manager = st.selectbox('Select a Manager to delete', make_managers_list(managers_from_query),
                                        index=None, placeholder="Select a manager...")
        selected_manager_id = find_manager_id(managers_from_query, selected_manager)
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            manager_to_delete = session.query(Manager).filter(Manager.id == selected_manager_id).first()
            if manager_to_delete:
                try:
                    session.query(Manager).filter(Manager.id == selected_manager_id).delete(synchronize_session='fetch')
                    session.commit()
                    st.write(f"The manager _'{selected_manager}'_ was successfully deleted.")
                except Exception as e:
                    session.rollback()
                    st.write(f"An error occurred: {e}")
                finally:
                    db_engine.close_session()
            else:
                st.write(f"The manager _'{selected_manager}'_ could not be found.")
        else:
            st.write('To succeed please select input and smash a Submit button.')


def delete_task(tasks_from_query: list[Task]) -> None:
    """Creates a form in the Streamlit application to delete an existing task from the system.

    This function generates a form within a Streamlit app that allows users to delete an existing task.
    Users can select a task from a dropdown menu and submit the form to remove the task from the database.
    The function handles the deletion process, including error handling in case the task cannot be found or if
    an issue occurs during deletion.

    Parameters:
    tasks_from_query : list[Task]
        A list of task objects or names obtained from a database query. This list populates the dropdown
        menu where the user selects the task they want to delete.

    Returns: None : This function does not return any value. It directly modifies the Streamlit UI and updates
    the database by deleting the selected task upon form submission.
    """
    with st.form('delete_task', clear_on_submit=True):
        st.write("Delete task:")
        selected_task = st.selectbox('Select a Task to delete', make_tasks_list(tasks_from_query),
                                     index=None, placeholder="Select a task...")
        selected_task_id = find_task_id(tasks_from_query, selected_task)
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            task_to_delete = session.query(Task).filter(Task.id == selected_task_id).first()
            if task_to_delete:
                try:
                    session.query(Task).filter(Task.id == selected_task_id).delete(synchronize_session='fetch')
                    session.commit()
                    st.write(f"The task _'{selected_task}'_ was successfully deleted.")
                except Exception as e:
                    session.rollback()
                    st.write(f"An error occurred: {e}")
                finally:
                    db_engine.close_session()
            else:
                st.write(f"The task _'{selected_task}'_ could not be found.")
        else:
            st.write('To succeed please select input and smash a Submit button.')


def delete_assignee(assignees_from_query: list[Assignee]) -> None:
    """Creates a form in the Streamlit application to delete an existing assignee from the system.

    This function generates a form within a Streamlit app that allows users to delete an existing assignee.
    Users can select an assignee from a dropdown menu and submit the form to remove the assignee from the database.
    The function handles the deletion process, including error handling in case the assignee cannot be found or if
    an issue occurs during deletion.

    Parameters:
    assignees_from_query : list[Assignee]
        A list of assignee objects or names obtained from a database query. This list populates the dropdown
        menu where the user selects the assignee they want to delete.

    Returns: None : This function does not return any value. It directly modifies the Streamlit UI and updates
    the database by deleting the selected assignee upon form submission.
    """
    with st.form('delete_assignee', clear_on_submit=True):
        st.write("Delete assignee:")
        selected_assignee = st.selectbox('Select a Assignee to delete', make_assignees_list(assignees_from_query),
                                         index=None, placeholder="Select a assignee...")
        selected_assignee_id = find_assignee_id(assignees_from_query, selected_assignee)
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            assignee_to_delete = session.query(Assignee).filter(Assignee.id == selected_assignee_id).first()
            if assignee_to_delete:
                try:
                    session.query(Assignee).filter(Assignee.id == selected_assignee_id).delete(
                        synchronize_session='fetch')
                    session.commit()
                    st.write(f"The assignee _'{selected_assignee}'_ was successfully deleted.")
                except Exception as e:
                    session.rollback()
                    st.write(f"An error occurred: {e}")
                finally:
                    db_engine.close_session()
            else:
                st.write(f"The assignee _'{selected_assignee}'_ could not be found.")
        else:
            st.write('To succeed please select input and smash a Submit button.')
