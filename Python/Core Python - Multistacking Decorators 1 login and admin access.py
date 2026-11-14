def login_required(func):
    def inner():
    return inner
def admin_required(func):
    def inner():
    return inner
        print("Checking login")
        print("Checking admin permission")
        func()
        func()
@login_required
@admin_required
def delete_record():
    print("Record deleted")
delete_record()