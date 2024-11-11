SELECT 
    "State_y",
    SUM(final_df."Unit Price USD" * final_df."Quantity" * final_df."Exchange") AS Total_Sales
FROM 
    final_df
GROUP BY 
    "State_y"
ORDER BY 
    Total_Sales DESC;
