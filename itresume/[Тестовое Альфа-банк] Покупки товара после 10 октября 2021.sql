

'''
Необходимо вывести количество людей, которые покупали товар с id = 5 после 10 октября 2021 (включительно).
'''


select count(distinct customer.id_customer)

from customer inner join purchases on customer.id_customer = purchases.user_id inner join skus on skus.id = purchases.sku_id
where skus.id = 5 and purchases.created_at >='2021-10-10'
