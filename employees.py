from helpers.database import SessionLocal
from helpers import crud, micro


def employees():
    session = SessionLocal()
    key = micro.login()
    # department_list = crud.get_all_departments(db=session)
    # for department in department_list:
    #     departments_dict[f"{department.code}"] = department.id
    try:
        employee_list = micro.employee_list(key=key)
    except:
        key = micro.login()
        employee_list = micro.employee_list(key=key)

    crud.add_employees(db=session, employee_list=employee_list)
    micro.logout(key=key)


if __name__ == '__main__':
    employees()
