/*
Name: 
    Baskhuu Batpurev

SQL 50:
    https://leetcode.com/studyplan/top-sql-50/

Title:
    1757. Recyclable and Low Fat Products
    https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50

Problem:
    product_id is the primary key (column with unique values) for this table.
    low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
    recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
*/

-- Write your MySQL query statement below
SELECT product_id FROM Products WHERE low_fats = "Y" and recyclable = "Y"