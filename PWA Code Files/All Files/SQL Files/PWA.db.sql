
CREATE TABLE IF NOT EXISTS
user notes (
      user_id INTEGER PRIMARY KEY AUTOINCREMENT
      user_name VARCHAR(200)
      secret_password VARCHAR(150)
      created_at (7.34 05/12/25)  -- ISO 8601 timestamp
      updated_at (7.34 05/12/25)  -- ISO 8601 timestamp
      is_private INTEGER DEFAULT 1 

)

SELECT user_id, user_name, secret_password, AS preview, created_at  (7.34 05/12/25)
FROM user notes
WHERE user_id = ?
ORDER BY created_at (7.34 05/12/25) DESC
LIMIT 200 OFFSET ?;

