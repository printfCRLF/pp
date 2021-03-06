WITH title_seen_by_524 AS (
    select distinct title
    from film
        join inventory using (film_id)
        join rental using (inventory_id)
    where customer_id = 524
),
customer_seen_same AS (
    select distinct customer_id
    from customer
        join rental using (customer_id)
        join inventory using (inventory_id)
        join film using (film_id)
    where title IN (
            select *
            from title_seen_by_524
        )
),
group_favorite AS (
    select distinct title,
        count(*)
    from customer
        join rental using (customer_id)
        join inventory using (inventory_id)
        join film using (film_id)
    WHERE customer.customer_id IN (
            SELECT *
            from customer_seen_same
        )
    group by title
    order by COUNT(*) DESC
)
select COUNT(*)
from group_favorite as gf
where gf.title NOT IN (
        SELECT title
        from film_title_seen_by_524
    );