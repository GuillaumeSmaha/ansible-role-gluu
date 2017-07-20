from org.xdi.model.custom.script.type.uma import AuthorizationPolicyType
from org.xdi.util import StringHelper, ArrayHelper
from java.util import Arrays, ArrayList, HashSet
from org.xdi.oxauth.service.uma.authorization import AuthorizationContext

import java

class AuthorizationPolicy(AuthorizationPolicyType):
    def __init__(self, currentTimeMillis):
        self.currentTimeMillis = currentTimeMillis

    def init(self, configurationAttributes):
        print "UMA authorization policy. Initialization"

        self.clientsSet = self.prepareClientsSet(configurationAttributes)
        print "UMA authorization policy. Initialization. Count authorized clients: %s" % self.clientsSet.size()

        print "UMA authorization policy. Initialized successfully"

        return True   

    def destroy(self, configurationAttributes):
        print "UMA authorization policy. Destroy"
        print "UMA authorization policy. Destroyed successfully"
        return True   

    def getApiVersion(self):
        return 1

    # Process policy rule
    #   authorizationContext is org.xdi.oxauth.service.uma.authorization.AuthorizationContext
    #   configurationAttributes is java.util.Map<String, SimpleCustomProperty>
    def authorize(self, authorizationContext, configurationAttributes):
        print "UMA Authorization policy. Attempting to authorize client"
        client_id = authorizationContext.getGrant().getClientId()

        print "UMA Authorization policy. Client: ", client_id
        if (self.clientsSet.contains(client_id)):
            print "UMA Authorization policy. Authorizing client"
            return True
        else:
            print "UMA Authorization policy. Client isn't authorized"
            return False

        print "UMA Authorization policy. Authorizing client"
        return True

    def prepareClientsSet(self, configurationAttributes):
        clientsSet = HashSet()
        if (not configurationAttributes.containsKey("allowed_clients")):
            return clientsSet

        allowedClientsList = configurationAttributes.get("allowed_clients").getValue2()
        if (StringHelper.isEmpty(allowedClientsList)):
            print "UMA authorization policy. Initialization. The property allowed_clients is empty"
            return clientsSet    

        allowedClientsListArray = StringHelper.split(allowedClientsList, ",")
        if (ArrayHelper.isEmpty(allowedClientsListArray)):
            print "UMA authorization policy. Initialization. There aren't clients specified in allowed_clients property"
            return clientsSet
        
        # Convert to HashSet to quick search
        i = 0
        count = len(allowedClientsListArray)
        while (i < count):
            client = allowedClientsListArray[i]
            clientsSet.add(client)
            i = i + 1

        return clientsSet
