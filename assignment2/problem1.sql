SELECT count(*) FROM (
  SELECT docid FROM Frequency WHERE term='transactions' GROUP BY docid
  INTERSECT
  SELECT docid FROM Frequency WHERE term='world' GROUP BY docid
) x;
