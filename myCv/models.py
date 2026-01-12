from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    position = models.CharField(max_length=30, default='')
    bio = models.TextField()
    contact = models.CharField(max_length=30, default='No phone number')
    email= models.EmailField()
    address = models.TextField(max_length=255, default='Unknown Address')
    linkedin = models.URLField(blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    
class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name= "skills")
    name = models.CharField(max_length= 50)    
    level = models.PositiveIntegerField(help_text="Skill level(0-100)")
    
    
    def __str__(self):
        return f"{self.name} ({self.level}%)"
    
    
class workExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="work_experience")
    title = models.CharField(max_length=100)
    company= models.CharField(max_length=100)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20)
    descri = models.TextField()
    
    def __str__(self):
        return f"{self.title} - {self.company}"
    
    
class Academic(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="academics")
    institution = models.CharField(max_length=100)
    paper = models.CharField(max_length=100)
    years = models.CharField(max_length=20)
    descri = models.TextField()
    
    
    def __str__(self):
        return f"{self.paper} - {self.institution}"
    
    
class Language(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="languages")
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(help_text="Proficiencylevel(0-100)")
    
    def __str__(self):
        return f"{self.name} ({self.level})"
    
class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    picture = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    descri = models.TextField()
    
    def __str__(self):
        return self.title
    
class Referee(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="referees")
    name = models.CharField(max_length=100)
    position= models.CharField(max_length=100)
    email= models.EmailField()
    
    def __str__(self):
       return  self.name
        
class Message(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    message= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name}"
    
class Hobby(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="hobbies")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name