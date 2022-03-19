class Returns:
    INSERTED          = {"error" : False, "body" : "INSERTED"}
    NOT_INSERTED      = {"error" : True,  "body" : "NOT INSERTED"}
    DELETED           = {"error" : False, "body" : "DELETED"}
    NOT_DELETED       = {"error" : True,  "body" : "NOT DELETED"}
    UPDATED           = {"error" : False, "body" : "UPDATED"}
    NOT_UPDATED       = {"error" : True,  "body" : "NOT UPDATED"}
    NULL              = {"error" : True,  "body" : "NULL"}
    TOKEN_NOT_FOUND   = {"error" : True,  "body" : "TOKEN_NOT_FOUND"}
    TOKEN_NOT_DECODED = {"error" : True,  "body" : "TOKEN_NOT_DECODED"}
    TOKEN_NOT_ENCODED = {"error" : True,  "body" : "TOKEN_NOT_ENCODED"}
    USER_NOT_FOUND    = {"error" : True,  "body" : "USER_NOT_FOUND"}
    STUDENT_NOT_FOUND = {"error" : True,  "body" : "STUDENT_NOT_FOUND"}
    LIMIT             = {"error" : True,  "body" : "LIMIT"}
    USER_EXISTS       = {"error" : False,  "body" : "USER_EXISTS"}
    
    def object(obj):
        return {"error" : False, "body" : obj}
    
    def id(obj):
        return {"error" : False, "body" : {"INSERTED_ID" : obj}}
    
    def token(obj):
        return {"error" : False, "body" : {"token" : obj}}