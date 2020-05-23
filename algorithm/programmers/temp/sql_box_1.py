"""

SELECT 
GAME_USERS.ID USER_ID,
count(PURCHASES.USER_ID) PURCHASE_COUNT,
IFNULL(sum(CHARACTERS.PRICE),0) TOTAL_PRICE
from GAME_USERS
left JOIN PURCHASES on GAME_USERS.ID = PURCHASES.USER_ID
left JOIN CHARACTERS on PURCHASES.ITEM = CHARACTERS.NAME
group by PURCHASES.USER_ID
having PURCHASE_COUNT >= 0
order by USER_ID asc


"""