# Section 3: GROUP BY Statements

## 28. Aggregation Functions

### Most Common Aggregate Functions:
* `AVG()`, `COUNT()`, `MAX()`, `MIN()`, `SUM()`

Syntax:
```sql
-- Example 1:
SELECT MAX(replacement_cost), MIN(replacement_cost)
    FROM film;

-- Example 2:
SELECT ROUND(AVG(replacement_cost), 3)
    FROM film;
```

## 29. GROUP BY - Part 1
* The `GROUP BY` clause must appear right after a `FROM` or `WHERE` statement.
* In the `SELECT` statement, columns must either have an aggregate function or be in the `GROUP BY` call.
* `WHERE` statements should not refer to the aggregation result, later on we will learn to use `HAVING` to filter on those results.
* If you want to sort results based on the aggregate, make sure to reference the entire function.

Syntax:
```sql
-- Example 3:
SELECT category_col, AGG(data_col)
    FROM table
    GROUP BY category_col;

-- Example 4:
SELECT category_col, AGG(data_col)
    FROM table
    WHERE category_col != 'A'
    GROUP BY category_col;

-- Example 5:
SELECT company, SUM(sales)
    FROM finance_table
    GROUP BY company
    ORDER BY SUM(sales)
    LIMIT 5;
```
