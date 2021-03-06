def container_image_is_external(biocontainers, app):
    """
    Return a boolean: is this container going to be run
    using an external URL (quay.io/biocontainers),
    or is it going to use a local, named Docker image?
    """
    try:
        d = biocontainers[app]
        if (('use_local' in d) and (d['use_local'] is True)):
            # This container does not use an external url
            return False
        else:
            # This container uses a quay.io url
            return True

    except KeyError:
        # No "biocontainers" key specified in params.
        # 
        # We can either crash here,
        # or hope the user knows what
        # they're doing.
        # 
        return True 


def container_image_name(biocontainers, app):
    """
    Get the name of a container image for app,
    using params dictionary biocontainers.

    Verification:
    - Check that the user provides 'local' if 'use_local' is True
    - Check that the user provides both 'quayurl' and 'version'
    """
    if container_image_is_external(biocontainers,app):
        try:
            qurl  = biocontainers[app]['quayurl']
            qvers = biocontainers[app]['version']
            quayurl = "docker://" + qurl + ":" + qvers
            return quayurl
        except KeyError:
            err = "Error: quay.io URL for %s biocontainer "%(app)
            err += "could not be determined"
            raise Exception(err)

    else:
        try:
            dir_loc = biocontainers[app]['location']
            file_name =  biocontainers[app]['filename']
            full_path = "file:"+dir_loc+file_name
            return full_path
        except KeyError:
            err = "Error: the parameters provided specify a local "
            err += "container image should be used for %s, but none "%(app)
            err += "was specified using the 'local' key."
            raise Exception(err)

