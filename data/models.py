from django.db import models
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_image = CloudinaryField('profile', blank=True, resource_type='image',
                                    folder='portfolio/profile_images')
    resume = CloudinaryField('resume', blank=True, resource_type='raw', folder='portfolio/resumes')
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'User Profiles'


class Skill(models.Model):
    Levels = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, choices=Levels)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    responsibilities = models.TextField()
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    image = CloudinaryField('project', blank=True, resource_type='image', folder='portfolio/project_images')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title


class Experience(models.Model):
    company_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='experiences')

    def __str__(self):
        return f'{self.company_name} - {self.position}'


class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='educations')

    def __str__(self):
        return f'{self.degree} - {self.institution}'


class ContactMessage(models.Model):
    sender = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='contact_messages')

    def __str__(self):
        return f'{self.sender} - {self.subject}'
