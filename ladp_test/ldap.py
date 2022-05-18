from ldap3 import ALL, Connection, Server

# https://ldap3.readthedocs.io/en/latest/tutorial_searches.html

user = "uid=vcloudsync,cn=私有云平台专用账号,ou=私有云服务平台,ou=JFBJ,ou=ZBBJ,dc=csc,dc=local"
user = "cn=私有云平台专用账号,ou=私有云服务平台,ou=JFBJ,ou=ZBBJ,dc=csc,dc=local"
password = "1111111@csc"

server = Server(host="10.237.96.225", port=389, get_info=ALL)
conn = Connection(server, user, password, auto_bind=True)
conn.search('dc=csc,dc=local', '&(objectCategory=person)(objectClass=user)')

# 查看用户信息
conn.extend.standard.who_am_i()
# 查看结果
conn.entries
# 信息??
conn.result