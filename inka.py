import os
import json

# Ordner mit den Medien
video_extensions = ('.mp4', '.webm', '.ogv')
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')

media_list = []

for f in os.listdir("."):
    if f.lower().endswith(video_extensions):
        media_list.append({"name": f, "type": "video"})
    elif f.lower().endswith(image_extensions):
        media_list.append({"name": f, "type": "image"})

with open('media.json', 'w') as f:
    json.dump(media_list, f)

print(f"{len(media_list)} Dateien wurden in 'media.json' eingetragen.")