email = ['foo@a.com','bar@a.com','baz@b.com','qux@d.com']
# domain
# domain = {}
# username = {}
# for each in email:
#     word = each.split('@')[0]
#     username = each.split('@')[1].split('.')
#     print(domain)
#     print((username))
#     # domain[each.split('@')[0]]= domain.get(each.split('@')[0],0)
#     # username[each.split('@')[1]]= domain.get(each.split('@')[1],0)
    

domain = ['www.siva.com','www.vinoth.com','www.hari.com']
for each in domain:
    print(each.split('.')[1])



