"""
sql 문제 풀이

#여러기준으로 출력
SELECT ANIMAL_ID, NAME, DATETIME from ANIMAL_INS 
order by NAME asc, DATETIME desc

#상위 n개 출력
SELECT NAME from ANIMAL_INS
order by DATETIME asc limit 1

#최대/최소값 구하기
SELECT DATETIME 시간 from ANIMAL_INS
order by DATETIME desc limit 1

# 카운트
SELECT count(*) from animal_ins

# 중복제거
SELECT  count(distinct name) from ANIMAL_INS

#항목별 카운트
SELECT ANIMAL_TYPE,	count(ANIMAL_TYPE) cnt from ANIMAL_INS
group by ANIMAL_TYPE

#중복이름 카운트, having 사용해서 null 제외 
SELECT NAME, count(NAME) count from ANIMAL_INS
group by NAME
having count > 1

#입양시각 구하기 찾을 시간 범위 정하고 카운트하고 그룹별로 카운트
SELECT hour(DATETIME) HOUR, count(hour(DATETIME)) COUNT from ANIMAL_OUTS
where hour(DATETIME) >= 9
and hour(DATETIME) <= 19
group by HOUR
order by HOUR asc

#입양시각 구하기(2), 참고 https://mentha2.tistory.com/97?category=356750
UNION : 2개 이상의 쿼리를 결합할 때 사용
UNION, UNION ALL 2가지를 사용할 수 있음
UNION > 결합 시 중복은 제거
UINON ALL > 중복 제거 X




#조인
SELECT AO.ANIMAL_ID , AO.NAME FROM ANIMAL_OUTS AS AO 
LEFT JOIN ANIMAL_INS AS AI 
ON (AI.ANIMAL_ID = AO.ANIMAL_ID AND AI.ANIMAL_TYPE = AO.ANIMAL_TYPE) 
WHERE AI.ANIMAL_ID IS NULL ORDER BY AO.ANIMAL_ID

"""