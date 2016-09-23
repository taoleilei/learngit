from .Controllers import Home
from .Controllers import Account
from .Controllers import Image
from .Controllers import Region
from .Controllers import Merchant
from .Controllers import Product
from Infrastructure.CheckCode import HttpCheckCode

patterns = [
    # (r"/index$", Home.IndexHandler),
    (r"/Login.html$", Account.LoginHandler),
    (r"/CheckCode.html", HttpCheckCode.CheckCodeHandler),
    # (r"/UploadImg.html$", Image.UploadImageHandler),
    (r"/provinceManager.html$", Region.ProvinceManagerHandler),
    (r"/province.html$", Region.ProvinceHandler),
    (r"/cityManager.html$", Region.CityManagerHandler),
    (r"/city.html$", Region.CityHandler),
    (r"/countyManager.html$", Region.CountyManagerHandler),
    (r"/county.html$", Region.CountyHandler),
    (r"/merchantManager.html$", Merchant.MerchantManagerHandler),
    (r"/merchant.html$", Merchant.MerchantHandler),
    (r"/merchantEdit.html$", Merchant.MerchantEditHandler),
    (r"/ProductManager.html$", Product.ProductManagerHandler),
    (r"/JdProduct.html$", Product.JdProductHandler),
    # (r"/JdProductEdit.html$", Product.JdProductEditHandler),
    # (r"/JdProductPriceManager.html$", Product.JdProductPriceManagerHandler),
    # (r"/JdProductPrice.html$", Product.JdProductPriceHandler),
    # (r"/JdProductDetail.html$", Product.JdProductDetailHandler),
    # (r"/JdProductView.html$", Product.JdProductViewHandler),
    # (r"/TextView.html$", Product.TestProductViewHandler),
    (r"/", Account.LoginHandler),
]