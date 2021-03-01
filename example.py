from genshin import api
import sys

# print(api.get_artifacts().list)
characters = api.get_characters().list
albedo = characters.albedo
print("Name: ", albedo.name)
print("Description: ", albedo.description)
print("Nation: ", albedo.nation)
print("Vision: ", albedo.vision)
print("Talents: ")
for skill in albedo.skillTalents:
    print("Name: ", skill.name)
    print("Unlock", skill.unlock)
    print("Description: ", skill.description)