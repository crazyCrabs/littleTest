from ldap3 import SUBTREE, Connection, Server
from logbook.base import Logger

logger = Logger("ladp", level="info")

ldap_host = '10.237.96.225'  # ldap服务器地址
ldap_port = 389  # 默认389
ldap_admin_user = 'xx'  # ldap管理员账户用户名
ldap_admin_password = 'xxx'  # ldap管理员账户密码
ldap_base_search = 'dc=csc,dc=loacl'  # 查询域



def ldap_auth(username, password):
    '''
    ldap验证方法
    :param username: 用户名
    :param password: 密码
    :return: 
    '''
    s = Server(host=ldap_host, port=ldap_port, use_ssl=False, get_info='ALL', connect_timeout=3)

    # 连接ldap服务器
    ldapz_admin_connection = Connection(s, user=ldap_admin_user, password=ldap_admin_password, auto_bind='NONE',
                                        version=3,
                                        authentication='SIMPLE', client_strategy='SYNC', auto_referrals=True,
                                        check_names=True,
                                        read_only=False, lazy=False,
                                        raise_exceptions=False)

    # 连上以后必须bind才能有值
    ldapz_admin_connection.bind()

    # 这个是为了查询你输入的用户名的入口搜索地址
    res = ldapz_admin_connection.search(search_base=ldap_base_search,
                                        search_filter='(sAMAccountName={})'.format(
                                            username),
                                        search_scope=SUBTREE,
                                        attributes=['cn', 'givenName',
                                                    'mail', 'sAMAccountName'],
                                        )

    try:
        if res:
            entry = ldapz_admin_connection.response[0]
            logger.info(entry)
            dn = entry['dn']
            attr_dict = entry['attributes']
            logger.info('attr_dic:%s' % attr_dict)

            try:
                # 这个connect是通过你的用户名和密码还有上面搜到的入口搜索来查询的
                conn2 = Connection(s, user=dn, password=password,
                                   check_names=True, lazy=False, raise_exceptions=False)
                conn2.bind()
                # logger.info(conn2.result["description"])

                # 正确-success 不正确-invalidCredentials
                if conn2.result["description"] == "success":
                    logger.info("ldap auth pass!")
                    return True
                else:
                    logger.info("username or password error!")
                    return False
            except Exception as e:
                logger.info("username or password error!")
                logger.info(e)
                return False
    except KeyError as e:
        logger.info("username or password error!")
        logger.info(e)
        return False

ldap_auth("1", "2")
