'''

Write an SQL query to find the following for each invoice_id:

customer_name: The name of the customer the invoice is related to.
price: The price of the invoice.
contacts_cnt: The number of contacts related to the customer.
trusted_contacts_cnt: The number of contacts related to the customer and at the same time they are customers to the shop. (i.e their email exists in the Customers table.)
Return the result table ordered by invoice_id.

The query result format is in the following example.
'''


select
    i.invoice_id,
    c.customer_name,
    i.price,
    count(con.user_id) as contacts_cnt,
    count(c2.email) as trusted_contacts_cnt
from invoices i
join customers c on c.customer_id = i.user_id
left join contacts con on con.user_id = c.customer_id
left join customers c2 on c2.email = con.contact_email
group by i.invoice_id, c.customer_name, i.price
order by i.invoice_id
