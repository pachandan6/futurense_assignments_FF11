-- 06/05/2022
-- Aggregate Funtions

-- count--
select COUNT(customerNumber) as No_of_Customers,paymentDate from payments group by paymentDate;

-- max---
select MAX(customerNumber) as Max_No_of_Customers,paymentDate from payments group by paymentDate order by Max_No_of_Customers desc;

-- min---
select min(customerNumber) as min_No_of_Customers,paymentDate from payments group by paymentDate order by min_No_of_Customers ;

-- avg --
select round(avg(amount)) as AvgAmount,paymentDate from payments group by paymentDate order by AvgAmount;

-- sum--
select round(sum(amount)) as TotalAmount,paymentDate from payments group by paymentDate order by TotalAmount;

-- CASE WHEN--

Select amount,
case 
when amount > 100000 then "High"
when amount > 50000 and amount <100000 then "Medium"
when amount <50000 then "low"
else "very less"
end as AmountStatus
from payments;








