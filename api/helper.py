def show_filter(data, show=[]):
    from collections import OrderedDict

    def inner(x):
        od = OrderedDict().fromkeys(show)
        for k in od.keys():
            if k in show:
                od[k] = x.get(k)
        return od

    res = map(lambda x: inner(x), data)
    return list(res)
