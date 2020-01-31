import dropbox


def init_dropbox():
    with open ("dropbox_handler.txt", "r") as myfile:
    token=myfile.readlines()
    return dropbox.Dropbox(token)


def get_account_info(dbx):
    return dbx.users_get_current_account()


def upload_file(dbx, filename, destination):
    with open(filename, 'rb') as f:
        dbx.files_upload(f.read(), destination + filename)
