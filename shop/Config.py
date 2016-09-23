PY_MYSQL_CONN_DICT = {
    "host": '192.168.127.129',
    "port": 3306,
    "user": 'root',
    "passwd": '000000',
    "db": 'ShoppingDb',
    'charset': 'utf8',
}

SQLACHEMY_CONN_STR = "mysql+pymysql://root:000000@192.168.127.129:3306/ShoppingDb?charset=utf8"

# Session类型：cache/redis/memcached
SESSION_TYPE = "cache"
# Session超时时间（秒）
SESSION_EXPIRES = 3 * 60
# Memcache天生支持集群[('1.1.1.1:12000', 1), ('1.1.1.2:12000', 2), ('1.1.1.3:12000', 1)]
MEMCACHE_CONNECT = ['192.168.127.129:12000']

# Redis
REDIS_CONNECT = {
    'host': '192.168.127.129',
    'port': 6379
}

routes = (
    {
        'host_pattern': 'www.oldboy.com',
        'route_path': 'UIWeb.Urls',
        'route_name': 'patterns'
    },
    {
        'host_pattern': 'admin.oldboy.com',
        'route_path': 'UIAdmin.Urls',
        'route_name': 'patterns'},
    {
        'host_pattern': 'dealer.oldboy.com',
        'route_path': 'UIDealer.Urls',
        'route_name': 'patterns'
    }
)


ui_method = (
    'Infrastructure.UIMethods.Null',
)

ui_module = (
    'Infrastructure.UIModules.Null',
)


settings = {
    'template_path': 'Views',  # 模板路径的配置
    'cookie_secret': 'sdfgsdfg',  # cookie加密
    'static_path': 'Statics',  # 设置静态文件解析路径：
    'static_url_prefix': '/Statics/',
    'autoreload': True,
}