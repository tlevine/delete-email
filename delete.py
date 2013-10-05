#!/usr/bin/env python
import imaplib

def login(server, username, password):
    m = imaplib.IMAP4_SSL(server)
    m.login(username, password)
    return m

def select_and_count(m, folder):
    return 'There remain %s messages in %s.' % (m.select(folder)[1][0].decode('ascii'), folder)

def delete_server_messages(m, folder, chunk_size = 100):
    select_and_count(m, folder)
    typ, data = m.search(None, 'ALL')
    for i, num in enumerate(data[0].split()):
        if i % chunk_size == 0:
            # So we can see the progress
            m.expunge()
            print(select_and_count(m, folder))
        m.store(num, '+FLAGS', '\\Deleted')

if __name__ == '__main__':
    import sys
    _, server, username, password = sys.argv
    folder = sys.argv[4] if len(sys.argv) > 4 else 'INBOX'

    m = login(server, username, password)
    delete_server_messages(m, folder)
    m.close()
