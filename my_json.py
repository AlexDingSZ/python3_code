import  json

jsondict = {"name":"mytest", "type":{"name":"type_name", "other_para":["1", "2"]}}
jsonarray = [{"name":"xiaohong", "weight":"60"},{"name":"xiaohong", "weight":"45"}]
jsonstr1 = json.dumps(jsondict)
jsonstr2 = json.dumps(jsonarray)

print (type(jsonstr1), jsonstr1)
print (type(jsonstr1), jsonstr2)

json1 = json.loads(jsonstr1)
json2 = json.loads(jsonstr2)

print(json1.keys())
print(json1["name"])
print(json1["type"]["other_para"][1])
print(type(json1),json1)
print(type(json2),json2)
