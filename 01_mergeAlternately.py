#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
Name: 
    Baskhuu Batpurev

LeetCode75:
    https://leetcode.com/studyplan/leetcode-75/

Title:
    1768. Merge Strings Alternately
    https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

Problem:
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
    If a string is longer than the other, append the additional letters onto the end of the merged string.
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        word1_i = len(word1)
        word2_i = len(word2)
        max_words_i = max(len(word1), len(word2))
        
        for i in range(max_words_i):
            if i < word1_i:
                result += word1[i]
            if i < word2_i:
                result += word2[i]

        return result

solution = Solution()    
print(solution.mergeAlternately("abc", "pqr"))
print(solution.mergeAlternately("abcd", "pq"))
print(solution.mergeAlternately("ab", "pqrs"))

#End of file
print("EOF")
