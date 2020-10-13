from controllers import favsControllers,LoginUserControllers, RegisterUserControllers, ProductsControllers, ordersControllers
routes = {
"register": "/api/v01/register", "register_controllers": RegisterUserControllers.as_view("register_api"),
"login": "/api/v01/login", "login_controllers": LoginUserControllers.as_view("login_api"),
"products": "/api/v01/products", "products_controllers": ProductsControllers.as_view("products_api"),
"orders": "/api/v01/orders", "orders_controllers": ordersControllers.as_view("orders_api"),
"fav": "/api/v01/fav/<id_f>", "fav_controllers": favsControllers.as_view("fav_api")



}

