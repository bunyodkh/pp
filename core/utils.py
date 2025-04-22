import os
import uuid
from django.utils.text import slugify

def rename_uploaded_image(instance, filename):
    """
    Rename the uploaded image file to include a unique identifier.
    If the instance has an 'event' attribute, include the event name in the path.
    """
    # Generate a unique identifier for the file
    unique_id = uuid.uuid4().hex[:8]

    # Get the file extension
    ext = filename.split('.')[-1]

    # Check if the instance has an 'event' attribute
    if hasattr(instance, 'event') and instance.event:
        # Use the event name in the file path
        event_name = slugify(instance.event.name)
        new_filename = f"{event_name}-{unique_id}.{ext}"
        return os.path.join('events', new_filename)
    elif hasattr(instance, 'name') and instance.name:
        # Use the instance name (e.g., for EventType) in the file path
        instance_name = slugify(instance.name)
        new_filename = f"{instance_name}-{unique_id}.{ext}"
        return os.path.join('event_types', new_filename)
    else:
        # Default path if no specific attribute is available
        new_filename = f"{unique_id}.{ext}"
        return os.path.join('others', new_filename)
