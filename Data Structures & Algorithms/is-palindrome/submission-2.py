class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join([c.lower() for c in s if c.isalnum()])

        return cleaned_text == cleaned_text[::-1]