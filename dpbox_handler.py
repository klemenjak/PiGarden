import dropbox


def init_dropbox():
    with open ("dropbox_token.txt", "r") as myfile:
        token=myfile.read().replace('\n', '')
    return dropbox.Dropbox(token)


def get_account_info(dbx):
    return dbx.users_get_current_account()


def upload_file(dbx, filename, destination):
    with open(filename, 'rb') as f:
        dbx.files_upload(f.read(), destination + filename)
