import os
from uuid import uuid4
from django.utils.timezone import now

def rename_uploaded_image(instance, filename):
    """
    Custom function to rename uploaded images.
    The new name will include the event name and a unique identifier.
    """
    ext = filename.split('.')[-1]  # Get the file extension
    new_filename = f"{instance.event.name}_{uuid4().hex}.{ext}"  # Generate a unique filename
    return os.path.join('events', new_filename)  # Save in the 'events/' directory
