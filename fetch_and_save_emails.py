from simplegmail import Gmail
import pandas as pd
import numpy as np
from simplegmail.query import construct_query


def fetch_emails():
  """Fetch emails from the past month"""
  print("Authenticating with Gmail...")

  gmail = Gmail()

  print("Fetching recent emails...\n")

  query_parms = {
        "newer_than": (1, "month"),
  }

  messages = gmail.get_messages(query =construct_query(query_parms))
  return messages

  if not messages:
      print("No messages found.")
      return messages
    
  print(f"Found {len(messages)} messages:\n")


def extract_email_data(messages):
  """Extract relevant data from messages"""
  email_data = np.array([])

  for i, message in enumerate(messages, 1):
    try:
      body = message.plain if message.plain else message.snippet

      email_dict = {
        'id': message.id,
        'sender': message.sender,
        'subject': message.subject,
        'date': str(message.date),
        'body_preview': body[:500] if body else '',
        'snippet':message.snippet
      }

      email_data = np.append(email_data, email_dict)

      if i % 50 == 0:
        print(f"Processed {i}/{len(messages)} emails...")
      
    except Exception as e:
      print(f"Error on email {i}: {e}")
      continue
  
  print(f"Extracted {len(email_data)} emails\n")
  return email_data


def save_to_csv(email_data, filename='emails_data.csv'):
  """Save email data to csv"""
  print(f"Saving to {filename}...")

  df = pd.DataFrame(email_data)
  df.to_csv(filename, index=False, encoding='utf-8')

  print(f"Saved {len(df)} emails to CSV\n")
  return df


def main():
  """Run complete pipeline"""
  try:
    messages = fetch_emails()
    email_data = extract_email_data(messages)
    df = save_to_csv(email_data)

    # Display summary
    print("=" * 80)
    print("✓ SUCCESS!")
    print("=" * 80)
    print(f"Emails fetched: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    print(f"File: emails_data.csv")

  except Exception as e:
    print(f"x Error: {e}")
    import traceback
    traceback.print_exc()


if __name__ == "__main__":
    main()     

