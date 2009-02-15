def rawr(foo='foo',bar='bar'):
    print "FOO IS %s BAR IS %s" % (foo, bar)

if __name__ == '__main__':
    rawr('oof', 'rab')

    data = {'foo':'FRAWR', 'bar':'BAWRA'}
    rawr(**data)
