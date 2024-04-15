from routes.brands import brandsBlueprint
from routes.cart_stuff import cartStuffBlueprint
from routes.categories import categoriesBlueprint
from routes.notification import notificationsBlueprint
from routes.order import ordersBlueprint
from routes.payment import paymentsBlueprint
from routes.products import productsBlueprint
from routes.promo_code import promoCodesBlueprint
from routes.suggest import suggestBlueprint
from routes.user import user_bp

blueprints = [
    user_bp,
    productsBlueprint,
    brandsBlueprint,
    cartStuffBlueprint,
    categoriesBlueprint,
    notificationsBlueprint,
    ordersBlueprint,
    paymentsBlueprint,
    promoCodesBlueprint,
    suggestBlueprint,
]
