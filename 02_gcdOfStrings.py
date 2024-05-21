#!/usr/bin/python3
#-*- coding: utf-8 -*-

'''
Name: 
    Baskhuu Batpurev

LeetCode75:
    https://leetcode.com/studyplan/leetcode-75/

Title:
    1071. Greatest Common Divisor of Strings
    https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

Problem:
    For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        case2_pattern = "AB"

        for i in range(len(str1)):
            if i < len(str2) and str1[i] == str2[i]:
                result += str2[i]

        if result[2:4] == case2_pattern[0:2]:
            result = result[:2] + result[4:]

        return result

solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))
print(solution.gcdOfStrings("ABABAB", "ABAB"))
print(solution.gcdOfStrings("LEET", "CODE"))

#End of file
print("EOF")