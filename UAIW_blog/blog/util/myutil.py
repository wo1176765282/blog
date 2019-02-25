from django.shortcuts import redirect,reverse
def authuser(fn):
    def newfn(request):
        username = request.session.get('username',None)
        if username:
            res = fn(request)
            return res
        else:
            return redirect(reverse("userauth:login"))
    return newfn