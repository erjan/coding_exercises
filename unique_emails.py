'''
Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 
'''


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def get_local_name(self,email):
            local_name = email.split('@')[0]
            domain_name = email.split('@')[1]
            #print('local name now %s' % local_name)
            local_name = local_name.replace('.', '')
            #print('after removing dots , the local name: %s' % local_name)
            local_name = local_name.split('+')[0]
            #print('returning this local name: %s' % local_name)
            return local_name +  '@' + domain_name
        
            
        local_names = set()
        for email in emails:
            local_names.add(get_local_name(self,email))
        return len(local_names)

