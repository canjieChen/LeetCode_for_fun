# coding=utf-8

"""
每封电子邮件都由一个本地名称和一个域名组成，以 @ 符号分隔。

例如，在 alice@leetcode.com中， alice 是本地名称，而 leetcode.com 是域名。

除了小写字母，这些电子邮件还可能包含 ',' 或 '+'。

如果在电子邮件地址的本地名称部分中的某些字符之间添加句点（'.'），则发往那里的邮件将会转发到本地名称中没有点的同一地址。例如，"alice.z@leetcode.com” 和 “alicez@leetcode.com” 会转发到同一电子邮件地址。 （请注意，此规则不适用于域名。）

如果在本地名称中添加加号（'+'），则会忽略第一个加号后面的所有内容。这允许过滤某些电子邮件，例如 m.y+name@email.com 将转发到 my@email.com。 （同样，此规则不适用于域名。）

可以同时使用这两个规则。

给定电子邮件列表 emails，我们会向列表中的每个地址发送一封电子邮件。实际收到邮件的不同地址有多少？



示例：

输入：["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
输出：2
解释：实际收到邮件的是 "testemail@leetcode.com" 和 "testemail@lee.tcode.com"。


提示：

1 <= emails[i].length <= 100
1 <= emails.length <= 100
每封 emails[i] 都包含有且仅有一个 '@' 字符。每封电子邮件都由一个本地名称和一个域名组成，以 @ 符号分隔。

例如，在 alice@leetcode.com中， alice 是本地名称，而 leetcode.com 是域名。

除了小写字母，这些电子邮件还可能包含 ',' 或 '+'。

如果在电子邮件地址的本地名称部分中的某些字符之间添加句点（'.'），则发往那里的邮件将会转发到本地名称中没有点的同一地址。例如，"alice.z@leetcode.com” 和 “alicez@leetcode.com” 会转发到同一电子邮件地址。 （请注意，此规则不适用于域名。）

如果在本地名称中添加加号（'+'），则会忽略第一个加号后面的所有内容。这允许过滤某些电子邮件，例如 m.y+name@email.com 将转发到 my@email.com。 （同样，此规则不适用于域名。）

可以同时使用这两个规则。

给定电子邮件列表 emails，我们会向列表中的每个地址发送一封电子邮件。实际收到邮件的不同地址有多少？



示例：

输入：["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
输出：2
解释：实际收到邮件的是 "testemail@leetcode.com" 和 "testemail@lee.tcode.com"。


提示：

1 <= emails[i].length <= 100
1 <= emails.length <= 100
每封 emails[i] 都包含有且仅有一个 '@' 字符。
"""


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        temp = []
        new_email = ''
        for k in emails:
            temp_index = k.find('@')
            new_email = k[temp_index:]
            for i in range(temp_index):
                if not k[i].isalpha() and k[i] == '+':
                    k = k[:i] + new_email
                    break
                elif not k[i].isalpha():
                    k = k[:i] + k[i + 1:]
            if k not in temp:temp.append(k)
        return len(temp)

if __name__ == '__main__':
    s = Solution()
    s.numUniqueEmails([
"j+ezsorqlmc@rfpycgjuf.com",
"j+k+ri+rigt.ad@rfpycgjuf.com",
"hfmeqzk.isx+i@fiidmdrsu.com",
"j+p+h+d+d+p+z.j.k.g@rfpycgjuf.com",
"zygekdy.l.w+s@snh.owpyu.com",
"j+m.l+ia+qdgv+w@rfpycgjuf.com",
"r+hwbjwefkp@wcjaki.n.com",
"zygekdy.l.w+d@snh.owpyu.com",
"bizdm+sz.f.a.k@il.cjjlp.com",
"hfmeqzk.isx+t@fiidmdrsu.com",
"hfmeqzk.isx+i@fiidmdrsu.com",
"bizdm+f+j+m.l.l@il.cjjlp.com",
"zygekdy.l.w+g@snh.owpyu.com",
"r+evgvxmksf@wcjaki.n.com",
"hfmeqzk.isx+h@fiidmdrsu.com",
"bizdm+lov+cy@il.cjjlp.com",
"hfmeqzk.isx+o@fiidmdrsu.com",
"bizdm+hs+qao@il.cjjlp.com",
"r+v+z+rcuznrj@wcjaki.n.com",
"j+r.kn+h.w.a.h+bh@rfpycgjuf.com",
"hfmeqzk.isx+t@fiidmdrsu.com",
"hfmeqzk.isx+a@fiidmdrsu.com",
"zygekdy.l.w+o@snh.owpyu.com",
"zygekdy.l.w+i@snh.owpyu.com",
"r+vy.u.y+f.er+aw@wcjaki.n.com",
"zygekdy.l.w+c@snh.owpyu.com",
"bizdm+wztzg@il.cjjlp.com",
"j+h.fwbsr+chp@rfpycgjuf.com",
"zygekdy.l.w+s@snh.owpyu.com",
"zygekdy.l.w+d@snh.owpyu.com",
"bizdm+qq.o.q+p@il.cjjlp.com",
"zygekdy.l.w+o@snh.owpyu.com",
"j+c+zqbq+h.dyt@rfpycgjuf.com",
"r+hl.b.i+fz.hz.t@wcjaki.n.com",
"r+cbabpf.k+w+e@wcjaki.n.com"
])