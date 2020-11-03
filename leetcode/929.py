class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid = set()
        
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            for i, c in enumerate(local):
                if c == '+':
                    local = local[:i]
                    break
            valid.add(local+'@'+domain)
        return len(valid)