params = ['value1', 123, 'value3']  # This could be dynamically generated
placeholders = ' , '.join('?' * len(params))  # Create the placeholder string
stored_procedure = f"exec YourStoredProcedure {placeholders} "

#print(stored_procedure)


#dictionay based params

params = {
    'Prob_No': 'P12345',
    'Assigned_Eng_ID': 101,
    'Help_Desk_Comments': 'Help desk comments',
    'Priority': 'High',
    'AssetType': 'Laptop',
    'AssetSubType': 'HP'
}


sql_placeholders = ', '.join([f"@{key} = ?" for key in params.keys()])

# Step 4: Construct the stored procedure call dynamically
sql = f"EXEC TicktGen_Update_User_Problem ({sql_placeholders})"

print(sql)

# Step 5: Execute the SQL with the values from the dictionary (in the correct order)
print(tuple(params.values()))

print(list(params.values()))


