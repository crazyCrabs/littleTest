from ldap3 import SUBTREE, Connection, Server

_ldap_host = "10.237.96.225"
_ldap_port = 389
_ldap_admin_user = "cn=私有云平台专用账号,ou=私有云服务平台,ou=JFBJ,ou=ZBBJ,dc=csc,dc=local"
_ldap_admin_password = "1111111@csc"
_ldap_base_search = "dc=csc,dc=local"

username = ''
password = ''

s = Server(host=_ldap_host, port=_ldap_port, use_ssl=False, get_info="ALL", connect_timeout=30)

ldapz_admin_connection = Connection(
            s,
            user=_ldap_admin_user,
            password=_ldap_admin_password,
            auto_bind="NONE",
            version=3,
            authentication="SIMPLE",
            client_strategy="SYNC",
            auto_referrals=True,
            check_names=True,
            read_only=False,
            lazy=False,
            raise_exceptions=False,
        )

ldapz_admin_connection.bind()

res = ldapz_admin_connection.search(
        search_base=_ldap_base_search,
        search_filter="(sAMAccountName={})".format(username),
        search_scope=SUBTREE,
        attributes=["cn", "givenName", "mail", "sAMAccountName"],
    )

print(f'>>> search {username} res: ', res)

entry = ldapz_admin_connection.response[0]
dn = entry["dn"]
print(">>> dn info: ", dn)

conn2 = Connection(s, user=dn, password=password, check_names=True, lazy=False, raise_exceptions=False)
conn2.bind()

print(f'>>> finally {username} result: ', conn2.result["description"])
