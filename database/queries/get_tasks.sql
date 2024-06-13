SELECT ROW_NUMBER() OVER (ORDER BY id) AS row_number, task 
    FROM tasks 
    WHERE user_id = %(user_id)d;
