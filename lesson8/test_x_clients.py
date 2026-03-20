# 1
# import requests


# base_url = "http://5.101.50.27:8000"

# def test_get_active_companies():
#     # Получить список всех компаний
#     resp = requests.get(base_url+'/company/list')
#     full_list = resp.json()

#     # Получить список активных компаний
#     resp = requests.get(base_url+'/company/list?active=true')
#     filtered_list = resp.json()

#     # Проверить, что список 1 > списка 2
#     assert len(full_list) > len(filtered_list)

# # Получить список активных компаний
# resp = requests.get(base_url+'/company/list', params={'active' : 'true'})
# filtered_list = resp.json()

# 2
# import requests


# base_url = "http://5.101.50.27:8000"

# def get_company_list(params_to_add = None):
#         resp = requests.get(base_url+'/company/list', params_to_add)
#         return resp.json()


# def get_token(user = 'harrypotter', password = 'expelliarmus'):
#     creds = {
#         'username': user,
#         'password': password
#         }
#     resp = requests.post(base_url+'/auth/login', json=creds)
#     return resp.json()["user_token"]


# def create_company(name, description=""):
#     company = {
#             "name": name,
#             "description": description
#      }
#     resp = requests.post(base_url + '/company/create', json=company)
#     return resp.json()


# def test_add_new():
#     # Получить количество компаний до
#     body = get_company_list()
#     len_before = len(body) # Находим длину переменной

#     # Создать новую компанию
#     name = "Autotest"
#     descr = "Descr"
#     create_company(name, descr)

#     # Получить количество компаний после
#     body = get_company_list()
#     len_after = len(body) # Находим длину переменной

#     # Проверить, что размер списка увеличен на +1
#     assert len_after - len_before == 1
#     # Проверить название и описание
#     assert body[-1]["name"] == name
#     assert body[-1]["description"] == descr


# PageObject
from lesson8.CompanyApi import CompanyApi


api = CompanyApi("http://5.101.50.27:8000")

def test_get_companies():
    body = api.get_company_list()
    assert len(body)  > 0

# Проверка получения активных компаний
def test_get_active_companies():
    full_list = api.get_company_list()
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    assert len(full_list)  > len(filtered_list)


 # Проверка добавления новой компании

def test_add_new():
    body = api.get_company_list()
    len_before = len(body)
    name = "Autotest"
    descr = "Descr"
    api.create_company(name, descr)

    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr

def test_get_one_company():
    # Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)

    # Проверим название, описание и статус новой компании:
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True

def test_edit():
    name = "Company to be edited"
    descr = "Edit me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_name = "Updated"
    new_descr = "_upd_"

    edited = api.edit_company(new_id, new_name, new_descr)

    # Проверяем, что название компании поменялось
    assert edited["name"] == new_name
    # Проверяем, что описание компании поменялось
    assert edited["description"] == new_descr

def test_delete():
    name = "Company to be deleted"
    descr = "Delete me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)
    # Проверим название, описание и статус компании:
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True

    # Получаем список компаний и сохраняем его длину
    body = api.get_company_list()
    len_before = len(body)

    # Удаляем компанию
    api.delete_company(new_id)

    # Проверяем, что список компаний меньше на 1
    body = api.get_company_list()
    len_after = len(body)
    assert len_before- len_after == 1

    # Проверяем, что удаленная компания не находится по id
    deleted = api.get_company(new_id)
    assert deleted['detail'] == 'Компания не найдена'

def test_deactivate():
    # Создаем компанию
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]
    # Деактивируем компанию
    body = api.set_active_state(new_id, False)

    # Проверяем, что у компании статус «неактивная»
    assert body["is_active"] is False

def test_deactivate_and_activate_back():
    #Создаем компанию:
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]

    # Деактивируем компанию с помощью параметра False
    body_d = api.set_active_state(new_id, False)
    # Проверяем, что компания не активная
    assert body_d["is_active"] is False

    # Активируем компанию с помощью параметра True
    body_a = api.set_active_state(new_id, True)
    # Проверяем, что компания активная
    assert body_a["is_active"] is True