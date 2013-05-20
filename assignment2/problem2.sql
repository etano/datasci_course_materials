SELECT total FROM (
  SELECT A.row_num, B.col_num, SUM(A.value*B.value) AS total
  FROM A,B
  WHERE A.col_num = B.row_num
  GROUP BY A.row_num, B.col_num
) x
WHERE row_num=2 AND col_num=3;
