import yaml

# with open("sample.yaml", "r") as stream:
#   try:
#     #print(yaml.load(stream))
#   except yaml.YAMLERROR as err:
#     #print(err)


with open("sample.yaml", "r") as yamlfile:
    yaml_json = yaml.load(yamlfile)
    #print yaml_json
    #print " ------------------------------ "
    #print yaml_json["app"]["arr"].split(", ")
