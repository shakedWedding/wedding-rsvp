import pandas as pd
from urllib.parse import quote

# Load guests
df = pd.read_csv("guests.csv")

# Base RSVP URL
base_rsvp_url = "https://shakedwedding.github.io/wedding-rsvp/"

# Generate WhatsApp links
def generate_whatsapp_link(name, phone):
    rsvp_link = f"{base_rsvp_url}?name={quote(name)}"
    message = f"Hello {name}, you're invited to our wedding! Please confirm here: {rsvp_link}"
    return f"https://wa.me/{phone}?text={quote(message)}"

df["WhatsApp_Link"] = df.apply(lambda row: generate_whatsapp_link(row["name"], row["phone"]), axis=1)

# Save to CSV
df.to_csv("whatsapp_links.csv", index=False)
print(df[["name", "WhatsApp_Link"]])
