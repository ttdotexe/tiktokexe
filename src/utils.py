def get_user_speed(default_speed=0.1):
    """Prompt the user for playback speed."""
    try:
        return float(input("Enter playback speed (in seconds, e.g., 0.1): "))
    except ValueError:
        print("[WARNING] Invalid input. Using default speed.")
        return default_speed
