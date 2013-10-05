import imaplib

def login(mailbox, username, password):
    mail = imaplib.IMAP4_SSL(mailbox)
    mail.login(username, password)
    return mail

if __name__ == '__main__':
    import sys
    _, mailbox, username, password = sys.argv
    login(mailbox, username, password)
