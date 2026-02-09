from datetime import datetime

def current_time()-> str:
    """Return current time in iso format."""
    return datetime.now().isoformat()

if __name__ == "__main__":
    print(current_time())