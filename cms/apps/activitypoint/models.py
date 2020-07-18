from django.db import models
from django.conf import settings
# Create your models here.
class Activitypoints(models.Model):
    date=models.DateField(null=True)
    ACTIVITY_CHOICES = [
        ('ncc', 'N C C'),
        ('nss', 'N S S'),
        ('sports', 'Sports'),
        ('games', 'Games'),
        ('music', 'Music'),
        ('performingarts','Performing Arts'),
        ('literaryarts','Literary arts'),
        ('techfestquiz','Tech Fest, Tech Quiz'),
        ('moocfinalass','Massive Open Online Courses with final assessment certificate'),
        ('competition','Competition conducted by Professional Societies - (IEEE, IET, ASME, SAE, NASA etc.)'),
        ('attendingseminariit','Attending Full time Conference/Seminars/Exhibitions/Workshop/ STTP conducted at IITs /NITs'),
        ('attendingseminarktu','Attending Full time Conference/Seminars/Exhibitions/Workshop/ STTP conducted at KTU or its affiliated institutes'),
        ('paperiit','Paper presentation/publication at IITs/NITs'),
        ('paperktu','Paper presentation/publication at KTU or its affiliated institutes'),
        ('posteriit','Poster Presentation at IITs /NITs'),
        ('posterktu','Poster Presentation at KTU or its affiliated institutes'),
        ('industrialtraining','Industrial Training/Internship (atleast for 5 full days)'),
        ('industrialexhibition','Industrial/Exhibition visits'),
        ('foreign','Foreign Language Skill(TOEFL/IELTS/ BEC examsetc.)'),
        ('startup','Start-up Company –Registered legally'),
        ('pfield','Patent - Filed'),
        ('ppublished','Patent - Published'),
        ('papproved','Patent- Approved'),
        ('plicensed','Patent- Licensed'),
        ('prototype','Prototype developed and tested'),
        ('awards','Awards for Products developed'),
        ('innovative','Innovative technologies developed and used by industries/users'),
        ('gotventure','Got Venture capital funding for innovative ideas/products'),
        ('startup','Startup Employment(Offering jobs to two persons not less than Rs. 15000/- per month)'),
        ('societal','Societal innovations'),
        ('studentps','Student Professional Societies (IEEE, IET, ASME, SAE, NASA etc.)'),
        ('college','College Association Chapters(Mechanical, Civil, Electrical etc.)'),
        ('festival','Festival & Technical Events(College approved)'),
        ('hobbyclub','Hobby Club'),
        ('elected','Elected student representatives')

    ]
    activity = models.CharField(max_length=100,choices=ACTIVITY_CHOICES,default="ncc")
    ACTIVITY_LEVEL=[
        ('notapplicable','Not Applicable'),
        ('collegeevents','I (College Events)'),
        ('zonalevents','II (Zonal Events)'),
        ('stateuniversityevents','III (State/ University Events)'),
        ('nationalevents','IV (National Events)'),
        ('internationalevents','V (International Events)')
    ]
    activitylevel=models.CharField(max_length=100,choices=ACTIVITY_LEVEL,default='notapplicable')
    PRIZE_LEVEL=[
        ('notapplicable','Not Applicable'),
        ('participant','Participant'),
        ('first','First'),
        ('second','Second'),
        ('third','Third')
    ]
    prize=models.CharField(max_length=100,choices=PRIZE_LEVEL,default="notapplicable")
    INVOLVEMENT_TYPE=[
        ('notapplicable','Not Applicable'),
        ('corecoordinator','Core coordinator'),
        ('subcoordinator','Sub coordinator'),
        ('volunteer','Volunteer')
    ]
    involvement=models.CharField(max_length=100,choices=INVOLVEMENT_TYPE,default="notapplicable",blank=False)
    document=models.FileField(upload_to='uploads/')
    YEAROF=[
        ('firstyear','First Year'),
        ('secondyear','Second Year'),
        ('thirdyear','Third Year'),
        ('fourthyear','Fourth Year')
    ]
    year=models.CharField(max_length=100,choices=YEAROF,default="firstyear")
    notes=models.CharField(max_length=300,blank=True)
    points=models.IntegerField(default=0)
    student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)