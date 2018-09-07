def md5(user):
    if not user:
        return ''
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(user)
    m.update(ctime)
    return m.hexdigest()
