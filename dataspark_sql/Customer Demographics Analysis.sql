SELECT 
    "Gender",
    CASE 
        WHEN "age" BETWEEN 18 AND 25 THEN '18-25'
        WHEN "age" BETWEEN 26 AND 35 THEN '26-35'
        WHEN "age" BETWEEN 36 AND 50 THEN '36-50'
        WHEN "age" > 50 THEN '50+'
        ELSE 'Unknown' 
    END AS Age_Group,
    "Country",
    COUNT("CustomerKey") AS Customer_Count
FROM 
    Customers
GROUP BY 
    "Gender", Age_Group, "Country"
ORDER BY 
    "Country", "Gender", Age_Group;
