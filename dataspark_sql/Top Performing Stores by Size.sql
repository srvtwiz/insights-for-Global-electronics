SELECT 
    final_df."StoreKey",
    final_df."State_y",
    final_df."Square Meters",
    SUM(final_df."Unit Price USD" * final_df."Quantity" * final_df."Exchange") AS Total_Sales,
    SUM(final_df."Unit Price USD" * final_df."Quantity" * final_df."Exchange") /  NULLIF(final_df."Square Meters", 0) AS Sales_Per_Sqm
FROM 
    final_df
JOIN 
    Sales ON final_df."StoreKey" = Sales."StoreKey"
--JOIN 
   -- Currency ON Sales."Currency_Code" = Currency."Currency_Code"  -- if applicable
GROUP BY 
    final_df."StoreKey", final_df."State_y", final_df."Square Meters"
ORDER BY 
    Sales_Per_Sqm DESC;
