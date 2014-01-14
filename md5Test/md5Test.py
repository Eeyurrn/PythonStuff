import md5

s = "Let's build Autotrader"

hash = md5.new()
hash.update(s)

print "The hash for \"%s\" is %s"% (s, hash.hexdigest())


