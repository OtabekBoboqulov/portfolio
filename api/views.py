from rest_framework.response import Response
from rest_framework.decorators import api_view
from data.models import UserProfile, ContactMessage
from .serializers import UserProfileSerializer, SkillSerializer, ProjectSerializer, ExperienceSerializer, \
    EducationSerializer, LanguageSerializer, CertificatesSerializer


@api_view(['POST'])
def profile(request):
    name = request.data['name']
    profile = UserProfile.objects.filter(name=name).first()
    profile_serialized = UserProfileSerializer(profile)
    return Response({'profile_data': profile_serialized.data})


@api_view(['POST'])
def skills(request):
    name = request.data['name']
    profile = UserProfile.objects.filter(name=name).first()
    skills = profile.skills.all()
    skills_serialized = SkillSerializer(skills, many=True)
    return Response({'skills_data': skills_serialized.data})


@api_view(['POST'])
def projects(request):
    name = request.data['name']
    profile = UserProfile.objects.filter(name=name).first()
    projects = profile.projects.all()
    projects_serialized = ProjectSerializer(projects, many=True)
    return Response({'projects_data': projects_serialized.data})


@api_view(['POST'])
def project_detail(request, pk=None):
    name = request.data['name']
    profile = UserProfile.objects.filter(name=name).first()
    project = profile.projects.filter(id=pk).first()
    project_serialized = ProjectSerializer(project)
    return Response({'project_data': project_serialized.data})


@api_view(['POST'])
def experiences(request):
    name = request.data['name']
    profile = UserProfile.objects.filter(name=name).first()
    experiences = profile.experiences.all()
    experiences_serialized = ExperienceSerializer(experiences, many=True)
    return Response({'experience_data': experiences_serialized.data})


@api_view(['POST'])
def education(request):
    name = request.data['name']
    profile = UserProfile.objects.filter(name=name).first()
    educations = profile.educations.all()
    educations_serialized = EducationSerializer(educations, many=True)
    return Response({'education_data': educations_serialized.data})


@api_view(['POST'])
def contact(request):
    name = request.data['name']
    profile = UserProfile.objects.filter(name=name).first()
    data = request.data
    message = ContactMessage(sender=data['sender'], email=data['email'], subject=data['subject'],
                             message=data['message'], user=profile)
    message.save()
    return Response({'Message': 'Message saved successfully'})


@api_view(['POST'])
def all_data(request):
    name = request.data['name']
    profile = UserProfile.objects.filter(name=name).first()
    profile_serialized = UserProfileSerializer(profile)
    skills = profile.skills.all()
    skills_serialized = SkillSerializer(skills, many=True)
    projects = profile.projects.all()
    projects_serialized = ProjectSerializer(projects, many=True)
    experiences = profile.experiences.all()
    experiences_serialized = ExperienceSerializer(experiences, many=True)
    educations = profile.educations.all()
    educations_serialized = EducationSerializer(educations, many=True)
    languages = profile.languages.all()
    languages_serialized = LanguageSerializer(languages, many=True)
    certificates = profile.certificates.all()
    certificates_serialized = CertificatesSerializer(certificates, many=True)
    return Response({'profile_data': profile_serialized.data, 'skills_data': skills_serialized.data,
                     'projects_data': projects_serialized.data, 'experience_data': experiences_serialized.data,
                     'education_data': educations_serialized.data, 'language_data': languages_serialized.data,
                     'certificates_data': certificates_serialized.data})


@api_view(['GET'])
def check(request):
    return Response({'status': 'ok'})
