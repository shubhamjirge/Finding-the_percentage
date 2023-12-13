"""
Title     : Finding the percentage
Subdomain : Data Types
Domain    : Python
Author    : Shubham Jirge
Created   : 13 December 2023
Updated   : 13 December 2023
Problem   : https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""
if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg_score:.2f}")
