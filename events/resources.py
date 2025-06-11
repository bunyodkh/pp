from import_export import resources
from .models import Participant

class ParticipantModelResource(resources.ModelResource):
    class Meta:
        model = Participant
        # Specify the fields to include in the export
        fields = (
            'full_name', 
            'phone_number', 
            'tg_username', 
            'startup_name', 
            'startup_description', 
            'created_at',
            'startup_status',
            'startup_sphere',
            'startup_sphere_other',
            'position_in_startup',
            'has_entrepreneurship_experience',
            'has_attracted_investment',
            'incubators_accelerators',
            'presentation_link',
            'consent'
            )
        # Or exclude specific fields
        # exclude = ('some_field',)
    