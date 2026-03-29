# Проект автоматизации тестирования с Allure

Проект содержит автоматизированные тесты с использованием Page Object Model и интеграцией Allure для формирования отчетов.

## Запуск тестов для формирования отчётов
 
 Для запуска всех тестов ввести команду
 pytest --alluredir=allure-results

## Запуск конкретного теста

 Для запуска конкретного теста ввести команду

 # Тест формы регистрации
 pytest test_01_form_page_obj.py --alluredir=allure-results

 # Тест калькулятора
 pytest test_calculator.py --alluredir=allure-results

 # Тест SauceDemo
 pytest test_saucedemo_checkout_pom.py --alluredir=allure-results

## Запуск с подробным выводом
 pytest -v --alluredir=allure-results

## Очистка предыдущих результатов перед запуском
 pytest --alluredir=allure-results --clean-alluredir


### Просмотр сформированного отчета Allure
 После запуска тестов выполните команду:
 allure serve allure-results