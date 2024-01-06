from helpers.database import SessionLocal
from helpers import crud, micro


def shift_list():
    session = SessionLocal()
    key = micro.login()
    department_list = crud.get_all_departments(db=session)
    i = 0
    for department in department_list:
        i += 1
        try:
            shifts = micro.shift_list(key=key, department_id=department.id)
        except:
            key = micro.login()
            shifts = micro.shift_list(key=key, department_id=department.id)

        crud.add_shifts(db=session, shift_list=shifts, department_id=department.id)
    print(f"Was processed {i} departments")

    micro.logout(key=key)


if __name__ == '__main__':
    shift_list()
