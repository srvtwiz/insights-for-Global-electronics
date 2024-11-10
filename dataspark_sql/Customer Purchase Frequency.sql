SELECT 
    "CustomerKey",
    COUNT("Order Number") AS Purchase_Frequency
FROM 
    final_df
GROUP BY 
    "CustomerKey"
ORDER BY 
    Purchase_Frequency DESC;
