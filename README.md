Single Turn Task
response = client.chat.completions.create(model="",messages=[{role:user,content:prompt}])
Multi Turn Task 
response = client.chat.completions.create(model="",messages=[{role:system,content:prompt},{role:user,content:prompt}])
Guardrails - We can use 'system messages' to add guardrails which are specific restrictions on what the model can generate 