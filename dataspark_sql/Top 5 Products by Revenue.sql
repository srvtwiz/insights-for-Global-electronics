SELECT 
    "ProductKey",
    "Product Name",
    SUM("Quantity" * "Unit Price USD") AS Total_Revenue
FROM 
    final_df
GROUP BY 
    "ProductKey", "Product Name"
ORDER BY 
    Total_Revenue DESC
LIMIT 5;
