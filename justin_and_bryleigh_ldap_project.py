#UserList
user_data = (
    {
        "uid=joe,ou=users,dc=acme,dc=com": {
            "uid": "joe",
            "firstName": "Joe",
            "lastName": "Jones",
            "email": "joejones@acme.com",
            "department": "Sales",
            "location": "US",
            "status": "active"
        },
        "uid=john,ou=users,dc=acme,dc=com": {
            "uid": "john",
            "firstName": "John",
            "lastName": "Jacobson",
            "email": "john.jacobson@acme.com",
            "department": "Sales",
            "location": "CA",
            "status": "terminated"
        },
        "uid=laura,ou=users,dc=acme,dc=com": {
            "uid": "laura",
            "firstName": "Laura",
            "lastName": "Johnson",
            "email": "laura.johnson@xyz.com ",
            "department": "Marketing",
            "location": "US",
            "status": "active"
        },
        "uid=jack,ou=users,dc=acme,dc=com": {
            "uid": "jack",
            "firstName": "Jack",
            "lastName": "Jackson",
            "email": "jack.jackson@company",
            "department": "Sales",
            "location": "US",
            "status": "active"
        },
        "uid=emily,ou=users,dc=acme,dc=com": {
            "uid": "emily",
            "firstName": "Emily",
            "lastName": "Jameson",
            "email": "Emily.Jameson@acme.com",
            "department": "Sales",
            "location": "CA",
            "status": "terminated"
            },
        "uid=jeremy,ou=users,dc=acme,dc=com": {
            "uid": "jeremy",
            "firstName": "Jeremy",
            "lastName": "Jordan",
            "email": "Jeremy.Jordan@abc.com",
            "department": "Marketing",
            "location": "CA",
            "status": "active"
        },
        "uid=sarah,ou=users,dc=acme,dc=com": {
            "uid": "sarah",
            "firstName": "Sarah",
            "lastName": "Jenkins",
            "email": "sarah.jenkins@acme.com",
            "department": "Marketing",
            "location": "US",
            "status": "active"
        }
}
)
# If you need to see userdata
# print(user_data)

def list_of_people(key,value):
    list_to_return = []
    #for each record in user_data
    for key, value in user_data.items():
        #   check if location matches passed parameter
        if key[1]['location'] == key and value[1]['us'] == value:
            list_to_return.append(user[1]['uid'])
        elif key[1]['firstname'] == key and value[1][Joe] == value:
            list_to_return.append(user[1]['uid'])
    #   return "uid"
    return list_to_return
print(list_of_people("location","US"))
