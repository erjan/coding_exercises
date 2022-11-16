Find the number of emails received by each user under each built-in email label. The email labels are: 'Promotion', 'Social', and 'Shopping'. Output the user along with the number of promotion, social, and shopping mails count,.


with h as(
select 
label,
to_user, count(*) as cnt
from google_gmail_emails g1 inner join google_gmail_labels g2 on g1.id = g2.email_id

group by to_user, label)

select to_user,
count(label)
-- sum(case when label = 'Promotion' then cnt else 0 end)as prom_cnt,
-- sum(case when label = 'Social' then cnt else 0 end)as soc_cnt,
-- sum(case when label = 'Shopping' then cnt else 0 end)as shop_cnt



from h where label in ('Promotion', 'Social', 'Shopping')
group by to_user
