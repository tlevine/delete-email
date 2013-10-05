#!/usr/bin/env python
import imaplib

def login(server, username, password):
    m = imaplib.IMAP4_SSL(server)
    m.login(username, password)
    return m

def delete_server_messages(m):
    typ, data = m.search(None, 'ALL')
    for num in data[0].split():
        m.store(num, '+FLAGS', '\\Deleted')
    m.expunge()

if __name__ == '__main__':
    import sys
    _, server, username, password = sys.argv
    folder = sys.argv[4] if len(sys.argv) > 4 else 'INBOX'

    m = login(server, username, password)
    m.select(folder)
    delete_server_messages(m)
    m.close()
