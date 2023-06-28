create view min_amount as
select book_author, sum(amount) min_amount from vh_vika.book group by book_author having sum(amount) = (select min(sum_amount) from (select sum(amount) sum_amount from vh_vika.book group by book_author))

select * from min_amount