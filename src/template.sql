DECLARE condition STRING DEFAULT '{condition_string1}';

SELECT
  {column_names}
FROM `table_{table_name}`
WHERE condition_column1 = condition
  AND condition_column2 in ({condition_string2})