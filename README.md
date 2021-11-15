## Run server
```
python migrate.py runserver
```
На данный момент реализованы приложения: landing, orders, products. 
<p>В дальнейшем сайт будет дополняться.</p>

## Целевая страница
![landing](https://github.com/PavVlada/test/blob/screenshots/screenshots/landing.png)
Вводятся имя и email пользователя, которые будут занесены в БД

## Начальная страница
![home1](https://github.com/PavVlada/test/blob/screenshots/screenshots/home1.png)
![home2](https://github.com/PavVlada/test/blob/screenshots/screenshots/home2.png)
Выгружает из БД активные товары и выводит на страницу

## Админка
![admin](https://github.com/PavVlada/test/blob/screenshots/screenshots/admin.png)

### Landing - Пользователи
![user](https://github.com/PavVlada/test/blob/screenshots/screenshots/admin-landing-user.png)
Здесь содержатся те данные, которые пользователи ввели на целевой странице
### Orders - Заказы
![order](https://github.com/PavVlada/test/blob/screenshots/screenshots/admin-orders-order.png)
Здесь содержатся данные о сделанных заказах
![order-change](https://github.com/PavVlada/test/blob/screenshots/screenshots/admin-orders-order-change.png)
Автоматический подсчет итоговой суммы в зависимости от количества и цены товаров
### Orders - Статус заказов
![status](https://github.com/PavVlada/test/blob/screenshots/screenshots/admin-orders-status.png)
### Orders - Товары в заказе
![productinorder](https://github.com/PavVlada/test/blob/screenshots/screenshots/admin-orders-productinorder.png)
Здесь содержатся данные о заказанных товарах
### Products - Товары
![Product](https://github.com/PavVlada/test/blob/screenshots/screenshots/admin-products-product.png)
Здесь содержатся данные обо всех товарах. Отсюда выгружаются данные на начальной странице
### Products - Товары - изменение товара
![productinorer-change](https://github.com/PavVlada/test/blob/screenshots/screenshots/admin-products-product-change.png)
Имеется связь с фотографиями. Также возможно загрузить фотографии, которые автоматически сохранятся в БД
### Products - Фотографии
![productimage](https://github.com/PavVlada/test/blob/screenshots/screenshots/admin-products-productimage.png)
