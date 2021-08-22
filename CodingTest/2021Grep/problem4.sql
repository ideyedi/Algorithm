SELECT EMPLOYEE_ID,
    CASE
        WHEN count(CREATED_AT) >= 4 THEN '최우수 사원'
        WHEN count(CREATED_AT) = 3 or count(CREATED_AT) = 2 THEN '우수 사원'
        ELSE '일반 사원'  
    END as '분류 상태'
    , count(CREATED_AT) as COUNT
FROM SELLINGS GROUP BY EMPLOYEE_ID ORDER BY EMPLOYEE_ID