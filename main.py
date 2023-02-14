import json
import os
import sys

from utils import run


def main():
    pr_id = json.loads(sys.argv[1])['event']['number']
    print(f'pr_id: {pr_id}')

    with open('settings.json', 'r') as f:
        settings = json.load(f)

    # run(['ls', '/submissions'])
    run(['cp', os.path.join('/submissions', f'fishyscapes_pr_{pr_id}'), os.path.join('/tmp', f'fishyscapes_pr_{pr_id}.simg')])

    run(['mkdir', '-p', settings['tmp_pred_path']])
    run(['rm', '-rf', os.path.join(settings['tmp_pred_path'], '*')])
    cmd = [
        'singularity', 'run', '--nv', '--pwd', settings['run']['pwd'],
        '--bind', f"{settings['tmp_pred_path']}:{settings['run']['pred_path']},"
                  f"{settings['val_rgb_path']}:{settings['run']['rgb_path']}",
        os.path.join('/tmp', f'fishyscapes_pr_{pr_id}.simg')
    ]
    run(cmd)


if __name__ == '__main__':
    main()