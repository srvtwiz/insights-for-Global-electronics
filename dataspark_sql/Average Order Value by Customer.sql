SELECT 
    "CustomerKey",
    AVG(final_df."Unit Price USD" * final_df."Quantity" * final_df."Exchange") AS Average_Order_Value
FROM 
    final_df
GROUP BY 
    "CustomerKey"
ORDER BY 
    Average_Order_Value DESC;
