SELECT 
    "Category",
    SUM("Quantity") AS Total_Sold
FROM 
    Products
JOIN Sales ON Products."ProductKey" = Sales."ProductKey"
GROUP BY 
    "Category"
ORDER BY 
    Total_Sold DESC;
