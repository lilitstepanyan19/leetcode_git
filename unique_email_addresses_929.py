def numUniqueEmails(emails):
    res = set()
    for el in emails:
        name, domain = el.split('@')
        name = name.split('+')[0]
        name = name.replace('.', '')
        res.add(f'{name}@{domain}')
    return len(res) 
    # res = []
    # for el in emails:
    #     if el.count('@') != 1:
    #         continue
    #     name, domain = el.split('@')
    #     if '+' in name:
    #         name = name.split('+')[0]
    #     if '.' in name:
    #         name = name.replace('.', '')
    #     # if domain.count('.') == 1:            
    #     res.append(name + "@" + domain)
    # return len(set(res))

print(numUniqueEmails(["test.email+alex@leetcode.com",\
    "test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
print(numUniqueEmails(["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com",\
    "fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com",\
    "r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com",\
    "r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com",\
    "r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com",\
    "fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com",\
    "fg.r.u.uzj+fek@kziczvh.com"]))