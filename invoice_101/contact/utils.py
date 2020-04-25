from uuid import uuid4


def get_contact_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "user/%s/contact_images/%s.%s" % (instance.id, uuid4(), ext)
    return filename
