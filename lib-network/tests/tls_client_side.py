# $ uv run python --version
# Python 3.13.9

# https://medium.com/@cumulus13/building-bulletproof-ssl-tls-connections-in-python-a-developers-guide-to-secure-socket-4cb1c2d9544e


# https://docs.python.org/3/library/ssl.html

import socket, ssl

# C:\Users\russ\python-misc\lib-network\tests\tls_client_side.py:7: DeprecationWarning: ssl.PROTOCOL_TLSv1_2 is deprecated

# C:\Users\russ\python-misc\lib-network\tests\tls_client_side.py:7: DeprecationWarning: ssl.PROTOCOL_TLSv1_2 is deprecated
# https://crypto.stackexchange.com/questions/76811/what-encryption-to-choose-from-the-ssl-library-in-python-3
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, 
server_hostname='www.verisign.com')
ssl_sock.connect(('www.verisign.com', 443))

print(s)
print(ssl_sock)

# https://github.com/tlsfuzzer/tlslite-ng