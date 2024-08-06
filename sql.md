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

## 32. HAVING
* We cannot use use `WHERE` to filter based off of aggregate results, because those happen after a `WHERE` is executed.
* `HAVING` allows us to use the aggregate result as a filter along with a `GROUP BY`.

Snytax:
```sql
-- Example 6:
SELECT company, SUM(sales)
    FROM finance_table
    WHERE company != 'Google'
    GROUP BY company
    HAVING SUM(sales) > 1000;
```

## 39. AS Statement
* The `AS` operator gets executed at the very end of a query, meaning that we can not use the alias inside a `WHERE` operator.

Snytax:
```sql
-- Example 7:
SELECT customer_id, amount AS new_name
    FROM payment
    WHERE new_name > 2;

-- Example 8:
SELECT customer_id, SUM(amount) AS total_spent
    FROM payment
    GROUP BY customer_id
    HAVING SUM(amount) > 100
```

## 40. Inner Joins
* If you see just `JOIN` without the `INNER`, PostgreSQL will treat it as an `INNER JOIN`.

Syntax:
```sql
-- Example 9:
SELECT payment_id, payment.customer_id, first_name
	FROM payment
	INNER JOIN customer
	ON payment.customer_id = customer.customer_id;

-- Example 10:
SELECT reg_id, Logins.name, log_id
    FROM Registrations
    INNER JOIN Logins
    ON Registrations.name = Logins.name
```

## 41. Full Outer Joins
* Symmetric

Syntax:
```sql
-- Example 11:
SELECT *
    FROM tableA
    FULL OUTER JOIN tableB
    ON tableA.col_match = tableB.col_match
```

Full Outer Join with `WHERE`
* Symmetric

Syntax:
```sql
-- Example 12:
SELECT *
    FROM tableA
    FULL OUTER JOIN tableB
    ON tableA.col_match = tableB.col_match
    WHERE tableA.id IS NULL OR tableB.id IS NULL    
```

## 42. Left Outer Joins

Syntax:
```sql
-- Example 13:
SELECT *
    FROM tableA
    LEFT OUTER JOIN tableB
    ON tableA.col_match = tableB.col_match
```

`LEFT OUTER JOIN` with `WHERE`

Syntax:
```sql
-- Example 14:
SELECT *
    FROM tableA
    LEFT OUTER JOIN tableB
    ON tableA.col_match = tableB.col_match
    WHERE tableB.id IS NULL;
```
