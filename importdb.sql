SELECT *
FROM customers
JOIN internet_service_types USING(internet_service_type_id)
JOIN contract_types USING(contract_type_id)
JOIN payment_types USING (payment_type_id);