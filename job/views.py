from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from .tasks import fetch_data_task

class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobRangeList(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = Job.objects.all()
        start = self.request.query_params.get('start', None)
        end = self.request.query_params.get('end', None)
        if start is not None and end is not None:
            queryset = queryset[int(start):int(end)]
        return queryset
    
fetch_data_task()