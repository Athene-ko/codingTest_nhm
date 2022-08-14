-- NOT IN
# SELECT name AS Customers FROM Customers WHERE id NOT IN (SELECT customerId FROM Orders);

-- LEFT JOIN
SELECT name AS Customers FROM Customers c LEFT JOIN Orders o ON c.id = o.customerId WHERE o.customerId is Null;