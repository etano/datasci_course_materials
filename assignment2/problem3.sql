SELECT
  (SELECT SUM(A.count*B.count)
  FROM (SELECT * FROM Frequency WHERE docid="10080_txt_crude") AS A,
       (SELECT * FROM Frequency WHERE docid="17035_txt_earn") AS B
  WHERE A.term = B.term);
