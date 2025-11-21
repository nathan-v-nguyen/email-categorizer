from simplegmail import Gmail

def main():
    print("Authenticating with Gmail...")

    gmail = Gmail()

    print("Fetching recent emails...\n")

    messages = gmail.get_messages()

    if not messages:
        print("No messages found.")
        return
    
    print(f"Found {len(messages)} messages:\n")

    for i, message in enumerate(messages, 1):
        print(f"{i}. Subject: {message.subject}")
        print(f"   From: {message.sender}")
        print(f"   Date: {message.date}")
        print("-" * 80)

if __name__ == "__main__":
    main()        
