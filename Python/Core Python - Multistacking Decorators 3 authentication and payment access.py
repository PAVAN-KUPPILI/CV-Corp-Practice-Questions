def auth_required(fun):
def payment_required(fun):
@auth_required
def download_course():
    print("Course downloaded")
        print("Checking user authentication")
    def inner():
    return inner
    def inner():
        print("Checking payment status")
@payment_required
        fun()
        fun()
    return inner
download_course()