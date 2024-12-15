""""Database"""

from sqlalchemy.orm import sessionmaker
from models import engine, Task


class Data:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_task(self, title, description):
        """Inserta una nueva tarea en la base de datos"""
        try:
            task = Task(title=title, description=description)
            self.session.add(task)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"Error al crear tarea, {e}")
        return task

    def get_tasks(self):
        """Obtiene todas las tareas de la base de datos"""
        try:
            tasks = self.session.query(Task).all()
        except Exception as e:
            self.session.rollback()
            print(f"Error al consultar, {e}")
        return tasks

    def update_task(self, id):
        """Actualiza el estado de una tarea en la base de datos"""
        try:
            task = self.session.query(Task).filter_by(id=id).first()
            task.done = True
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"Error al actualizar, {e}")
        return task

    def delete_task(self, id):
        """Elimina una tarea de la base de datos"""
        try:
            task = self.session.query(Task).filter_by(id=id).first()
            self.session.delete(task)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"Error al eliminar, {e}")
        return task
