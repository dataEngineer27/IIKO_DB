from helpers.database import SessionLocal
from helpers import crud, micro


def employee_roles():
    session = SessionLocal()
    key = micro.login()
    try:
        roles = micro.employee_roles(key=key)
    except:
        key = micro.login()
        roles = micro.employee_roles(key=key)

    crud.add_roles(db=session, role_list=roles)
    micro.logout(key=key)


if __name__ == '__main__':
    employee_roles()
