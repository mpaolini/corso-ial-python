from django.core.management.base import NoArgsCommand

import requests
import os

headers = {'Authorization': 'Bearer X8Vd5NDweMMAAAAAAAAAATqgLGrVSu_6NN61xocrbxHXGEut7b1FfHym5GSwwJoD'}


class Command(NoArgsCommand):

    def handle_noargs(self, **opts):
        resp = requests.get('https://api.dropbox.com/1/metadata/dropbox/',
                            headers=headers)
        resp.raise_for_status()
        for item in resp.json()['contents']:
            if item['is_dir']:
                continue
            resp = requests.get(
                'https://api-content.dropbox.com/1/files/dropbox{}'
                .format(item['path']),
                headers=headers)
            resp.raise_for_status()
            with open(os.path.join('media', item['path'].lstrip('/')), 'wb') as f:
                f.write(resp.content)
