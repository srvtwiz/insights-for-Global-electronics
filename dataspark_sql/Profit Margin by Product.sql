SELECT 
    "ProductKey",
    "Product Name",
    AVG("Unit Price USD" - "Unit Cost USD") AS Average_Profit_Margin
FROM 
    final_df
GROUP BY 
    "ProductKey", "Product Name"
ORDER BY 
    Average_Profit_Margin DESC;
