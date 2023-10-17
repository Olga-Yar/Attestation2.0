# Платформа торговой сети электроники.

*Приложение выполнено в соответствии с [условиями](README_task.md)*

1. Реализовать модель сети по продаже электроники:

Создано 3 основных модели:
- factory (завод);
- company (ИП);
- retail (розничная сеть).

И 2 вспомогательные модели:
- contacts;
- products.

Модель Factory не может иметь поставщика, так как по умолчанию уровень объекта 0.
У модели могут быть клиенты/покупатели: Company и Retail.

Если Company закупает оборудование непосредственно у Завода, то уровень данного объекта = 1,
если через Retail, то уровень данного объекта = 2.

Аналогичная логика с Retail.

Связь моделей происходит через поле provider (ссылка на модель Contacts).

2. Вывод в админ-панели:
- Ссылка на "Поставщика"

При просмотре списка ИП или розничных сетей отображается столбец "Поставщик"

![Django admin_list_company](/staticfiles/readme_files/Снимок экрана 2023-10-17 в 13.34.12.png)

При нажатии на поставщика, перенаправляет на страницу этого поставщика

![Django admin_provider](/staticfiles/readme_files/Снимок экрана 2023-10-17 в 13.34.30.png)

- Фильтр по названию города и по определенной страны

![Django admin_filter](/staticfiles/readme_files/Снимок экрана 2023-10-17 в 13.40.03.png)

- "admin action", очищающий задолженность перед поставщиком у выбранных объектов

![Django admin_action](/staticfiles/readme_files/Снимок экрана 2023-10-17 в 13.42.54.png)

Итог admin action:

![Django admin_action_result](/staticfiles/readme_files/Снимок экрана 2023-10-17 в 13.44.27.png)

3. Запретить обновление через API поля "Задолженность перед поставщиком"

```
    def update(self, instance, validated_data):
        """Запрет на обновление поля задолженности перед поставщиком"""
        if 'credit' in validated_data:
            raise serializers.ValidationError("Обновление задолженности перед поставщиком запрещено.")

        return super().update(instance, validated_data)
```

4. Настроены права доступа к API так, чтобы только активные сотрудники
имели доступ к API

```
class IsActiveUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_active:
            return True
        return False
```


