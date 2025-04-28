def validate_zip(zip_code):
    """Validate that the zip code is 5 digits."""
    return zip_code.isdigit() and len(zip_code) == 5
