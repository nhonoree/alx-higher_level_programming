-- This script prints the full description of the table first_table

SELECT table_name, 
       column_name, 
       column_type, 
       is_nullable, 
       column_default, 
       extra 
FROM information_schema.columns 
WHERE table_schema = 'hbtn_0c_0' 
  AND table_name = 'first_table';
