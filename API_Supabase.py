#  pip install supabase
#  API Settings
#  Project URL  https://paiumevgqnprrgthcapn.supabase.co
#  Project API Keys : eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBhaXVtZXZncW5wcnJndGhjYXBuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM4NTUzNzcsImV4cCI6MjA1OTQzMTM3N30.cafWpvjcrD4kq1y5JQ4bqVuHsqGRY3AjyGyYZQJUTro

import os
from supabase import create_client, Client
from dotenv import load_dotenv

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

response = (
    #supabase.table("Clientes")
    supabase.table("comp_quimica")
    .select("*")
    .execute()
)
print(response)