from django.db import models
from django.urls import reverse
from Home.models import Teacher


class FeedbackData(models.Model):

    class Meta:
        verbose_name_plural = 'Feedback Data'

    
    BasicChoice = (
        ('Demonstrates professional competence and mastery of subject matter', 'Demonstrates professional competence and mastery of subject matter'),
        ('Meets commitments, observes deadlines and achieves desired results', 'Meets commitments, observes deadlines and achieves desired results'),
        ('Admits mistakes and refocuses efforts when appropriate','Admits mistakes and refocuses efforts when appropriate'),
        ('Completes own work on time','Completes own work on time'),
        ('Ensures that written correspondence is neat and professional','Ensures that written correspondence is neat and professional'),
        ('Works to overcome obstacles to completing tasks or assignments','Works to overcome obstacles to completing tasks or assignments')
    )

    IntermediateChoice = (
        ('Shows persistence when faced with difficult problems or challenges','Shows persistence when faced with difficult problems or challenges' ),
        ('Modifies behaviour as appropriate to meet the expectations of the position and the situation','Modifies behaviour as appropriate to meet the expectations of the position and the situation'),
        ('Accepts responsibility for outcomes (positive or negative) of ones work, and admits mistakes and refocuses efforts when appropriate','Accepts responsibility for outcomes (positive or negative) of ones work, and admits mistakes and refocuses efforts when appropriate'),
        ('Sets high standards of work performance for self','Sets high standards of work performance for self'),
        ('Reviews own work and others for quality','Reviews own work and others for quality'),
        ('Dedicates required time and energy to assignments or tasks that no aspects of the work is neglected','Dedicates required time and energy to assignments or tasks that no aspects of the work is neglected')
    )

    AdvancedChoice = (
        ('Expresses personal developmental goals and engages in activities to achieve them','Expresses personal developmental goals and engages in activities to achieve them' ),
        ('Acknowledges others desire for development and creates a team atmosphere towards mutual improvement','Acknowledges others desire for development and creates a team atmosphere towards mutual improvement'),
        ('Provides encouragement and support to others in accepting responsibility','Provides encouragement and support to others in accepting responsibility'),
        ('Does not accept others denial of responsibility without questioning','Does not accept others denial of responsibility without questioning'),
        ('Sets high standards of performance for team, group or others','Sets high standards of performance for team, group or others'),
        ('Sets examples of high-quality work for peers','Sets examples of high-quality work for peers')
    )

    SuperiorChoice = (
        ('Demonstrates a high level of personal responsibility, dependability and reliability','Demonstrates a high level of personal responsibility, dependability and reliability' ),
        ('Exhibits values, attitudes and behaviours of the organization','Exhibits values, attitudes and behaviours of the organization'),
        ('Establishes criteria and/or work procedures to achieve a high level of quality, productivity and service','Establishes criteria and/or work procedures to achieve a high level of quality, productivity and service')
    )
    date_submitted = models.DateTimeField(auto_now=True)

    teacher_name = models.CharField(verbose_name='Name:', max_length=225,
                                     blank=False)


    punctuality = models.CharField(verbose_name='Department', max_length=225,
                                blank=False)

    portion = models.CharField(verbose_name='College', max_length=225,
                                blank=False)

    basic = models.CharField(verbose_name='Basic',
                             max_length=225,
                             choices=BasicChoice)

    intermediate = models.CharField(verbose_name='Intermediate',
                             max_length=225,
                             choices=IntermediateChoice)


    advanced = models.CharField(verbose_name='Advanced',
                             max_length=400,
                             choices=AdvancedChoice)

    superior = models.CharField(verbose_name='Superior',
                             max_length=225,
                             choices=SuperiorChoice)

    

    def __str__(self) -> str:
        return self.teacher_name




    def get_absolute_url(self):
        return reverse('SuccessView')
