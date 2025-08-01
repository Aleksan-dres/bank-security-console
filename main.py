import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__': 

    passcard = Passcard.objects.all() 
    active_passcards = Passcard.objects.filter(is_active=True) 
    print("Активных пропусков",len(active_passcards))  
    
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
