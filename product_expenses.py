from helpers.database import SessionLocal
from helpers import crud, micro


def product_expense():
    session = SessionLocal()
    department_list = crud.get_all_departments(db=session)
    key = micro.login()
    for department in department_list:
        # if department.is_added == 0:
        try:
            product_expense_list = micro.product_expenses(key=key, department=department.id)
        except:
            key = micro.login()
            product_expense_list = micro.product_expenses(key=key, department=department.id)
        if product_expense_list is None or product_expense_list['dayDishValues'] is None or product_expense_list['dayDishValues']['dayDishValue'] is None:
            continue
        else:
            product_expense_list = product_expense_list['dayDishValues']['dayDishValue']
            crud.add_product_expense(db=session,
                                     product_expense_list=product_expense_list,
                                     department=department.id
                                     )  # not_found_products=not_found_products

        # crud.update_department(db=session, id=department.id)
            # not_found_products = crud.add_product_expense(db=session,
            #                                               product_expense_list=product_expense_list,
            #                                               department=department.id,
            #                                               not_found_products=not_found_products)
            # with open("not_found_products(product_expense).json", "w+") as json_file:
            #     json.dump(not_found_products, json_file)
    micro.logout(key=key)
    # crud.update_all_departments_is_added(db=session, departments=department_list)


if __name__ == '__main__':
    product_expense()
