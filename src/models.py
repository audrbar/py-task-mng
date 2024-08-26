"""Data Model for Entire App."""
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import Relationship

from src.base import TimeStampedModel, PersonModel, Model


class Project(TimeStampedModel):
    """Represents a project within the system, including its name, aim, budget, and associated relationships.

    This model defines a project entity with attributes for its name, aim, and budget. It also establishes
    relationships with other entities, specifically a one-to-one relationship with a `Manager` and a
    one-to-many relationship with `Task` entities.

    Attributes:
    project_name : sqlalchemy.Column
        The name of the project. It is a required field with a maximum length of 80 characters.
    project_aim : sqlalchemy.Column
        The aim or goal of the project. It is a required field with a maximum length of 80 characters.
    project_budget : sqlalchemy.Column
        The budget allocated for the project. It is a required field and represented as a floating-point number.

    Relationships:
    manager_id : sqlalchemy.Column
        The foreign key that links the project to a `Manager`. This is a one-to-one relationship, meaning
        each project has exactly one manager. The `ondelete='CASCADE'` setting ensures that if the manager
        is deleted, the project will also be deleted. The `unique=True` constraint enforces the one-to-one
        relationship.
    manager : sqlalchemy.orm.Relationship
        A SQLAlchemy relationship that represents the connection between the `Project` and its `Manager`.
        The `single_parent=True` parameter ensures that a `Manager` can be associated with only one `Project`
        at a time.
    tasks : sqlalchemy.orm.Relationship
        A one-to-many relationship between the `Project` and `Task` entities. Each project can have multiple
        tasks associated with it. The `cascade="all, delete-orphan"` option ensures that if a project is
        deleted, all associated tasks are also deleted. The `passive_deletes=True` option allows for efficient
        deletion of tasks without requiring explicit deletion commands.

    Methods:
    __repr__():
        Returns a string representation of the `Project` instance, showing the project name and budget.
    """
    __tablename__ = "projects"

    project_name = Column(String(80), nullable=False)
    project_aim = Column(String(80), nullable=False)
    project_budget = Column(Float, nullable=False)

    # One-to-one relationship with Manager
    manager_id = Column(Integer, ForeignKey('managers.id', ondelete='CASCADE'), unique=True, nullable=False)
    manager = Relationship("Manager", back_populates="project", uselist=False, single_parent=True)

    # One-to-many relationship with Tasks
    tasks = Relationship("Task", back_populates="project", cascade="all, delete-orphan", passive_deletes=True)

    def __repr__(self) -> str:
        return f"<Project(name={self.project_name}, budget={self.project_budget})>"


class Manager(PersonModel):
    """Represents a manager within the system, including personal details and their associated project.

    This model defines a manager entity, inheriting from the `PersonModel` class, which typically includes
    attributes such as `firstname`, `lastname`, `salary`, and `email`. The `Manager` class establishes a
    one-to-one relationship with the `Project` class, indicating that each manager is responsible for exactly
    one project.

    Attributes:
    Inherited from `PersonModel`:
        firstname : sqlalchemy.Column
            The first name of the manager.
        lastname : sqlalchemy.Column
            The last name of the manager.
        salary : sqlalchemy.Column
            The salary of the manager.
        email : sqlalchemy.Column
            The email address of the manager.

    Relationships:
    project : sqlalchemy.orm.Relationship
        A one-to-one relationship with the `Project` class. Each manager is associated with exactly one project,
        and this relationship is bidirectional, meaning that the `Project` class also references the `Manager`.
        The `cascade="all, delete-orphan"` option ensures that if a manager is deleted, the associated project
        is also deleted. The `uselist=False` parameter enforces the one-to-one nature of this relationship.

    Methods:
    __repr__():
        Returns a string representation of the `Manager` instance, showing the manager's firstname, lastname,
        salary, and email.
    """
    __tablename__ = "managers"

    # One-to-one relationship with Project
    project = Relationship("Project", back_populates="manager", cascade="all, delete-orphan", uselist=False)

    def __repr__(self) -> str:
        return (f"<Manager(firstname={self.firstname}, lastname={self.lastname}, salary={self.salary}, "
                f"email={self.email})>")


class Assignee(PersonModel):
    """Represents an assignee within the system, including personal details and their assigned tasks.

    This model defines an assignee entity, inheriting from the `PersonModel` class, which typically includes
    attributes such as `firstname`, `lastname`, `salary`, and `email`. The `Assignee` class establishes a
    many-to-many relationship with the `Task` class, indicating that an assignee can be associated with
    multiple tasks, and each task can have multiple assignees.

    Attributes:
    Inherited from `PersonModel`:
        firstname : sqlalchemy.Column
            The first name of the assignee.
        lastname : sqlalchemy.Column
            The last name of the assignee.
        salary : sqlalchemy.Column
            The salary of the assignee.
        email : sqlalchemy.Column
            The email address of the assignee.

    Relationships:
    tasks : sqlalchemy.orm.Relationship
        A many-to-many relationship with the `Task` class. This relationship is managed through an association
        table named `assignee_tasks`, which links `Assignee` and `Task` entities. The `cascade="all, delete"`
        option ensures that if an assignee is deleted, the corresponding entries in the association table are
        also removed, maintaining referential integrity.

    Methods:
    __repr__():
        Returns a string representation of the `Assignee` instance, showing the assignee's firstname, lastname,
        salary, email, and the number of tasks they are associated with.
    """
    __tablename__ = "assignees"

    # Many-to-many relationship with Tasks
    tasks = Relationship("Task", secondary="assignee_tasks", back_populates="assignees", cascade="all, delete")

    def __repr__(self) -> str:
        return (f"<Assignee(firstname={self.firstname}, lastname={self.lastname}, salary={self.salary}, "
                f"email={self.email}, tasks={len(self.tasks)})>")


class Task(TimeStampedModel):
    """Represents a task within the system, including its name, dates, status, and associated relationships.

    This model defines a task entity with attributes for its name, start date, due date, completion date,
    and status. The `Task` class establishes relationships with other entities, specifically a many-to-one
    relationship with the `Project` class and a many-to-many relationship with the `Assignee` class.

    Attributes:
    task_name : sqlalchemy.Column
        The name of the task. It is a required field with a maximum length of 80 characters.
    start_date : sqlalchemy.Column
        The date when the task is scheduled to start. It is a required field.
    due_date : sqlalchemy.Column
        The date by which the task is expected to be completed. It is a required field.
    done_date : sqlalchemy.Column
        The date when the task was actually completed. This field is optional.
    status : sqlalchemy.Column
        The current status of the task (e.g., "not_started", "in_progress", "done"). It is a required field.

    Relationships:
    project_id : sqlalchemy.Column
        The foreign key that links the task to a `Project`. This is a many-to-one relationship, meaning that
        each task is associated with one project. The `ondelete='CASCADE'` setting ensures that if the project
        is deleted, the associated tasks are also deleted.
    project : sqlalchemy.orm.Relationship
        A SQLAlchemy relationship that represents the connection between the `Task` and its `Project`.
        This relationship is bidirectional, with the `Project` class referencing its related tasks.
    assignees : sqlalchemy.orm.Relationship
        A many-to-many relationship with the `Assignee` class. This relationship is managed through an
        association table named `assignee_tasks`, which links `Task` and `Assignee` entities. The `cascade="all,
        delete"` option ensures that if a task is deleted, the corresponding entries in the association table are also
        removed, maintaining referential integrity.

    Methods:
    __repr__():
        Returns a string representation of the `Task` instance, showing the task's ID and name.
    """
    __tablename__ = "tasks"

    task_name = Column(String(80), nullable=False)
    start_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    done_date = Column(Date, nullable=True)
    status = Column(String(80), nullable=False)

    # Many-to-one relationship with Project
    project_id = Column(Integer, ForeignKey("projects.id", ondelete='CASCADE'), nullable=False, index=True)
    project = Relationship("Project", back_populates="tasks")

    # Many-to-many relationship with Assignees
    assignees = Relationship("Assignee", secondary="assignee_tasks", back_populates="tasks",
                             cascade="all, delete")

    def __repr__(self) -> str:
        return f"<Task(id={self.id}, name={self.task_name})>"


class AssigneeTask(TimeStampedModel):
    """Represents the association between an Assignee and a Task within the system.

    This model defines an association table that implements a many-to-many relationship between the `Assignee`
    and `Task` classes. Each record in the `AssigneeTask` table links a specific assignee to a specific task,
    allowing multiple assignees to be associated with a single task and multiple tasks to be assigned to a single
    assignee.

    Attributes:
    assignee_id : sqlalchemy.Column
        The foreign key that links this record to an `Assignee`. This field is part of the composite primary key,
        and the `ondelete="CASCADE"` option ensures that if the referenced assignee is deleted, the corresponding
        records in this table are also deleted.
    task_id : sqlalchemy.Column
        The foreign key that links this record to a `Task`. This field is also part of the composite primary key,
        and the `ondelete="CASCADE"` option ensures that if the referenced task is deleted, the corresponding
        records in this table are also deleted.

    Methods:
    __repr__():
        Returns a string representation of the `AssigneeTask` instance, showing the associated assignee and task IDs.
    """
    __tablename__ = "assignee_tasks"

    assignee_id = Column(Integer, ForeignKey("assignees.id", ondelete="CASCADE"), primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True)

    def __repr__(self) -> str:
        return f"<AssigneeTask(assignee_id={self.assignee_id}, task_id={self.task_id})>"
