# Write your code here
from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='None')
    deadline = Column(Date, default=datetime.now())

    def __repr_(self):
        return self.task


def main():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    while True:
        choice = int(input(
            "1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit\n"))
        print()
        if choice not in [1, 2, 3, 4, 5, 6, 0]:
            print('Enter a valid choice!\n')
            continue
        elif choice == 1:
            print(f'Today {datetime.now().strftime("%d %b")}:')
            if len(session.query(Table).filter(Table.deadline == datetime.now().date()).all()) == 0:
                print('Nothing to do!\n')
                continue
            else:
                print(*(f'{i}. {j.task}' for i, j in
                        enumerate(session.query(Table).filter(Table.deadline == datetime.now().date()).all(), 1)),
                      sep='\n')
                print()
                continue
        elif choice == 2:
            for i in range(7):
                day_of_week = datetime.now().date() + timedelta(days=i)
                print(day_of_week.strftime('%A %d %b:'))
                filter_deadline = session.query(Table).filter(Table.deadline == day_of_week)
                if not list(filter_deadline):
                    print('Nothing to do!\n')
                else:
                    for i, j in enumerate(filter_deadline, 1):
                        print(f'{i}. {j.task}')
                    print()
                    continue
        elif choice == 3:
            print('All tasks:')
            if len(session.query(Table).all()) == 0:
                print('Nothing to do!\n')
                continue
            else:
                print(*(f'{i}. {j.task}. {j.deadline.strftime("%d %b")}' for i, j in
                        enumerate(session.query(Table).order_by(Table.deadline).all(), 1)),
                      sep='\n')
                print()
                continue
        elif choice == 4:
            print('Missed tasks:')
            if len(session.query(Table).filter(Table.deadline < datetime.now().date()).all()) == 0:
                print('Nothing is missed!\n')
            else:
                print(*(f'{i}. {j.task}. {j.deadline.strftime("%d %b")}' for i, j in
                        enumerate(session.query(Table).order_by(Table.deadline).filter(
                            Table.deadline < datetime.now().date()).all(), 1)), sep='\n')
                print()
        elif choice == 5:
            tasks = input('Enter task\n')
            deadlines = input('Enter deadline\n')
            new_row = Table(task=tasks, deadline=datetime.strptime(deadlines, '%Y-%m-%d'))
            session.add(new_row)
            session.commit()
            print('The task has been added!\n')
        elif choice == 6:
            if len(session.query(Table).all()) == 0:
                print('Nothing to delete!\n')
                continue
            else:
                print("Choose the number of the task you want to delete:")
                print(*(f'{i}. {j.task}. {j.deadline.strftime("%d %b")}' for i, j in
                        enumerate(session.query(Table).order_by(Table.deadline).all(), 1)),
                      sep='\n')
                print()
                number_delete = int(input())
                session.delete(session.query(Table).order_by(Table.deadline).all()[number_delete - 1])
                session.commit()
                print("The task has been deleted!\n")
        elif choice == 0:
            print('Bye!', end='')
            break


if __name__ == '__main__':
    main()
