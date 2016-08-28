from rest_framework.permissions import BasePermission

SAFE_METHODS = ["GET", "HEAD", "OPTIONS"]
class isAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user == "root":
            return True
        elif(request.method in SAFE_METHODS):
            return True
        else:
            return False