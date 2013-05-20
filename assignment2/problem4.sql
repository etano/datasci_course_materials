SELECT MAX(similarity) FROM (
  SELECT SUM(A.count*B.count) AS similarity
    FROM (SELECT * FROM Frequency WHERE docid!="q") AS A,
         (SELECT * FROM (SELECT 'q' as docid, 'washington' as term, 1 as count
                         UNION
                         SELECT 'q' as docid, 'taxes' as term, 1 as count
                         UNION
                         SELECT 'q' as docid, 'treasury' as term, 1 as count)) AS B
    WHERE A.term = B.term
    GROUP BY A.docid
  ) x;
