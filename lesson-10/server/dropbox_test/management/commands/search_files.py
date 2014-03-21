from django.core.management.base import LabelCommand

import requests


headers = {'Authorization': 'Bearer X8Vd5NDweMMAAAAAAAAAATqgLGrVSu_6NN61xocrbxHXGEut7b1FfHym5GSwwJoD'}

class Command(LabelCommand):

    def handle_label(self, label, **opts):
        resp = requests.get('https://api.dropbox.com/1/search/dropbox/',
                            params={'query': label},
                            headers=headers)
        resp.raise_for_status()
        for item in resp.json():
            # print('path: {path} size: {size}'.format(
            #     path=item['path'],
            #     size=item['size']))
            # print('path: {item[path]} size: {item[size]}'.format(item=item))
            if not item['is_dir']:
                print('path: {path} size: {size} mime type: {mime_type}'.format(**item))
